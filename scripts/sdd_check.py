"""Compare requirement definitions in two Markdown SDDs. Python 3.9+, standard library.

Usage: python scripts/sdd_check.py OLD NEW [--json] [--check]
JSON includes both full inventories. Section records retain unlabelled prose. A
requirement body runs to the next definition or section heading, including its
lists, tables, formulas and fenced examples. Repeated blocks are kept in order.
Changelog item names are local to their revision. Cross-references do not start
new definitions. Line numbers are locations, never inputs to change detection.
"""
import argparse
import difflib
import json
from pathlib import Path
import re
import sys

# G-01, P3b-05, P0-A, DEC-035, PROJECT-REQ-001, P0.5, R6.1, G3a.
ID = (r"(?:[A-Z][A-Z0-9]*(?:[a-z](?=-))?(?:-[A-Z][A-Z0-9]*)*"
      r"-(?:\d+[a-z]?(?:\.\d+)*|[A-Z]+)|[A-Z]+\d+[a-z]?(?:\.\d+)*)")
END = r"(?![A-Za-z0-9_-])"
TOKEN = re.compile(r"(?<![A-Za-z0-9_-])" + ID + END)
ANCHOR = re.compile(r"(?P<id>" + ID + r")" + END)
GATE = re.compile(r"\*\*Gate\s+(?P<id>" + ID + r")(?=[.:*\s])")
INLINE_MILESTONE = re.compile(r"(?<![\w-])[A-Z]+\d+\.\d+(?![\w.-])")
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s{0,3}(\x60{3,}|~{3,})")
DECIMAL = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?|\.\d+"
NUMBER = re.compile(r"[+−-]?(?:" + DECIMAL + r")(?:[eE][+−-]?\d+)?%?|[⁺⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+")


def leading_id(line, is_heading):
    """Recognize definitions at structural starts, never arbitrary prose mentions."""
    stripped = line.lstrip()
    cell = stripped.startswith("|")
    lead = stripped.split("|", 2)[1].strip() if cell else stripped
    lead = re.sub(r"^(?:[-*+]|\d+\.)\s+", "", lead)
    marked = lead.startswith(("**", "__", "\x60"))
    lead = lead.lstrip("*_\x60")
    if lead.startswith("Gate "):
        lead = lead[5:]
    match = ANCHOR.match(lead)
    if not match:
        return None
    tail = lead[match.end():]
    if cell or is_heading or marked or re.match(r"^(?:[.:](?:\s|$)|\s+[—–-]\s)", tail):
        return match.group()
    return None


def scan(path):
    lines = Path(path).read_text(encoding="utf-8-sig").splitlines()
    blocks, mentions = {}, {}
    headings = []
    section = "Document"
    owner = "@ " + section
    current = None
    fence = None

    def select(key, force=False):
        nonlocal owner, current
        if key != owner or force:
            owner, current = key, None

    def emit(piece, lineno):
        nonlocal current
        if current is None:
            current = {"line": lineno, "lines": []}
            blocks.setdefault(owner, []).append(current)
        current["lines"].append(piece)

    for lineno, line in enumerate(lines, 1):
        marker = FENCE.match(line)
        if fence:
            emit(line, lineno)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not line[marker.end():].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            emit(line, lineno)
            continue
        for item in TOKEN.finditer(line):
            locations = mentions.setdefault(item.group(), [])
            if not locations or locations[-1] != lineno:
                locations.append(lineno)

        head = HEADING.match(line)
        label = head[2] if head else line
        key = leading_id(label, bool(head))
        if not key and not head:
            continuation = re.match(r"^(" + ID + r")\s+(?:includes|requires|costs)\b", line)
            if continuation and continuation[1] in blocks:
                key = continuation[1]
        if head:
            level = len(head[1])
            headings = [(n, h) for n, h in headings if n < level]
            headings.append((level, label))
            section = " / ".join(h for _, h in headings)
            select("@ " + section, True)
        if key:
            # R1 and S1 in dated change tables are different from global R-01.
            if headings and headings[-1][1].startswith("Changes in v"):
                key = headings[-1][1] + " / " + key
            select(key, True)
        # The phase summaries share lines with a gate or named release milestones.
        events = [(m.start(), m["id"]) for m in GATE.finditer(line)]
        if re.match(r"^\s*Milestones?\s*:", line, re.I):
            events.extend((m.start(), m.group()) for m in INLINE_MILESTONE.finditer(line))
        begin = 0
        for pos, new_key in sorted(events):
            if pos > begin:
                emit(line[begin:pos], lineno)
            if pos or new_key != key:
                select(new_key, True)
            begin = pos
        emit(line[begin:], lineno)
        if line.lstrip().startswith("|") and key:
            # A decision row ends at its last cell. Adding a later row must
            # not move unrelated prose into or out of an existing decision.
            select("@ " + section)

    records = {}
    for key, chunks in blocks.items():
        body = "\n\n".join("\n".join(c["lines"]).strip("\n") for c in chunks).strip("\n")
        if body:
            records[key] = {"text": body, "numbers": NUMBER.findall(body),
                            "lines": [c["line"] for c in chunks]}
    return records, mentions


def compare(old, new):
    changes = []
    for key in sorted(old.keys() | new.keys()):
        left, right = old.get(key), new.get(key)
        if left is None:
            status = "added"
        elif right is None:
            status = "removed"
        elif left["text"] != right["text"] or left["numbers"] != right["numbers"]:
            status = "changed"
        else:
            continue
        changes.append({"id": key, "status": status,
                        "numbers_changed": (left or {}).get("numbers") != (right or {}).get("numbers")})
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--json", action="store_true", help="include all definitions, numbers, locations and mentions")
    parser.add_argument("--check", action="store_true", help="exit 1 when changes exist (default success)")
    args = parser.parse_args()
    try:
        old, old_refs = scan(args.old)
        new, new_refs = scan(args.new)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read SDD: {exc}\n")
    changes = compare(old, new)
    if args.json:
        print(json.dumps({"old": old, "new": new, "old_mentions": old_refs,
                          "new_mentions": new_refs, "changes": changes}, indent=2, ensure_ascii=True))
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(errors="backslashreplace")
        print(", ".join(f"{sum(c['status'] == status for c in changes)} {status}"
                        for status in ("added", "removed", "changed")))
        for c in changes:
            key = c["id"]
            a, b = old.get(key, {}), new.get(key, {})
            print(f"\n{c['status'].upper()} {key}  lines {a.get('lines', [])} -> {b.get('lines', [])}")
            if c["numbers_changed"]:
                print("  numbers before:", " ".join(a.get("numbers", [])))
                print("  numbers after: ", " ".join(b.get("numbers", [])))
            for line in difflib.unified_diff(a.get("text", "").splitlines(), b.get("text", "").splitlines(),
                                             fromfile="before", tofile="after", n=1, lineterm=""):
                print(line)
    return int(args.check and bool(changes))


if __name__ == "__main__":
    sys.exit(main())
