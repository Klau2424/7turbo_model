# Spec-Driven Development (SDD) — Local learned collision operators for lattice Boltzmann simulation

Version 0.4, proposed for joint ratification on 18 November 2026. Authors: Clau and Partner (name: ___). Source audit: 20 October 2026. B1 started on 2026-10-20. No gate has passed. The numerical criteria and forecasts below are proposals.

### Changes in v0.4

| Request | Sections | Revision |
|---|---|---|
| v0.4-R1 | §§2–3, 6–7, 17–18 | Acoustic outlet, probe tests and DFG extension check. |
| v0.4-R2 | §§3, 7, 17–18 | One onset bracket per held-out geometry. |
| v0.4-R3 | §§2–3, 6–8, 17–18 | Deterministic cold-start pulse and replay contract. |
| v0.4-R4 | §§3, 8, 17–18 | Bounded lag only for reference qualification. |
| v0.4-R5 | §§2, 5–6, 8–10, 13, 15, 17–18 | Fixed TRT in classical comparisons and fusion. |
| v0.4-R6 | §§3, 5, 9–10, 17–18 | Project training spans one convective unit. |
| v0.4-R7 | §§3, 7–8, 17–18 | Gentler ramp, extrapolation cap, then lower speed. |
| v0.4-R8 | §§1, 11–15, 17–19 | 12 GB 3D target and direct D = 16 domain check. |
| v0.4-V1 | §§5–6, 8, 17–18 | Fused implementation effort and first-session toolchain tests. |
| v0.4-V2 | §§1, 5, 10, 12–13, 17–18 | G4 chooses the final branch. Classical 3D can start after G3. |
| v0.4-V3 | §§5–10, 12–13, 16, 18 | Learning milestones, review questions and ownership. |
| v0.4-V4 | §§5, 13, 18 | A shareable artifact about every four working weeks. |
| v0.4-V5 | §§5, 9, 15, 18 | Taylor–Green and silhouette sandboxes. |
| v0.4-V6 | §§1, 10, 18 | Pre-registered stress-versus-ghost hypotheses and inference. |
| v0.4-V7 | §§5, 10, 17–18 | Protected paired full-data arms, four widths and revised forecast. |
| v0.4-V8 | §§14–15, 18 | Four bounded engineering and research explorations. |
| v0.4-V9 | §§18, 20 | Four possible directions after this project. |
| v0.4-V10 | §§6, 8, 18 | Carry forward the post-v0.3 fused-classical-step edits in DEC-035. |
| v0.4-V11 | §§13, 18 | Track learning material and the SDD comparison script. |
| v0.4-V12 | §§1, 18 | Shared reading path before ratification. |

### Changes in v0.3

| Change | Affected sections / revision |
|---|---|
| S1 | §§3, 5–8, 17–18: cheaper classical pilots, representative reference qualification, measured-throughput budget and fixed reduction order. |
| S2 | §§3, 5, 7–10, 13, 17–18: shared training/validation/test families, separate triangle transfer, balanced counts and revised storage. |
| S3 | §§9, 13, 17–18: adoption must also match the best same-resolution classical method; disclose weak baseline coverage. |
| S4 | §§1, 12, 17–18: coarse Bhatnagar–Gross–Krook (BGK) divergence counts as nontrivial when regularized BGK (RBGK) and qualified references remain valid. |
| S5 | §§5, 10, 17–18: full-data scaling trains to plateau or 51,200 visits; smaller fractions are screening runs. |
| S6 | §§10, 17–18: bounded moment relaxation replaces the unconstrained scaling residual. |
| S7 | §§5, 9, 11, 13, 17–18, Appendix B: separate as-published and corrected source runs; B2 uses corrected weights. |
| S8 | Throughout: spacing, first-use definitions and readable multi-part rules; unchanged requirements retain their meaning. |
| S9 | §§3, 9–10, 18: the 96 Type C validation windows monitor training loss only. |
| S10 | §§8, 13, 18: measured same-resolution cost ratio and acoustic break-even ratio alongside every efficiency comparison. |

### Changes in v0.2

| Change | Affected sections / revision |
|---|---|
| R1 | §§1, 5, 8–9, 16–18: day-one Track B; B1 started, B2 early port, B3 sandbox. |
| R2 | §§5, 9, 18: remove exploration percentage cap. |
| R3 | §9, Appendix B, §§17–18: confirmed source recipe and leakage. |
| R4 | §§3, 9, 17–18: Type C full-field K=100 baseline and storage. |
| R5 | §§10, 17–18: stress-capable scaling instrument and compute curves. |
| R6 | §§2–3, 6–8, 13, 17–18: halfway openings, three rungs, independent finer reference. |
| R7 | §§3, 8, 17–18: wider training, interpolation headline, separate extrapolation. |
| R8 | §§2–3, 6–7, 18: specular project walls; retain German Research Foundation (DFG) benchmark boundaries. |
| R9 | §§3–4, 7–8, 17–18: classical-pilot Mach rule. |
| R10 | §§3, 7, 17–18: materially different shape families. |
| R11 | §§3, 7, 17–18: onset-qualified validation/test Reynolds numbers. |
| R12 | §§8, 13, 18: core/output timing, sampled diagnostics, batching. |
| R13 | §§9, 18: five-epoch checkpoint selection across validation restarts. |
| R14 | §§1, 12, 17–18: nontrivial 3D teaching signal or explicit plumbing outcome. |
| R15 | §§12, 17–18: classical sphere D=8/12/16 and cost. |
| R16 | §§2–3, 8, 18: remove inactive guards and their exclusions. |
| R17 | §§3, 18: lifting projection is a rounding guard. |
| R18 | §§8, 13, 18: timing retry limit. |
| R19 | §§16, 18, Appendix A: human pull-request (PR) sign-off rule. |
| R20 | §§16, 18: current issues replace weekly check-in. |
| R21 | §18, Appendix A: CLAUDE.md imports AGENTS.md. |
| R22 | §§1, 13, 18: public 2D tag after G4. |
| R23 | §§5, 15, 18: three first sandbox entries. |

## 1. Authority, goals and interpretation

**G-01. Fix the ruler, free the thing being measured.** The classical solver, boundaries, reference generation, dataset contract, evaluation cases, metrics and comparison protocol are the ruler. They are conventional numerical machinery, not the research contribution. The learned collision operator is the experimental object. This document does not select its final architecture, receptive field, training objective or conservation mechanism.

**G-02. Primary research question.** On obstacle flows, do local learned collision operators allowed to modify stress relaxation outperform, and scale differently from, ghost-only operators with stress fixed at `1/τ`? Lettuce and the 2025 invariant-network operator motivate the ghost-only control. H1 predicts lower validation velocity error for the stress-capable arm at matched parameter count. H2 predicts a power-law decline in its error across at least two decades in parameters. Freeze the P4-07 analysis before any P4 run, including pilots. Report both arms against fixed TRT. The broader engineering question remains whether a cheaper coarse solver can meet the accuracy, conservation and stability ruler. Negative findings are publishable project outcomes. [Invariant-network operator](https://doi.org/10.1103/rbf2-p8tf)

**G-03. Fixed scope.** Use Python and PyTorch with one codebase for the central processing unit (CPU) and NVIDIA's Compute Unified Device Architecture (CUDA). Default arithmetic is 32-bit floating point (FP32); 64-bit floating point (FP64) is the verification oracle. The lattice Boltzmann method (LBM) is dimension-generic: two dimensions and nine velocities (D2Q9) first, then three dimensions and nineteen velocities (D3Q19). Collision has a bounded spatial neighbourhood and algebraically conserves mass and momentum.

All two-dimensional (2D) training/inference must fit the GTX 1650's 4 gigabytes (GB); three-dimensional (3D) deployment must fit the RTX 2060's 12 GB. Graphics processing unit (GPU) configuration may differ, but CPU/GPU numerical implementations may not. Optional acceleration retains a tested portable path. Colab is optional burst capacity, never required for generation or a gate.

**G-04. Non-goals.** Adaptive mesh refinement, automated architecture search, production aerodynamics software, realistic road-car Reynolds numbers, compressible/high-Mach flow, turbulence certification, moving obstacles, thermal/multiphase flow, distributed training and multi-GPU requirements. A low-Re Ahmed body is an optional demonstration, not an automotive prediction. No publication or positive speedup is required.

**G-05. Definition of done.** A public MIT-licensed repository contains this sole specification, a concise README naming both authors and their contributions, reproducible configurations and scripts, verified classical gates, the replicated learned baseline, all attempted explorations including failures, and tables and plots of accuracy, stability, cost and generalization. R-06 after G4 already delivers the public 2D result. At G4 both developers record the final branch and its completion evidence under OD-24. Branch (a) completes Phase 5 including its qualified teaching signal or labelled plumbing outcome. Branch (b) completes an extended 2D exploration and growth cycle. Branch (c) completes the classical sphere ladder and the 3D Taylor–Green sandbox with classical-only claims. All branches require Phase 6. A negative learned result can satisfy completion. The applicable classical correctness gates must pass.

**G-06. Normative language.** MUST/shall is binding after ratification. Requirement IDs remain stable. Unlabelled thresholds, sample counts, budgets and effort estimates are **project design criteria**, not measurements or literature claims. Their rationale is stated locally; literature values have source links. `[VERIFY]` means unavailable evidence, not permission to guess. A dependent gate cannot pass until resolved by a jointly reviewed SDD pull request (PR). There are no invented results.

Notation used below: Reynolds number Re, Mach number Ma, Strouhal number St, drag coefficient CD and lift coefficient CL. Memory arithmetic uses binary kibibytes (KiB), mebibytes (MiB) and gibibytes (GiB): 2¹⁰, 2²⁰ and 2³⁰ bytes. Hardware names retain the manufacturers' GB labels.

**G-07. Recommendations versus decisions.** The complete proposed ruler below uses the recommended options in §17. Both humans must ratify them at the stated deadlines or replace them with equally complete alternatives here. Agents must not silently resolve choices or claim a dependent gate has passed. Track B is the explicit early-work exception: DEC-007 records B1's start; its experiments do not ratify the project ruler. Ratification concerns research implementation, not permission to write this SDD.

**G-08. One specification.** README explains use and results; configs instantiate parameters; structured result files are evidence; issues and PRs track work. None is a second specification. Architecture decisions, new ideas and scope changes belong here. Agent instruction files contain only the pointer and git rules in Appendix A. No separate architecture, experiment-plan or requirements documents are allowed.

**G-09. Start here.** Both developers read §§1, 5, 16 and 17 first. Clau then reads §§2–3, 6–7 and 12. Partner reads §§8–10 and 15. Divide the remaining sections and appendices between the two readers. Before ratification, record one human who understood each section in the ratifying PR.

## 2. Contracts first: ownership and architecture

| Component / repository location | Accountable owner | Responsibility and rationale |
|---|---|---|
| `src/lbm/lattices.py`, `units.py`, `state.py`, `solver.py`, `classical/` | Clau | Standard numerical core and classical operators; physics ownership stays together. |
| `src/lbm/boundaries/`, `geometry/`, `validation/` | Clau | Geometry, boundary ordering, force measurement and physical gates. |
| `src/data/`, generation configs | Clau, with joint contract approval | Implements deterministic generation; both approve schema, splits, restriction and parameter changes. |
| `src/models/`, `src/training/` | Partner | Operator adapters, training, checkpoints and memory measurements. |
| `src/evaluation/`, evaluation configs | Partner implements; jointly owned | Frozen metrics, timing and final reporting. Neither owner may move the ruler alone. |
| `src/experiments/`, scaling configs | Partner | Planned comparisons and reproducible sweeps. |
| `tests/`, `scripts/`, `.github/` | Owner of affected component | Other human reviews. Shared integration tests require both sign-offs. |
| `SDD.md`, `README.md`, release manifests | Both | Scope, decisions, exploration and truthful public claims. |

**A-01. Dependency direction.** Lattices/units → state/macros → classical collision and boundaries → solver → generation/evaluation. Models depend on contracts, not generator or harness internals. Training calls the same solver step as inference. Evaluation loads an operator through its registry and never branches on architecture names. The solver never reads training targets.

**A-02. Runtime conventions.** `d ∈ {2,3}`, `Q ∈ {9,19}`, `B` is batch size, `S=(Nx,Ny[,Nz])`. Tensors are channel-first `[B,C,*S]`; spatial axes are **x, y, z in that order**, even inside convolution libraries. `f` is `[B,Q,*S]`; vector channels are x, y, z. No implicit batch squeeze. All floating tensors use the selected device/dtype; lattice index tensors use int64 and masks use bool/uint8. Host-side configuration is immutable. An error names the incompatible field rather than copying silently between devices.

**A-03. State time.** `state.f` is always the pre-collision distribution at integer step `n`, after the previous streaming/boundary update. Outputs of collision are denoted `f_star`. A complete step advances `n→n+1`. Saved examples state this phase explicitly. Solid nodes are not evolved; their feature values are deterministically `feq(rho=1,u=0)` and masked from losses and fluid sums.

### 2.1 Public typed interface

These application programming interface (API) signatures and data contracts specify the implementation boundary. `Tensor` means `torch.Tensor`; `Mapping` entries and all shape symbols are specified below. Public functions are pure with respect to input tensors during differentiable execution.

```python
@dataclass(frozen=True)
class LatticeSpec:
    name: str
    dimension: int
    c: Tensor                 # int64 [Q,d]
    w: Tensor                 # float [Q]
    opposite: Tensor          # int64 [Q]
    cs2: float                # 1/3 for the supported lattices
    ordering_version: str

@dataclass(frozen=True)
class Units:
    dx: float                 # physical length per lattice spacing
    dt: float                 # physical time per lattice step
    rho0: float               # physical density represented by rho_lu=1
    length_unit: str
    time_unit: str

@dataclass(frozen=True)
class Geometry:
    cell_kind: Tensor          # uint8 [B,1,*S]: 0 fluid, 1 solid, 2 inlet-adjacent fluid, 3 outlet-adjacent fluid
    solid_id: Tensor | None    # optional dense int32 [B,1,*S]; otherwise tile provider
    sdf: Tensor | None         # optional dense [B,1,*S]; otherwise tile provider
    link_fraction: Tensor | None  # optional [B,Q,*S]; None for halfway walls
    geometry_hash: str

@dataclass(frozen=True)
class State:
    f: Tensor                 # [B,Q,*S]
    step: Tensor              # int64 [B], supports different patch start times
    memory: Mapping[str, Tensor]  # optional local learned state [B,Cm,*S]

@dataclass(frozen=True)
class Macros:
    rho: Tensor               # [B,1,*S], rho/rho0
    momentum: Tensor          # [B,d,*S], rho_lu*u_lu
    velocity: Tensor          # [B,d,*S], lattice lengths / lattice step

@dataclass(frozen=True)
class OperatorSpec:
    name: str
    version: str
    supported_lattices: tuple[str, ...]
    radius: int               # full Chebyshev receptive radius per call
    memory_channels: Mapping[str, int]
    required_features: tuple[str, ...]
    parameter_count: int

@dataclass(frozen=True)
class CollisionContext:
    lattice: LatticeSpec
    tau: Tensor               # [B,1,*S], tau > 0.5
    geometry_features: Mapping[str, Tensor]
    memory: Mapping[str, Tensor]
    step: Tensor              # int64 [B]

@dataclass(frozen=True)
class CollisionResult:
    delta_f: Tensor           # [B,Q,*S], collision increment, not f_star
    next_memory: Mapping[str, Tensor]

class CollisionOperator(Protocol):
    spec: OperatorSpec
    def __call__(self, f: Tensor, ctx: CollisionContext) -> CollisionResult: ...

def macroscopic(f: Tensor, lattice: LatticeSpec) -> Macros: ...
def physical_macroscopic(f: Tensor, context: StepContext) -> Macros: ...
def geometry_features(geometry: Geometry, bounds: tuple[slice, ...],
                      names: tuple[str, ...], halo: int) -> Mapping[str, Tensor]: ...
def equilibrium(rho: Tensor, velocity: Tensor, lattice: LatticeSpec) -> Tensor: ...
def initialize(config: CaseConfig, lattice: LatticeSpec,
               device: torch.device, dtype: torch.dtype) -> tuple[State, Geometry]: ...
def step(state: State, operator: CollisionOperator,
         context: StepContext) -> tuple[State, StepDiagnostics]: ...
def rollout(state: State, operator: CollisionOperator, context: StepContext,
            steps: int, observe_every: int, differentiable: bool) -> RolloutResult: ...
def restrict_reference(f_fine: Tensor, fine_geometry: Geometry,
                       pair: PairSpec) -> RestrictedState: ...
def lift_reference(reference: RestrictedState, pair: PairSpec) -> Tensor: ...
def load_dataset(manifest_path: Path, split: str,
                 required_features: tuple[str, ...]) -> Dataset: ...
def train(config: TrainConfig, dataset: Dataset) -> CheckpointManifest: ...
def evaluate(config: EvalConfig, checkpoint: Path | None) -> RunManifest: ...
```

**A-04. Remaining types.** `StepContext` contains immutable lattice, per-batch units, geometry, boundary plan, broadcast `tau`, optional force configuration and requested diagnostics. `StepDiagnostics` contains fluid mass/momentum before/after, boundary mass/momentum flux, wall impulse by body, source impulse, maxima of speed/density deviation, minimum population, invalid-state flags and operator conservation residuals. Reductions use FP64 accumulation, including for FP32 simulations. `RolloutResult` contains final state and only the requested snapshots/diagnostics; it never retains all graphs unless training requests them. `RestrictedState` contains `rho`, `momentum`, projected averaged fine non-equilibrium, fluid mask and synchronized time. `PairSpec` contains scale ratio, units at both levels, both taus, geometry policy and restriction/lifting IDs from §3. All configs reject unknown core keys; `extensions` is the explicit escape hatch. `macroscopic` always returns unforced kinetic moments; `physical_macroscopic` applies the force adapter's half-force correction and is the sole observable used by the forced-channel validation. Each batch item's time is its step times its own dt.

The exact remaining record fields are:

| Record | Fields, types and invariants |
|---|---|
| `StepContext` | `lattice:LatticeSpec`; `units:tuple[Units,...]` length B; `geometry:Geometry`; `boundaries:tuple[BoundaryPlan,...]` length B; `tau:Tensor[B,1,*S]` or broadcast view, float; `force:ForceSpec\|None`; `diagnostic_names:tuple[str,...]`. |
| `BoundaryPlan` | `faces:tuple[FaceSpec,...]` exactly 2 d faces; `geometry_factor:int≥1`; `version:str`. Opposite periodic faces must be paired. Every grid cell belongs to the physical domain; open-face tags denote adjacent evolved fluid, not on-site boundary planes. No dynamically selected boundary type. |
| `FaceSpec` | `axis:int` in `[0,d)`; `side:Literal["lo","hi"]`; `kind:Literal["periodic","halfway_wall","velocity","acoustic_outlet","specular"]`; `plane_coordinate:float` in physical length; `velocity_profile:Literal["none","uniform","parabolic"]`; `velocity:tuple[float,...]` length d in physical length/time; `density:float\|None` as rho/rho0; `ramp:Literal["none","sin2"]`; `ramp_duration:float` physical time. Parabolic profile is `4 Umax eta(1−eta)` across the channel height, eta from the declared wall coordinates. Sin² ramp is `sin²(pi t/(2 ramp_duration))` until its endpoint. `ambient_normal_profile` names the inlet reference profile and ramp used for the acoustic outlet. `pulse_id` is `transverse-v1` for D-07 cold starts and `none` elsewhere. Inapplicable fields are null/none or zero, never silently inferred. |
| `ForceSpec` | `kind:Literal["guo_bgk"]`; `density_lu:Tensor[B,d,*S]`, force density per lattice step, spatial broadcast permitted. `None` means exactly zero source. |
| `StepDiagnostics` | `step:Tensor[B]` int64; float64 `mass_before,mass_after,mass_flux:Tensor[B]`; `momentum_before,momentum_after,momentum_flux,source_impulse:Tensor[B,d]`; `wall_impulse:Tensor[B,Nbody,d]`; `max_speed,max_density_deviation,min_population,mass_collision_residual:Tensor[B]`; `momentum_collision_residual:Tensor[B,d]`; `invalid_flags:Mapping[str,Tensor[B]]` bool. Flux sign is positive **into fluid**; wall impulse is **on fluid**, opposite the reported body force. Totals are lattice-cell sums; convert with rho0, dx and dt for physical metrics. |
| `RolloutResult` | `final_state:State`; `steps:Tensor[T,B]` int64; `rho:Tensor[T,B,1,*S]\|None`; `momentum:Tensor[T,B,d,*S]\|None`; `diagnostics:tuple[StepDiagnostics,...]`; `failure_step:Tensor[B]` int64, −1 if capped without failure; `failure_reason:tuple[str\|None,...]` length B. T is requested retained observation count, not all steps. |
| `PairSpec` | `ratio:int≥1`; `coarse_units,fine_units:Units`; `tau_coarse,tau_fine:float`; `coarse_shape,fine_shape:tuple[int,...]`; `geometry_policy:Literal["shared-voxel-v1","periodic-v1"]`; `restriction_id:Literal["volume-rho-j-v1"]`; `lifting_id:Literal["lift-acoustic-projected-v1"]`; `base_step:int`; `geometry_hash:str`. Source replication uses a separately named audited pair variant, never this core ID with different semantics. |
| `RestrictedState` | `rho:Tensor[B,1,*S_c]`; `momentum:Tensor[B,d,*S_c]`; `neq_projected:Tensor[B,Q,*S_c]`; `fluid_mask:Tensor[B,1,*S_c]` bool; `coarse_step:Tensor[B]` int64. Population/moment units are coarse lattice units; `neq_projected` is P times the averaged fine non-equilibrium before multiplication by alpha. |

`Nbody` is the number of distinct measured solid objects plus a separate wall group; `body_id_order:tuple[str,...]` is fixed in the case config. Missing requested diagnostics or snapshots are errors; unrequested arrays are null. Invalid configuration raises `ValueError`; unsupported schema/features/lattice raise a named compatibility error; numerical failure returns the first failing step and reason, never a successful result with silent NaNs.

**A-05. Locality and freedom.** A model declares its entire receptive radius, including every convolution, derivative and recurrent-state update. A stack of two 3×3 convolutions has radius 2. Radius is a finite configuration constant independent of domain size. Per-cell recurrent memory is allowed if its spatial communication has a declared bound and initialization/reset is reproducible. No global pooling, spatial BatchNorm statistics, full-field attention, global Fourier mixing or hidden solver access may influence a collision. Channel-only normalization at each cell, fixed training-set normalization, bounded local attention, mixtures and scalar physical parameters are allowed. Global reductions in a **training loss or diagnostic** do not violate inference locality. Changing architecture or memory dimensions must not change solver/harness code.

**A-06. Feature whitelist.** Core input is local populations and tau. Optional names are `fluid_mask`, `sdf`, `wall_normal`, `wall_link_fraction`, `prescribed_boundary_velocity`, `force` and declared local memory. Units/normalization are in the model manifest. The signed-distance field (SDF) is measured in local lattice lengths and clipped to the model's declared feature radius; normals are local derivatives of that clipped field. Case IDs, target fields, geometry family labels, test-set statistics and fine-grid information are forbidden inference features. Adding an optional schema feature is not permission to expose forbidden information.

**A-07. Conservation.** With `C=[ones;c_x;c_y(;c_z)]`, every unforced fluid-cell call satisfies `C delta_f=0` algebraically. It is not a loss penalty. Mechanisms remain open: non-conserved moments, nullspace outputs or a projection such as `P=I−Cᵀ(CCᵀ)⁻¹C`. The latter is an example, not the required architecture. Measured normalized residual per cell must be ≤ `2e-6` in FP32 and ≤ `1e-12` in FP64 (§11). Floating-point arithmetic does not imply bitwise conservation. Any positivity limiter, gate, fallback or precision conversion is included in the conservation test and timing. No silent clipping or emergency BGK substitution is permitted. A specified fallback is part of an operator variant and its activation fraction is reported.

**A-08. Memory and tiling.** Full-grid and tiled inference must agree to FP32 relative Euclidean (L2) norm ≤ `1e-5`, with absolute ≤ `1e-6` for near-zero quantities. Tiles read an immutable old state including halos, then write separate new buffers; never update tiles in place on the portable or differentiable path. EXP-09 may assess an isolated classical/inference implementation only after demonstrating equivalent immutable-read semantics and parity. A K-step patch rollout needs halo `h=K(R+1)` around its scored interior for collision radius R plus one streaming link. Boundary geometry is part of that halo. Loss is computed only where the full domain of dependence exists. True physical-boundary patches apply the same boundary plan; artificial crop edges never receive invented wall or periodic conditions. Full small periodic grids are permitted for long unrolls where patch halos are wasteful.

Fresh trajectories and lifted training/evaluation restarts initialize every declared memory channel to zero, with the same device/dtype as f. Checkpoint resume restores memory exactly. The solver allocates memory from `OperatorSpec` before the first call; `initialize` may initially return an empty map. An exploration requiring learned memory initialization declares a local initializer and its radius in its entry/manifest and uses it identically at training and evaluation. No memory is carried across unrelated samples.

Static geometry descriptors, body-label rules and sparse wall links are retained by a deterministic tile provider. `geometry_features` returns dense arrays on exactly `bounds` expanded by `halo`, with the shapes/dtypes above, same device as the tile, using A-13 virtual padding outside the domain. `solid_id=-1` outside measured bodies; SDF is positive in fluid and negative in solid, zero on the represented surface. Missing dense fields mean compute from the descriptor, not omit required geometry. Halfway walls never allocate full link-fraction tensors; a requested wall link has fraction 0.5. Full-domain materialization is optional and included in measured memory. Classical sphere kernels can identify their one body from the solid mask/descriptor without dense per-cell IDs or SDF.

### 2.2 Classical equations, lattices and units

**A-09. Equilibrium and viscosity.** Use the standard isothermal second-order equilibrium

`feq_i = w_i rho [1 + (c_i·u)/cs² + (c_i·u)²/(2cs⁴) − (u·u)/(2cs²)]`,

`rho=sum_i f_i`, `j=sum_i c_i f_i`, `u=j/rho`, `p_lu=cs² rho`, `nu_lu=cs²(tau−1/2)`, and BGK `delta_f=−(f−feq)/tau`. The physical conversion is `u_phys=u_lu dx/dt`, `nu_phys=nu_lu dx²/dt`, `rho_phys=rho0 rho_lu`. Changing grid size must change tau/dt consistently, not accidentally change Re. Theory and parameter conversion: [Krüger et al., Chapters 3–4 and 7](https://link.springer.com/book/10.1007/978-3-319-44649-3).

**A-10. Lattice data.** D2Q9 ordering is `(0,0),(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)`, weights `4/9`, four `1/9`, four `1/36`. D3Q19 contains rest, six unit axes, twelve face diagonals; weights `1/3`, six `1/18`, twelve `1/36`. 3D ordering is rest first, then nonzero vectors sorted lexicographically by `(cx,cy,cz)`; `opposite` is derived from exact negation. `cs²=1/3`. Assert weight sum 1, first moment zero, second moment `cs² I`, fourth-order isotropy and opposite involution. These standard stencils are data; no core equation assumes Q=9 or d=2. [Book lattice definitions and implementation chapters](https://link.springer.com/book/10.1007/978-3-319-44649-3).

**A-11. Step ordering.** Compute collision on all fluid nodes, including open-face-adjacent nodes, from the old state; add any separately specified source; stream interior links and fill missing incoming populations through the A-12 boundary map; update diagnostics and step index. Each destination population has exactly one writer. Periodic wrap applies only to periodic axes. No population may wrap through an inlet/outlet or solid. Boundary kernels use lattice data and immutable old macros/post-collision populations.

**A-12. Boundaries — proposed ruler OD-01.** All nonperiodic faces are halfway between cell centres. Obstacles and no-slip walls use stationary bounce-back. D-07 transverse walls use specular free slip. Prescribe velocity at the inlet. At the outlet use a linear acoustic characteristic to supply the density in the link reconstruction. Let i be an outgoing direction, bar(i) its opposite and b the link midpoint.

`f_bar(i)(x,t+1)=f_star_i(x,t)−2 w_i rho_b (c_i·u_b)/cs²` at a velocity inlet, with prescribed `u_b(b,t+dt/2)` and `rho_b=rho(x,t)`;

At the outlet use `rho_b = 1 + (u_n − U_bg)/c_s` in lattice units. Here `u_n` is the old adjacent fluid velocity along the outward normal, and `U_bg` is the undisturbed ramped inlet normal speed at the corresponding transverse coordinate (DFG uses its parabolic profile). Set `u_b = u(x,t)` with the corner rule below. Fill only missing populations with `f_bar(i)(x,t+1) = −f_star_i(x,t) + feq_i(rho_b,u_b) + feq_bar(i)(rho_b,u_b)`. Use the negative squared-speed term in equilibrium. For virtual padding use the same face targets. Reject nonphysical density through the validity path. Stationary bounce-back uses the inlet formula at zero wall speed.

This closure sets the incoming linear acoustic invariant to its background value while allowing an outgoing pressure fluctuation. It adds no buffer cells or evolving boundary memory to a lifted restart. Oblique waves, vortices, mass drift and mixed corners still need testing. This is a project approximation inspired by characteristic LBM outlets. The cited paper does not validate this particular link rule. [Izquierdo and Fueyo](https://doi.org/10.1103/PhysRevE.78.046707) · [Halfway velocity bounce-back](https://cs10.gp.rrze.fau.de/pycodegen/lbmpy/sphinx/boundary_conditions.html#lbmpy.boundaries.boundaryconditions.UBB)

For a specular face, reflect only the normal velocity component and retain tangential travel: in a pull formulation, mirror the out-of-domain source index across that face and mirror the direction's normal component, then read that post-collision population. Reflect both components at two slip faces. For a link crossing an opening and a wall simultaneously, no-slip takes priority; with a slip wall the opening takes priority and its u_b has zero component normal to that wall. Apply this rule once, count that link only in the selected wall impulse or open flux, and never overwrite known streamed values. This mixed-corner closure is a project choice to validate, not a literature accuracy theorem. Reject intersecting open faces and obstacles touching openings.

**A-13. Boundary location.** At integer refinement s ≥ 1, centres are `(i+1/2)dx_base/s`, and box faces remain at 0 and L on every level. A base cell contains exactly `s^d` fine cells, including beside openings; common voxel faces also coincide. There are no inactive columns, corner rims or boundary scoring strips. Virtual padding for a model's stencil is computed on demand from the old state: periodic wrap, specular mirror, stationary-wall equilibrium at adjacent rho, or open-face equilibrium using A-12 face values. Geometry features use the same physical descriptors, with no invented solid outside an opening. Padding is never evolved, scored or counted in flux/force.

**A-14. Forcing scope.** Only the analytic channel gate requires forcing. Implement standard Guo forcing for BGK, including `rho u_phys-lu = sum(c_i f_i)+F/2`, with F the force density per lattice step. Keep the force-free collision API conservative; the BGK force adapter accounts for both the half-force equilibrium shift and the Guo source, and its total momentum increment must equal F. It must not pass shifted velocity into a supposedly conservative learned collision. Learned/coarse-grid experiments in this version are unforced; requesting Guo forcing with an unsupported operator is an explicit error. [Guo, Zheng & Shi, 2002](https://doi.org/10.1103/PhysRevE.65.046308).

**A-15. Stabilized baseline — proposed OD-04.** Implement regularized BGK (RBGK): form non-equilibrium stress `Pi_neq=sum_i (c_i c_i)(f_i−feq_i)`; reconstruct `fneq_reg_i=w_i (c_i c_i−cs²I):Pi_neq/(2cs⁴)`; output `feq+(1−1/tau)fneq_reg`. Use the same conserved moments and boundaries as BGK. This suppresses non-hydrodynamic content without a fitted stability parameter and generalizes to both stencils. Its superiority is measured, never assumed; it is a stabilized comparator, not proof against all multiple-relaxation-time (MRT) or Karlin–Bösch–Chikatamarla (KBC) methods. [Latt & Chopard, 2006](https://arxiv.org/abs/physics/0506157).

For two-relaxation-time collision (TRT), decompose `g_i = f_i − feq_i` into `g_i⁺ = (g_i + g_bar(i))/2` and `g_i⁻ = (g_i − g_bar(i))/2`. Return `delta_f_i = −g_i⁺/τ⁺ − g_i⁻/τ⁻`, where `τ⁺ = τ` and `(τ⁺ − ½)(τ⁻ − ½) = Λ = 3/16`. This conventional halfway bounce-back choice fixes the otherwise free odd rate and makes the straight-channel wall position viscosity-independent in the ideal Poiseuille analysis. It supplies a zero-trained-parameter control on the same lattice, viscosity, walls and starts. Check conservation, BGK recovery at equal rates, and absence of fitting. [TRT and boundary parametrization](https://doi.org/10.4208/cicp.2008.v3.p427) · [Halfway channel analysis](https://www10.cs.fau.de/publications/dissertations/Diss_2017-Bogner.pdf)

## 3. Dataset contract and reference definition

**D-01. Two different tasks.** Type A contains genuine local BGK pre/post-collision pairs. Type B (patches) and Type C (full 2D fields) contain lifted coarse starts and time-aligned restricted **macroscopic** fine-flow targets. Restriction and streaming generally do not commute; inverse-streaming a restricted future state can require a local change in conserved moments. B/C therefore train conservative rollouts against fields, never fabricated per-cell collision labels.

### 3.1 Resolution, geometry, restriction and lifting

**D-02. Acoustic scaling.** For integer ratio `r=dx_c/dx_f`, set `dt_c=r dt_f`, `u_lu,c=u_lu,f`, `nu_lu,f=r nu_lu,c`, and `tau_f=1/2+r(tau_c−1/2)`. Re, physical geometry/density and elapsed time agree. One coarse step corresponds to r fine steps. Project Type B/C and evaluation use reference factor 6 relative to base; candidates have factors 1, 2, 3, each dividing 6. Halfway boundaries nest at every integer factor; the periodic source replication separately uses factor 2. All observation times are base integer steps multiplied by level factor. This is a chosen observation operator, not exact kinetic coarse graining; non-equilibrium rescaling follows the leading-order [grid-coupling analysis](https://arxiv.org/abs/2004.14887).

**D-03. Shared geometry.** Repeat each base-mask cell r times per axis: every headline resolution shares the same stair-step surface. Fine grids improve flow resolution, not geometry. Analytic cylinder/sphere refinement is a separate study. Derive SDF/links from the represented surface; reject mixed solid/fluid blocks. Never average through walls or introduce implicit porosity. Cut-cell comparisons require a new ruler.

**D-04. Restriction.** For each coarse fluid cell and its `r^d` fluid children, `A(g)=sum(g)/r^d`. Set `rho_c=A(rho_f)`, `j_c=A(rho_f u_f)`, `u_c=j_c/rho_c`; store rho/j, never independently average velocity. This preserves volume-integrated mass/momentum in exact arithmetic. Only lifting requests non-equilibrium; no temporal smoothing. Hash coordinates and time alignment.

**D-05. Lifting to a coarse kinetic start.** Let `g=A(f_f−feq(rho_f,u_f))`, `alpha=r tau_c/tau_f`, and `P` be A-07's conserved-moment nullspace projection. Define `f_c^0=feq(rho_c,u_c)+alpha P g`, ID `lift-acoustic-projected-v1`. Each fine non-equilibrium has zero conserved moments, as does its average: P is mathematically a no-op up to rounding, retained only as a numerical guard. This leading-order initialization is not a unique exact coarse state. Reject nonpositive rho, nonfinite values or `min(f)<−1e-6`; never clip. Apply identical lifting to every method and pass D-13. For candidate factor s use ratio 6/s and its own tau. Zero-non-equilibrium lifting is a named ablation.

**D-06. Reference qualification.** Evaluation uses BGK at factor `r = 6` (96 cells per D), strictly finer than every candidate. Qualification compares it with `r = 9` (144 cells per D), restricting both independently to the base grid.

- Use the full E-03 schedule, including on sparsely retained side cases. For D-06 alone compare r = 6 at t with r = 9 at t + δ. For each resolved-periodic observation window choose one integer lag on the 0.2-unit observation grid from −1 to +1 convective unit inclusive to minimize the full-fluid E-02 spacetime error. Use the same lag for all cells, channels and times. Break ties by smallest |δ|, then smaller signed δ. Steady windows use zero lag. Require matching E-04 regimes on the two grids. Keep every endpoint: stream the finer fields with one unit of padding at both ends, including through t* = 201. Record raw and minimized errors and δ for each of [50,70], [100,120], [150,170] and [100,200]. Require each minimized velocity error ≤ 1%. Mean drag ≤ 2% difference and St ≤ 1% difference when defined use the original unshifted clocks and E-04 classification. Unresolved references still block qualification. Candidate E-02, E-03 and E-09 scores always use δ = 0.
- Qualify the highest-Re case in each family within each split. Among equal-Re instances choose maximum frontal blockage, then smallest resolved corner radius, then geometry hash. The default counts are 3 training + 3 validation + 3 main-test + 1 transfer + 3 extrapolation representatives = **13**.
- Add one mid-Re spot check in each held-out split: validation, main test, transfer and extrapolation. Choose the unqualified case nearest that split's Re-range midpoint, breaking ties by lower Re and then geometry hash. This gives **17 distinct r = 9 runs**.
- If any comparison fails, qualify **every case in that family and split**, retaining the failed row. Budget the expansion before continuing. At worst all 82 default cases need qualification; never weaken the thresholds or substitute an easier case.
- Every production reference still receives per-case validity and Mach checks. Label cases as directly qualified or covered by representative qualification. The expectation that error usually increases with Re motivates this sampling; it is an empirical assumption, not a bound on every geometry.

The classical comparator can **never be the reference run itself**. A changed reference factor must exceed 3 and be divisible by 1, 2 and 3; it requires a joint ruler revision. Classical-only qualification exposes no candidate-model scores.

### 3.2 Deterministic populations of cases

**D-07. Shape generator.** Use the following common physical setup:

- Box `24D × 8D`, obstacle centre `(6D, 4D)`, A-13 face locations, specular/free-slip horizontal walls and a no-slip obstacle.
- Uniform axial inlet at `U_lu = 0.03` initially proposed. From rest prescribe `u_x = U sin²(π min(t*/T,1)/2)`, where `t* = tU/D` and P1-A first tests `T = 20`. Freeze U, T and the boundary version before production.
- During cold starts only, add `u_y/U = 10⁻⁴ sin(2πq) sin²(πq)` for `q = (t* − 2)/2` in (0,1), zero otherwise. Evaluate both inlet components at the link half-time. The smooth two-lobed pulse has zero time integral and peak magnitude (3√3/8) × 10⁻⁴ U ≈ 6.50 × 10⁻⁵ U. It ends at t* = 4, well before any scored window. Apply exactly the same trace to references at all factors, candidates, classical baselines and pilots. It seeds an antisymmetric wake without sustained transverse forcing. Record the actual inlet trace and hash. Restart mode resumes the physical clock without replaying the pulse. DFG and source-reproduction fixtures keep their own starts.
- D is twice the maximum continuous radius. Candidate diameters 16/32/48 give grids 384×128, 768×256 and 1152×384. The reference grid is 2304×768; qualification uses 3456×1152.
- DFG retains its separate no-slip walls and parabolic inlet.

Training, validation and the main test each contain these same three families, with different instances:

| Family | Generator and resolved features |
|---|---|
| Lobed harmonics | `r(theta) = r0[1 + a cos(k theta + phi)]`, with `a ∼ Uniform[0.20, 0.35]`, `phi ∼ Uniform[0, 2pi)` and k = 2 or 3. Include both k values in every split; they are subtypes of one family. |
| Ellipses | Aspect ratio sampled in [1, 2.5], rotation in [0, pi). Reject near-circular instances whose distinguishing feature is unresolved. |
| Rounded squares | Superellipse `\|x/a\|^p + \|y/a\|^p = 1`, with p sampled in [12, 20] and rotation in [0, pi/2). |

The separate transfer family is **rounded equilateral triangles**. In base-cell units, take a centred equilateral triangle of circumradius `8 − r_corner`, add a disk of radius `r_corner ∈ [1, 1.5]`, and rotate uniformly in [0, 2 pi/3). The resulting circumradius is 8, and corner radius is at least one base cell. Three straight sides and rounded corners distinguish it from sinusoidal lobes and four-sided shapes; its radial excursion is `4 − r_corner/2 = 3.25–3.5` base cells.

Normalize the other families to maximum radius D/2 and rasterize at cell centres, counting equality as solid. Require the distinguishing feature and its rasterized extent to span at least two base cells. Harmonic excursion is `16a/(1+a) = 2.67–4.15` cells. Reject unresolved features, disconnected solids, enclosed fluid pockets and duplicate masks. These finite families do not represent arbitrary aerodynamics.

**D-08. Splits.** Use NumPy's permuted congruential generator with 64-bit output (PCG64) with geometry seeds 1101/2202/3303/3304 for training/validation/main test/transfer. The D-07 pulse is analytic and uses no RNG. Preserve seed 4404 plus case index for separately tagged stochastic augmentation only. Use window selection seed 5505 and model seeds 11/22/33. Pin library and generator versions. Within each split, assign harmonic orders by shape-ID order: training uses {2, 3, 2}; validation and main test each use {2, 3}. Draw continuous geometry parameters uniformly over their declared intervals, rejecting invalid instances until the fixed count is reached.

| Split | Shapes and Reynolds numbers | Cases | Role |
|---|---|---:|---|
| Training | 3 instances × 3 families × Re {20, 60, 100, 160} | 36 | Balanced family and Re coverage. |
| Validation | 2 new instances × 3 families × nominal Re {30, 140} | 12 | Checkpoint and model selection. |
| Main test | 2 new instances × 3 families × nominal Re {40, 80, 120} | 18 | In-distribution family coverage and Re interpolation; headline denominator. |
| Family transfer | 2 rounded triangles × nominal Re {80, 120} | 4 | Geometric transfer, outside the headline. |
| Re extrapolation | All 6 main-test shapes × Re {200, 240}, or {180, 200} on P1-A’s capped branch | 12 | Re transfer, outside the headline. |
| Total | 36 training + 46 evaluation | **82** | No side-row pooling into the headline. |

- Training, validation, main-test and transfer instances are disjoint. Only extrapolation reuses main-test geometry, with different case IDs. All descendants of a case retain its split; source periodic data stays separate.
- Bracket each of the 14 distinct held-out shape instances under P1-B. For its own verified [a,b], require `Re ≤ 0.8a` or `Re ≥ 1.2b`. Assign validation first, then main test. Visit shapes by ID, nominal levels in ascending order. Choose the nearest eligible integer in (20,160), excluding all original training levels, earlier levels for this shape, and (for main test) every validation level used in its family. Break ties by lower Re. Levels may repeat across shapes in the same split.
- Apply the same onset-margin rule to triangle transfer, but allow its interpolated Re values to match the main test. Extrapolation must also clear onset. Recheck every retained case and freeze assignments before learned evaluation; insufficient eligible levels or unresolved classifications require a joint revision, never case deletion.
- P1-C may reduce training to 2 instances per family (24 cases), then to Re {20, 160} (12 cases). Freeze the chosen cohort before generation and fitting. All 46 evaluation cases remain; interpolation still lies inside the training range.

At U = 0.03, `tau_base = 0.5 + 3UD/Re = 0.5 + 1.44/Re`. Training taus are 0.572, 0.524, 0.5144 and 0.509; nominal main-test taus are 0.536, 0.518 and 0.512. Extrapolation gives 0.5072 and 0.506. At r = 6, training taus are 0.932, 0.644, 0.5864 and 0.554; extrapolation gives 0.5432 and 0.536. Distance from 0.5 is not a stability proof: validity and representative convergence must be demonstrated.

On the capped branch, Re 180 and 200 give base `τ = 0.508, 0.5072` and r = 6 `τ = 0.548, 0.5432` at U = 0.03. At another U, multiply every listed excess above 0.5 by U/0.03. Check margins at both assigned extrapolation values.

**D-09. Trajectory sampling.**

- Run to `t* = 200`. At U = 0.03, the base stop is `ceil(200 × 16 / 0.03) = 106,667` steps. Factors 1/2/3/6/9 take 106,667/213,334/320,001/640,002/960,003 steps. Save forces every step.
- For the **30 validation/main-test cases**, retain base-restricted rho/j at `Δt* = 0.2` in [50, 70], [100,120], [150,170] and [100,200]. Deduplication leaves `101 + 501 = 602` frames per case.
- For the **16 transfer/extrapolation cases**, retain the same intervals at `Δt* = 2`: `11 + 51 = 62` frames. Label their velocity metrics as sparse-cadence diagnostics. They never enter headline qualification or checkpoint/adoption selection. Forces, horizons and failure diagnostics keep their full cadence.
- One frame is `3 × 4 × 49,152 = 589,824 bytes = 0.5625 MiB`. Main/validation fields use `30 × 602 × 0.5625 / 1024 = 9.920654 GiB`; side fields use `16 × 62 × 0.5625 / 1024 = 0.544922 GiB`.
- Keep three r = 6 kinetic restarts for each of the 46 evaluation cases. Each uses `9 × 4 × 49,152 × 6² = 60.75 MiB`; total `46 × 3 × 60.75 / 1024 = 8.187012 GiB`. Restrict them to each candidate rung. Stream other fine distributions; use temporary full-cadence fields for D-06 qualification, then discard them after verification.

**D-14. Full-field 2D windows (Type C).**

- Select 32 starts per training case and 8 per validation case, uniformly without replacement, using seed 5505. Starts lie in `t* ∈ [50,180]` and leave room for K steps before the trajectory stop. Never sample test or transfer cases.
- Store one lifted `f0[9,384,128]` and ten restricted rho/j targets at relative integer steps `ceil(j K/10)`, j = 1,…,10. Choose `K = ceil(16/U_lu)` base steps for every P3b/P4 visit: 534, 640 or 800 at U = 0.03, 0.025 or 0.02. At 0.03 these are steps 54, 107, 161, 214, 267, 321, 374, 428, 481 and 534. Geometry is shared per case.
- Default counts are `36 × 32 = 1,152` training windows and `12 × 8 = 96` validation windows, total **1,248**. The training reductions give 768 or 384 training windows; the 96 validation windows stay fixed.
- A start uses `9 × 4 × 49,152 = 1.6875 MiB`; a window uses `1.6875 + 10 × 0.5625 = 7.3125 MiB`. Default payload is `1,248 × 7.3125 / 1024 = 8.912109 GiB`, comprising 8.226563 GiB training and 0.685547 GiB validation.
- The **96 validation windows monitor training loss only**. They do not select checkpoints, determine plateau stopping, support adoption or choose hyperparameters. Selection uses E-03 restarts across all 12 validation cases.
- K = 534 spans 1.00125 convective units. K = 100 is the historical B1/B2 fidelity horizon. Sparse supervision keeps the Type C byte count independent of K, while backpropagation and checkpoint costs grow with K.

Type B remains the 3D default and an optional 2D exploration corpus. For 2D use interior 8×8, K = 8, R ≤ 1, halo 16 and initial side 40. If requested, `256 × 36 + 64 × 12 = 9,984` samples split equally between wake and uniformly eligible fluid centres, with probabilities recorded. Larger R/K needs compatible shards: K = 534 at R = 0 would require a (8 + 2 × 534)² = 1,076² patch, taller than the channel. Full-field loss is unweighted over fluid; vorticity uses valid neighbours and boundary masks.

Type A stores 6,144 local pairs per training case and 2,048 per validation case: `36 × 6,144 + 12 × 2,048 = 245,760` pairs by default. Training reductions yield 172,032 or 98,304 total pairs. Preserve wall/wake/interior stratification and verify labels using stored tau/equilibrium conventions. Synthetic stress perturbations remain separately tagged, projected and positivity-checked.

### 3.3 Storage and schema — proposed OD-02/OD-03

**D-10. Format.** Use immutable Hierarchical Data Format version 5 (HDF5) shards ≤ 512 MiB and a JavaScript Object Notation (JSON) manifest. Use lossless gzip level 1 with shuffle, and sample chunks targeting 1–4 MiB. Each worker opens read-only; one writer flushes, closes and verifies a temporary shard before atomic rename. No concurrent append readers, shared mutable files or pickle records. This supports typed random reads without a server. [h5py documentation](https://docs.h5py.org/en/stable/high/dataset.html).

Manifest core fields (all required unless marked optional):

| Key | Type / meaning |
|---|---|
| `schema_version`, `generator_version` | Semantic Versioning (SemVer) strings; v0.3 core is `1.0.0`. The changed required face and target-time semantics use `2.0.0` with a new dataset/ruler hash. |
| `dataset_id`, `dataset_sha256`, `created_utc` | Dataset ID is a 256-bit Secure Hash Algorithm (SHA256) digest of canonical generator commit + resolved config + lattice/schema/split IDs, excluding paths/timestamps. Manifest-content hash excludes only its own hash. Creation time follows the International Organization for Standardization (ISO) 8601 date/time standard in Coordinated Universal Time (UTC). |
| `sdd_git_commit`, `generator_git_commit`, `dirty` | Full commit-hash strings; `dirty=false` for usable research data. |
| `config`, `config_sha256`, `environment` | Embedded canonical config, SHA256, Python/PyTorch/NumPy/h5py/CUDA versions. |
| `seeds`, `split_manifest_sha256` | Named uint64 seeds and hash of immutable case assignments. |
| `lattice` | name, d, Q, c, w, opposite, cs², ordering version. |
| `pair_spec` | r, dx/dt/rho0 at both levels, taus, geometry policy, restriction/lift IDs; null for Type A. |
| `cases` | List of case_id, split, family, geometry hash/parameters, Re, D, U, units, grid sizes, boundaries, run validity and reference qualification. |
| `shards` | Relative path, SHA256, sample count, kind, array schema, uncompressed/stored bytes and case IDs. |
| `features` | Present optional feature names with dtype, shape, units, normalization and semantic version. |
| `extensions` | Namespaced JSON object; unknown entries ignored unless listed in `required_features`. |

Shard arrays use little-endian storage. N means shard samples, P means initial patch side, I means scored interior, and T=K+1. Sample arrays align by their first index:

| Array | Dtype and shape | Semantics |
|---|---|---|
| `sample_id`, `case_index`, `coarse_step` | uint64[N], int32[N], int64[N] | Stable identity, manifest case lookup, pre-collision start. |
| `origin` | int32[N, d] | Initial patch lower corner in coarse coordinates, including periodic wrap convention. |
| `sampling_probability` | float64[N] | Selection probability, `(0,1]`. |
| `tau` | float32[N,1] | Constant per sample in this dataset; broadcast spatially. |
| `a/f_pre`, `a/f_post` | float32[N, Q] | Type A only; unforced collision before streaming/boundaries. |
| `b/f0` | float32[N, Q, P,..., P] | Type B only; lifted state including causal halo. |
| `b/rho_target` | float32[N, T, 1, I,..., I] | Restricted reference at aligned target times including t=0. |
| `b/j_target` | float32[N, T, d, I,..., I] | Restricted momentum; velocity is derived. |
| `b/target_steps` | int64[N, T] | Consecutive coarse steps for default K=8; fine steps equal r times these relative to synchronized origin. |
| `b/cell_kind`, `b/sdf`, `b/solid_id` | uint8 / float32 / int32 [N, 1, P,..., P] | Same geometry semantics as runtime; complete halo. |
| `b/link_fraction` | float32[N, Q, P,..., P], optional | Needed only by a declared interpolated-boundary extension. |
| `b/score_mask` | bool[N, T, 1, I,..., I] | Excludes solids and derivative-invalid neighbours, never arbitrary difficult cells. |
| `b/crop` | int32[N, 2 d] | Interior start/stop indices in the initial patch. |
| `c/f0` | float32[N, 9,384,128] | Type C lifted full base state, pre-collision. |
| `c/rho_target`, `c/j_target` | float32[N, 10, 1,384,128] / float32[N, 10, 2,384,128] | Restricted targets at the ten D-14 offsets ceil(j K/10). |
| `c/target_steps`, `c/geometry_id` | int64[N,10], fixed SHA256[N] | Absolute coarse indices; geometry arrays referenced once per case, same runtime semantics. |
| `ext/<namespace>/<name>` | Declared typed array | Optional extra fields, e.g. local stress targets; never modifies core meanings. |

Common IDs/tau apply to all kinds; origin/probability apply to B and probability to C, with C origin implicitly zero. For C validate complete geometry/boundary plan instead of crop/halo. All required floats are finite; NaN is allowed only for absent wall fractions. Reference shards contain step/time, rho/j, body force, geometry hash and units; full fields exist only at budgeted observation times. Type C is a new kind; changed boundary/split/reference semantics create a new dataset ID, never relabel an old shard.

**D-11. Evolution.** Minor versions add optional fields with documented defaults; old readers ignore them. Major versions change meaning, units, required fields, ordering, restriction or lifting. Consumers declare supported major version and required features; missing requirements fail loudly. Appending a new model-required feature in `extensions` does not require rewriting unrelated contracts; changing the ruler does. Converters create a new dataset ID and preserve the parent hash. Never mutate published shards.

**D-12. Storage and compute budget.** All byte estimates are uncompressed; compression is not needed to meet the cap.

| Allocation per machine | Default payload and arithmetic | Limit |
|---|---|---:|
| 2D Type A/B/C | C: 8.912109 GiB; geometry for 48 training/validation cases: `48 × 9 × 49,152 / 2³⁰ = 0.019775 GiB`; optional B: `9,984 × 80 KiB < 0.761719 GiB`; A: `245,760 × 18 × 4 / 2³⁰ = 0.016479 GiB`. Sum < 9.7101 GiB before metadata. | 10 GiB |
| References/forces | 2D fields and restarts use 18.652588 GiB. Save the 32-byte force record for every step, including initialization, on all production cases. At 0.03, `82 × 640,003 × 32 / 2³⁰ = 1.564033 GiB`. Total 20.216621 GiB plus at most 2 GiB for 3D. | 24 GiB |
| 3D patches | P5-04 payload and metadata. | 4 GiB |
| Metadata/margin | Remaining working-dataset allowance. | 2 GiB |
| **Working total** | No main-test field or case trimming. | **40 GiB** |

- Checkpoints have a separate 5 GiB cap; rolling intermediates are limited to 10 GiB.
- An optional Type B sample uses 57,600 bytes for f0, 6,912 for targets and 14,400 for geometry. Masks and metadata bring it below 80 KiB.
- Reference grids at r = 6 and 9 have 1,769,472 and 3,981,312 cells. Three FP32 population buffers with Q = 9 use 0.177979 and 0.400452 GiB before scratch. Actual 2D process peak must remain ≤ 3.5 GiB.

For compute, define `W = 49,152 × ceil(200 × 16 / U_lu)` base cell updates per trajectory and `M_s` as measured throughput in million lattice updates per second (MLUPS) at factor s. At U = 0.03, `W = 5,242,896,384`. One factor-s trajectory costs `W s³ / (3.6 × 10⁹ M_s)` hours. Forecast these **additive** terms before production:

| Accepted branch | Production, 82 runs / M6 | Qualification, 17 padded runs / M9 | Cumulative Mach pilots / M3 | Onset at 3 / M3 | Endpoints at 6 / M6 | Total loop hours if all rates are 300 MLUPS |
|---|---:|---:|---:|---:|---:|---:|
| U = 0.03, Re up to 240 | 25,795.05 | 18,138.86 | 314.57 | 3,853.53–11,560.55 | 8,808.07–26,424.12 | 189.70–274.11 |
| U = 0.03, Re up to 200 | 25,795.05 | 18,138.86 | 629.15 | 3,853.53–11,560.55 | 8,808.07–26,424.12 | 190.75–275.16 |
| U = 0.025, Re up to 200 | 30,953.96 | 21,766.63 | 1,006.63 | 4,624.22–13,872.66 | 10,569.65–31,708.94 | 229.74–331.03 |
| U = 0.02, Re up to 200 | 38,692.45 | 27,208.29 | 1,478.49 | 5,780.28–17,340.83 | 13,212.06–39,636.17 | 287.91–414.52 |

Each coefficient is `runs × 49,152 × s³ × ceil(16T/U) / (3.6 × 10⁹)`. Divide by the measured MLUPS of that device at that factor and speed. Mach totals assume eight cases at each attempted branch. Onset uses 98 and 28 runs at T = 200–600, before repairs. Qualifications use T = 201 for fresh r = 9 runs. Capture full-cadence r = 6 qualification fields during production and stream comparison and lag sums case by case. Charge any replay explicitly, including when a failed representative triggers expansion.

At equal 150 MLUPS double the last column. At equal 300 MLUPS the ideal balanced load on each machine after 25% reserve is 118.56–171.32, 119.22–171.97, 143.59–206.89 or 179.94–259.08 hours respectively, before I/O or repairs. Dispatch discrete jobs using P1-C. Some branches exceed the 168-hour cap even in this illustration. Rates are assumptions, never benchmark results.

The fixed training reductions change only generation: 24 training + 46 evaluation = 70 runs cost `22,020.1648/M6`; 12 + 46 = 58 cost `18,245.2794/M6`. Qualification remains 17 runs unless failures expand it. Record which reductions fired, their reduced storage, the frozen cohort and forecasts.

For those reductions, Type C payload becomes `(768 + 96) × 7.3125 / 1024 = 6.169922 GiB` or `(384 + 96) × 7.3125 / 1024 = 3.427734 GiB`. Optional Type B counts become 6,912 or 3,840, and Type A totals become 172,032 or 98,304. The 46 evaluation cases retain 19.529972 GiB at U = 0.03. With all production force traces the reduced totals are 19.987738 and 19.758855 GiB. At U = 0.025 or 0.02 the default total is 18.652588 + 1.876833 or 2.346041 = 20.529421 or 20.998629 GiB. Size staging one case at a time within the separate 10 GiB cap. Corpus reductions change the data-size label, not the physical ruler or held-out denominators.

Account for contingencies explicitly:

- Endpoint disagreement adds r = 6 bracket repairs under P1-B.
- A default qualification expansion adds up to 65 r = 9 runs. At U = 0.03 this adds `65 × 49,152 × 9³ × 107,200 / (3.6 × 10⁹ M9) = 69,354.4550/M9` hours before any r = 6 replay.
- The Mach column includes all earlier attempts. If pilot throughput varies with speed, sum each attempt at its own measured rate. Count any exact reuse only once.
- Lowering U changes every production stop count and tau. Regenerate the table using the exact ceiling for the accepted U.
- A production reference above Ma 0.09 requires a recorded joint decision, not automatic global regeneration.

Unmeasured throughput, input/output (I/O) overhead and contingency counts remain `[VERIFY]`.

**D-13. Contract tests.** Require bitwise storage round-trips, corrupt-shard rejection and reproducible IDs/shapes from clean pinned inputs. Restriction mass/momentum tolerance is `1e-6` FP32/`1e-12` FP64; lifting uses A-07. Full/patch rollouts obey A-08; CPU/CUDA loaders have identical IDs/order. Train/validation/test geometry and case hashes are disjoint; only the declared test/extrapolation geometry reuse is permitted, with distinct case IDs.

## 4. Glossary for reviewers

| Term | Meaning in this project |
|---|---|
| Distribution / population `f_i` | A per-cell scalar for one discrete particle-velocity direction; Q channels jointly encode density, momentum and additional kinetic information. It is not a velocity component or a probability constrained to sum to one. |
| D2Q9 / D3Q19 | Two/three spatial dimensions with nine/nineteen populations per cell. |
| Equilibrium `feq` | Standard low-Mach distribution computed from local density and velocity; collision relaxes non-equilibrium content toward it. |
| Collision | Local update of populations before transport; must preserve cell mass and momentum without external force. |
| Streaming | Deterministic movement of each population by its lattice direction each step. It moves conserved quantities between cells. |
| BGK / tau | Single-relaxation-time collision; tau determines kinematic viscosity through `nu_lu=cs²(tau−1/2)`. Small positive viscosity puts tau near 1/2, often challenging stability. |
| RBGK / MRT | Regularized BGK removes unsupported kinetic content; multiple-relaxation-time collision controls different moments separately. |
| Moment | A weighted sum of populations, e.g. mass, momentum or stress. Non-conserved moments may change during collision. |
| Lattice units | Grid spacing and timestep are each one inside the update; physical conversion still exists and changes with resolution. |
| Reynolds number | `Re=UD/nu`, ratio of inertial to viscous effects; D and U must be stated for each case. |
| Strouhal number | `St=f_s D/U`, dimensionless shedding frequency; undefined if no resolved periodic shedding exists. |
| Mach constraint | `Ma=\|u_lu\|/sqrt(cs²)`. P1 freezes the matching cap and U using classical pilots (E-09); 0.15 remains the hard accuracy-regime limit. These project thresholds are not universal stability guarantees. |
| Restriction / lifting | Fine-to-coarse observation of fields / construction of kinetic populations from coarse observations. Neither is automatically a correct coarse collision. |
| MLUPS | Million lattice updates per second; its denominator and whether solid cells are counted must be declared. It alone cannot compare different resolutions at matched physical time. |
| Stable / accurate | A finite bounded rollout can be stable while wrong. Both criteria must be measured separately. |

Concept background: [Krüger et al., hydrodynamics, LBM, boundaries, parameter selection and implementation](https://link.springer.com/book/10.1007/978-3-319-44649-3).

## 5. Phase order, workload and gates

**P-01. Dependency graph.** Project evidence: P0→P1→P2→P3a→project 3b→G3. Parallel Track B: historical-source B1 started 2026-10-20; B2 follows periodic P0.2 checks; B3 explores before G3 without project holdouts/evidence claims. G3 consumes B1/B2 fidelity records. After G3, P3c, reporting and classical P5-01/P5-02 may overlap P4. At G4, record OD-24 and publish R-06. Final G6 requires G4 and the recorded branch’s G5 evidence. These exceptions replace the serial-only prohibition; other prerequisites remain.

**P-02. Effort.** Clau plans 8–10 hours/week; Partner 6–8, with explicit reduced capacity during exams. Estimates below are human working hours, including reading, reviewing, debugging and evidence capture; unattended computation is separate. Split a milestone exceeding 10 owner-hours into issues of 3–8 hours. At most one implementation issue per person plus one shared review is in progress. Each exploration is capped at 12–16 owner-hours over at most two normal working weeks; pause its clock during an agreed exam pause.

| Phase | Clau hours | Partner hours | Approximate elapsed working weeks | Reason for range |
|---|---:|---:|---:|---|
| 0 plus B1/B2/SBX-01 | 67–117 | 41–74 | 7–15 | Clau P0.0–0.5 = 52–90, acoustic/pulse tests 4–8, source review 4–6, L-01/L-02 7–13. Partner’s 34–60 includes core/Track B, plus acoustic review 2–4 and L-02/L-03 5–10. |
| 1 plus SBX-02–05 | 36–64 | 22–44 | 4–8 | Clau 31–52 core + 3–6 shape/Mach audit + 2–6 SBX-05. Partner 18–34 including SBX-02/03 + 2–4 qualification review + 2–6 SBX-04. |
| 2 | 10–18 | 30–48 | 4–8 | Clau 2–4 parity review + 4–6 freeze + 4–8 fixture/timing review. Partner’s former 28–44 plus 2–4 for TRT matrix coverage. |
| 3a/project 3b | 10–17 | 27–45 | 4–8 | Previous 9–15 / 24–39 plus 1–2 / 3–6 for long-window checks and profiling. |
| 4 | 12–22 | 38–66 | 5–11 | 10–18 / 32–54 plus 2–4 / 6–12 for matched arms, inference and G4 scope review. |
| 5, branch (a) | 40–65 | 19–31 | 4–9 | 38–61 / 18–29 plus 2–4 / 1–2 for the D = 16 expanded-domain and deployment checks. |
| 6 | 12–22 | 12–22 | 2–4 | Includes 2–4 each for R-06. |

During P0, budget 4–6 Partner-hours/week for Track B within 6–8 total; reserve 20% for review/reading. B1a/B1b require 14–24 hours. At 4–6 Track B hours per week, this is roughly 3–6 active weeks; adding the first 4–8-hour sandbox gives roughly 3–8 weeks in total, excluding computation waits. B3 may begin as soon as B1b supplies its finite fixture. Spare P1 capacity may fund further 4–8 h entries. P3c has no percentage cap; time boxes, X-03 and fortnightly review control scope. Zero adopted ideas is acceptable.

For branch (a), sum the seven rows: Clau 187–325 hours, Partner 189–330, combined **376–655 human-hours**. The original P0 Clau milestone minimum was 4 + 6 + 10 + 8 + 10 + 6 = 44 hours. The v0.3 ledger used 45. Moving implementation to P0.5 and charging it once corrects the ledger. The table includes five initial sandboxes, learning, PR explanations and release. Other §15 entries are optional, with hours charged when selected. L-04, L-05 and monthly artifacts use review, profiling and reporting time already budgeted.

Each row’s elapsed range rounds up the larger of the two owner loads divided by their respective weekly capacities. Serial work totals 30–63 working weeks. Overlap may save calendar time only where early classical P5 work actually runs. For alternatives use the common subtotal (all rows except 5) of 147–260 Clau and 170–299 Partner hours. Branch (b) adds actual optional early classical work plus a bounded 6–8 hours each for a 2D cycle. Branch (c) budgets 6–10 + 16–26 + 8–12 + 2–4 = 32–52 Clau hours for core, ladder, memory and direct domain tests, and 4–8 Partner review hours. Reuse SBX-04 evidence or rerun it inside its box. With the common subtotal, branch (b) is 329–575 combined hours plus actual early classical work. Branch (c) is 353–619 combined hours. Record actuals and avoid charging completed classical work twice.

GPU runs checkpoint every 15 minutes and declare wall-time/byte caps. Measure representative throughput/window time before production; D-12 supplies the revised cell-work forecast. Hardware hours remain `[VERIFY]`; unattended compute/exams are outside human estimates.

**P-03. Gate evidence.** Every gate has a JSON evidence index with requirement ID, observed value, threshold, pass/fail, command/config hash, artifact hash, machine and generating commit. Both humans sign the gate PR. Zero missing rows and zero failures are required. Use an immutable annotated tag `gate-N-passed` on the accepted merge. An unresolved `[VERIFY]` blocks only the gate depending on it; it does not retroactively erase completed work. A failed scientific hypothesis can satisfy an experiment-completion gate; a failed correctness criterion cannot.

### 5.1 Learning milestones

These small human exercises support review. Their outputs are learning material with `evidence=false`. The numerical gates still require their own evidence.

- **L-01. Hand-written mini solver.** Clau spends 4–8 hours before the P0.2 merge writing about 50–100 lines of plain NumPy D2Q9 BGK, without an agent and before reading an agent-written solver. Run periodic Taylor–Green decay, fit its amplitude and compare the viscosity with the analytic value. Commit the exercise under `sandbox/learning/`.
- **L-02. Paper derivations.** Clau spends 3–5 hours deriving ν = c_s²(τ − ½), acoustic scaling, the D-05 lift factor, the coarse-grid Re limitation and the quarter-wave period. Partner spends 1–2 hours reviewing the steps. Both must understand them before approving G0 and G1.
- **L-03. Partner onboarding.** During Track B, spend 4–8 hours reimplementing Lettuce LearnedMRT from scratch in plain PyTorch. Compare 100 seeded admissible states to the pinned source in FP64, using B-02’s collision tolerance and direction mapping. Explain how a per-cell MLP is a stack of 1×1 convolutions and how a 3×3 convolution introduces neighbors.
- **L-04. Explain before approving.** On each physics, numerics or evaluation PR, the human reviewer writes 3–5 sentences in the PR conversation explaining the change and why it is correct. An agent may not write the explanation. Budget it inside each review.
- **L-05. Fused kernel ownership.** Clau owns P0.5 and explains the reads, writes, coalescing and boundary traffic. Alongside MLUPS report bytes per update, measured GB/s and its fraction of the device’s bandwidth limit. Distinguish profiler DRAM bytes from an algorithmic lower bound. Use the P0.5 time box.

**P-04. Monthly artifact.** Aim for a shareable figure or short video in `results/` or `sandbox/` about every four working weeks. A ringing trace, a vortex street or B1’s reproduction figure qualifies. Label demos and include the generating config. This is a scheduling aim.

## 6. Phase 0 — Classical 2D solver

Owner: Clau. Partner reviews contracts, supplies unit-test fixtures and learns the git workflow. Dependency: P0.0 ratification. Estimate: §5.

| ID / milestone | Owner-hours | Requirement and numeric acceptance |
|---|---:|---|
| P0.0 Contract and repository ratification | 4–6 each | Resolve OD-01 through OD-06 and OD-08, plus the P0.0 decisions listed in §17; enter two human sign-offs; establish protected main and passing lint/CPU checks; zero unresolved core contract fields. |
| P0.1 Lattice, units, macros and equilibrium | 6–10 Clau | All A-09/A-10 identities pass in 2D and 3D tensor fixtures; CPU FP64 identity tolerance `1e-12`; complete 16² CPU/CUDA smoke run within FP32 `1e-5` relative velocity difference. 3D physics runs wait for P5. |
| P0.2 Collision, streaming and boundaries | 10–16 Clau | BGK passes conservation; periodic tagged streaming returns exactly after a domain-length cycle; every missing population filled once, including all mixed corners. A 10,000-step quiescent box has max speed ≤ `1e-6`, relative mass drift ≤ `1e-5`. A 64×32 unobstructed inlet/outlet/free-slip channel initialized at rho=1, ux=0.03, uy=0, tau=0.8 preserves velocity and density to absolute ≤ `1e-5` over 10,000 steps, including corners. |
| P0.3 Analytic flow gates | 8–12 Clau | Pass both analytic cases below, on CPU and each GPU at the specified production precision. |
| P0.4 Cylinder and refinement | 10–16 Clau | Pass cylinder criteria below, record force histories, temporal convergence, geometry refinement and outlet sensitivity. |
| P0.5 Independent cross-check, fused classical step and profiling | 14–30 Clau | Pass the Lettuce comparison and the fused-path requirements below. On both GPUs, report BGK, RBGK and TRT MLUPS for both portable and fused paths with project boundaries at r = 3, 6 and 9: 1152×384, 2304×768 and 3456×1152. Use five timing repeats under E-12 and verify the 3.5 GiB process-memory cap at every size. Record fused solver-loop throughput for the P1 forecast, with restriction and writing timed separately. 3 operators × 2 paths × 3 grids × 2 GPUs = 36 rows and 180 first-attempt timing samples. Record measured bandwidth under L-05. Every required row must exist. |

P0.5 includes this fused classical-step milestone:

- In Clau’s first P0.5 session, run a real compiled collision-plus-stream fixture on each Turing GPU and its actual OS. Log model, compute capability, OS, driver, toolkit, PyTorch, Triton, build output, fusion and timing. CUDA Inductor generates Triton kernels. The current upstream Triton support list starts at NVIDIA capability 8.0, while these machines target 7.5. Compatibility on each actual stack is [VERIFY]. If the default fails, test a pinned older compatible PyTorch/Triton pair or build a CUDA C++ extension via `torch.utils.cpp_extension`. Fit any hand-written kernel within the high end of the 14–30 hours or replan jointly. Keep a tested portable reference for all three operators. [PyTorch compiler](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler.html) · [Triton compatibility](https://github.com/triton-lang/triton#compatibility) · [PyTorch extensions](https://docs.pytorch.org/docs/stable/cpp_extension.html)
- For all three operators, require fused-versus-portable relative velocity difference ≤ `1e-5` in FP32 after 1,000 steps on the applicable P0.2/P0.3 fixtures, using identical starts and boundary settings. Existing A-14 forcing restrictions remain: the forced Poiseuille fixture uses Guo BGK.
- The full P0 gate suite must pass with the fused path for each classical operator used by its fixture. Fusion does not change equations, boundaries, force accounting or tolerances.
- Use the qualified fused path for P1 generation and the classical comparator in E-12 timing. Learned operators may also be compiled. Record the execution path for every timed row.

**P0-A. Poiseuille.** Periodic x channel, length 2 H, stationary walls at y=0, H, 64 then 128 fluid cells across H; tau=0.8 at H=64 and acoustic-scaled tau at 128. Choose acceleration so analytic maximum velocity is 0.02: `g=8 nu_lu(.02)/H_lu²`. Initialize rho=1, u=0; use Guo BGK. At cell centres, compare against `u_x(y)=g y(H−y)/(2nu)`, `u_y=0`. Stop after relative profile change ≤ `1e-6` over each of three consecutive 100-step intervals, capped at `10 H_lu²/nu_lu` steps. Both finest-grid relative L2 profile error and relative volume-flux error must be ≤ 1%; max transverse speed ≤ `1e-5`. The finer error must not exceed coarse error by more than 10% unless both are below `1e-4`. These project tolerances allow weak compressibility and discrete-wall effects while exposing wrong viscosity/forcing. Analytic channel and boundary basis: [Zou–He, 1997](https://arxiv.org/abs/comp-gas/9611001); no machine-accuracy claim is borrowed from their different incompressible formulation.

**P0-B. Taylor–Green vortex (TGV).** Periodic 64², k=`2pi/64`, U=0.02, tau in `{.6,.8,1.0}`. Initialize `ux=U cos(kx) sin(ky)`, `uy=−U sin(kx) cos(ky)` and `rho=1−U²[cos(2kx)+cos(2ky)]/(4cs²)`, then feq. The analytic velocity amplitude is `U exp(−2nu k²t)` and kinetic energy decays as `exp(−4nu k²t)`. Project velocity onto its initial Fourier mode; fit log amplitude over the interval where analytic amplitude falls from 90% to 30%. Require fitted nu within 1% of A-09, field relative L2 ≤ 2% over that interval and periodic mass drift ≤ `1e-5`. Repeat the tau=0.8 case at 128² with acoustic scaling and verify non-increasing error within 10%. This tests the viscosity law, not only a plausible picture. Formula convention is corroborated by [Lettuce's Taylor–Green source](https://lettuceboltzmann.readthedocs.io/en/stable/_modules/lettuce/flows/taylorgreen.html).

**P0-C. Confined cylinder, DFG 2D-2.** Use channel 2.2×0.41, circle centre(0.2, 0.2), D=0.1, rho=1, nu=0.001, **no-slip** horizontal walls and inlet `ux=4(1.5)y(.41−y)/.41²`, uy=0, evaluated at halfway link intersections. Mean inlet speed 1 defines Re 100 and force normalization. Published historical comparison bands are **maximum** drag `[3.22,3.24]`, **maximum positive** lift `[.99,1.01]`, St `[.295,.305]`; these are not temporal means. Geometry and conventions: [official Featflow specification](https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark2_re100.html). The historical bands are also explicitly reproduced by [Ataei & Salehipour, XLB §4.3](https://arxiv.org/html/2311.16080v3#S4.SS3). Do not substitute the approximately 0.165 unconfined-cylinder value.

Use D=40, 80 cells, and 160 if required; set mean lattice inlet speed 0.02 and derive dt/tau. Rasterize the analytic circle independently at each resolution for this validation only. Ramp inlet smoothly during the first two physical seconds. Evolve at least 25 physical seconds, then measure at least ten lift periods. Over the last five versus preceding five periods require period and drag extrema changes ≤ 1%. Practical gate: St inside the published interval; `|CDmax−3.23|/3.23≤5%`; `|CLmax−1.00|≤.10`; successive accepted-grid changes in all three ≤ 3%. The force tolerances are project choices accommodating stair-step walls; report strict-band membership separately. Source tables have refined examples slightly outside the historical lift band, so do not call the latter an exact truth interval.

Compute body force by momentum exchange on fluid-to-solid links using `2 f_star_i c_i`, sum over the body, and convert units before normalizing; walls and cylinder have separate IDs. Use `CD=Fx/(rho Umean² D/2)`, `CL=Fy/(rho Umean² D/2)` per unit span. Refine the force sampling to ensure its extrema change ≤ 0.5%. The proposed acoustic outlet differs from the continuum benchmark's traction condition: repeat accepted resolution with a doubled downstream extension and require St change ≤ 1% and CDmax change ≤ 2%. If this fails, OD-01 must be revisited and the original-domain gate rerun; an extended-domain pass cannot be relabelled as an exact DFG reproduction.

At the accepted spatial geometry, independently halve physical dt, hence halve lattice velocity and lattice viscosity while preserving physical U, nu and Re. Require St change ≤ 1% and drag/lift extrema change ≤ 2% after the same periodic-convergence test. This is the temporal/Mach-sensitivity check; refining output cadence alone is not timestep convergence.

**P0-F. Acoustic regression.** For a velocity inlet and a fixed-density end, the linear uniform-channel estimate is `T = 4L/c_s`. With L = 24D, `T* = 96 U/c_s = 4.9883` and `St_ac = 1/T* = 0.20047` at U = 0.03. The old ten-unit ramp lasted approximately 2.005 periods. Mean flow, blockage and discretization can move the peak. Test it with the actual boundary implementation.

Run two D-07 fixtures from rest at D = 16, Re = 30, U = 0.03: an empty channel and an aligned p = 16 rounded square of circumdiameter D, centred at (6D,4D). Use the proposed outlet, T = 20 and D-07 pulse. Sample density every step at the fluid centre nearest (12D,4D), breaking ties by highest x then y. Over [100,200] require `(max ρ − min ρ)/ρ₀ ≤ 10⁻⁴` on each fixture. This design limit resolves ringing well below the bulk density-deviation cap. Also require the obstacle to satisfy both parts of E-04’s steady rule, including the half-window mean velocity and drag comparisons. Archive density spectrum, forces and half-window fields. Repeat the fixed-density control with the same start for diagnosis. P0.2’s uniform-state test and both P0-C outlet-sensitivity limits remain mandatory. Under P1-A rerun the accepted outlet checks at the final D-07 settings if changed.

A BGK sweep of both fixtures with both outlets costs `4 × 49,152 × 106,667 / (3.6 × 10⁹ M) = 5.8254/M` solver hours per execution path and device at U = 0.03. Charge all required suite repeats, density/force reductions and output separately.

**P0-D. Independent solver.** Pin a tested immutable [Lettuce release](https://github.com/lettucecfd/lettuce), dependency environment and pure-PyTorch path; record direction/coordinate permutations and shared initial f. Compare periodic 64², tau=0.8, 1,000 steps: relative velocity disagreement ≤ `1e-8` CPU FP64 and ≤ `1e-4` FP32. This classical implementation check is separate from Track B training and is not proof of physics.

**P0-E. Performance.** Report BGK 256² and 512² periodic grids, plus the accepted cylinder grid, on both GPUs. Use §8 timing rules; positive measured MLUPS and peak allocated/reserved memory are required, not an invented performance floor. All 2D cases must finish below 3.5 GiB process peak on the 4 GB device, leaving headroom. Record available device memory, driver and other processes. Failing to access one GPU leaves the gate incomplete.

**Gate G0.** Both readers have completed L-02. Every P0 row and the §11 tests applicable to implemented P0 components pass; BGK/RBGK/TRT fused-path parity and the full fused P0 suite pass; later-phase dataset and learned-gradient tests become required when those components are introduced. P0-F and the three existing physics cases pass, one independent cross-check passes, and both GPU profiles exist. No tolerance may be changed merely to admit a failed result.

**Reviewer self-check**

- How does collision differ from streaming, and which equilibrium moments must be recovered?
- How do τ and the grid units determine physical viscosity and the Guo forcing correction?
- Where do the wall and opening links act, and why does the old outlet ring?
- Why does DFG use maximum drag and lift frequency, and how do the fused kernels access memory?

Read [Krüger Chapters 3–7 and 13](https://link.springer.com/book/10.1007/978-3-319-44649-3), the linked Guo/Zou–He papers, and the official DFG measurement definitions.

## 7. Phase 1 — Dataset generator

Owner: Clau implements; schema and generation parameters jointly owned. Dependency: G0. Estimate: §5.

| ID | Owner-hours | Requirement and acceptance |
|---|---:|---|
| P1.1 Restriction/lifting and schema | 6–10 Clau, 4–6 Partner | Implement D-01–D-05 and D-10–D-14. All round-trip, conservation, timing and halo tests pass; one batch of each Type A/B/C is consumed on CPU and CUDA. |
| P1.2 Geometry/split registry | 6–10 Clau | Default counts are 36 training, 12 validation, 18 main-test, 4 transfer and 12 extrapolation cases. If P1-C reduces training, its frozen count is 24 or 12; held-out counts stay fixed. There is zero forbidden overlap, and descendants retain their split. Reject duplicate shapes and family distinctions smaller than two base cells under D-07. |
| P1.3 Reference pilot | 10–16 Clau | Complete the time/storage forecast, D-06 qualification and P1-A/B/C across all registered families. Peak process memory is ≤ 3.5 GiB and retained data is ≤ 40 GiB. Reject one deliberately invalid reference. |
| P1.4 Generation/resume | 6–10 Clau | Produce the required Type A/C counts and Type B only when requested. Interrupt and resume with identical IDs and CPU fixture arrays; all checksums validate. |
| P1.5 Joint consumer review | 3–6 each | Partner independently loads 10 random shards, checks units and halos, and reproduces Type A labels. There are zero unexplained discrepancies. Test configurations and manifests are sealed; only predeclared classical pilot and qualification summaries may be inspected before P4. |

**P1-A. Mach pilot and frozen cap.** Run this pilot before production references, onset bracketing or project-model evaluation. Under acoustic scaling, lattice velocity is the same at each resolution; the pilot uses r = 3 with a margin for remaining resolution effects.

- For each of the four D-07 family categories, select the registered instance with the greatest frontal blockage and the instance with the smallest analytic radius of curvature. Break ties by shape ID and deduplicate if both rules select the same instance. This gives at most eight pilot cases; harmonic orders 2 and 3 belong to one family category.
- Begin with the A-12 outlet, D-07 pulse, the gentler T = 20 ramp and Re = 240. Run each selected instance through `t* = 200`. Include the inlet ramp and measure the maximum Mach number over all fluid cells at every step.
- At U = 0.03 test that longer ramp first. If any case exceeds 0.085, keep U and the ramp, cap extrapolation at Re 200 and test all selected instances at 200. Replace {200,240} by {180,200} on all six extrapolation shapes. Both levels exceed training Re 160. If still over 0.085, retain the cap and test U = 0.025, then 0.02. Accept the first complete passing branch. If none passes, require a joint revision. Freeze and hash U, ramp, cap, pulse, time indices and taus. E-07’s independent post-freeze stress ladder remains intact.
- Production references still undergo validity checks. A reference with maximum Ma > 0.09 pauses the affected production work for a recorded joint decision. The decision may require additional checks, targeted regeneration, or a revised U and regeneration of its dependent data. It never automatically reruns the whole corpus or mixes datasets generated under different U values. E-09's 0.10 cap remains frozen unless the ruler is explicitly revised; E-06's 0.15 hard limit is unchanged.

At most eight r = 3 cases per attempt run to t* = 200. Base stops are 106,667, 128,000 and 160,000 steps. At U = 0.03 one attempt costs `8 × 49,152 × 106,667 × 27 = 1,132,465,618,944` cell updates. D-12 tabulates cumulative attempts. A longer ramp within the same horizon adds no solver steps. The cap changes viscosity and uses the same number of trajectories. At U = 0.02 each production trajectory needs `160,000/106,667 ≈ 1.50` times the updates, plus earlier unsuccessful pilots.

**P1-B. Shedding-onset pilot.** Resolve an empirical onset bracket for each distinct held-out voxel geometry at its registered orientation.

- The registry has 6 validation + 6 main-test + 2 triangle shapes = 14. Extrapolation reuses the same 6 main-test geometries. Hash the physical shape and mask so reuse occurs only on exact matches. Use D-07’s common pulse, ramp and accepted U at every factor.
- Scan Re `{20,40,80,160}`. Classify using E-04 over the final 100 convective units. Start with a horizon of `t* = 200`; extend unresolved cases by 100 up to 600. An unresolved case never counts as steady.
- For a single steady-to-periodic transition, bisect until its bracket is at most 10 Re wide. At most three bisections are needed within the initial scan intervals. A missing transition is censored, not assigned an invented onset; unresolved or non-monotone transitions require joint review.
- Verify only the two final endpoints of each shape’s bracket at r = 6. If an endpoint's classification changes, refine that shape’s bracket at r = 6 only until the endpoint classifications and bracket width are established. There are no r = 9 pilot runs; D-06 handles reference qualification.
- Save the verified steady lower endpoint a and periodic upper endpoint b for that individual shape. Apply D-08’s 20% margins to this pair for every eligible assignment. Freeze classifications and Re values before learned evaluation. Insufficient values, censored or unresolved onset, or an unverified bracket blocks G1 pending a recorded revision.

The scan/bisection envelope is 14 × (4 + 3) = 98 r = 3 runs and 14 × 2 = 28 r = 6 checks. Under the same schedule this is 1.75 times v0.3’s 56 + 16 runs. The advantage is usable shape-specific margins. Actual cost may fall with earlier bracketing, exact reuse and fewer repairs. At U = 0.03:

- At t* = 200, budget `3,853.5288/M3 + 8,808.0659/M6` hours.
- At t* = 600, budget `11,560.5504/M3 + 26,424.1152/M6` hours. D-12 gives all Mach branches.

Each additional r = 6 repair run of horizon T adds `49,152 × ceil(16 T / U_lu) × 6³ / (3.6 × 10⁹ M6)` hours. Record actual extensions and repairs separately. Reuse an earlier run only when its initial condition, perturbation, parameters, observation schedule and stored outputs satisfy the later requirement exactly. Held-out visibility is limited to classical pilot and qualification summaries.

**P1-C. Compute budget and fixed reductions.** Use P0.5's separate fused-path r = 3, 6 and 9 measurements for each GPU to forecast all P1 and reserved held-out generation work in D-12. The proposed planning cap is **168 GPU-hours per machine**, with both machines running in parallel. This is one week of device time per machine, spread over four working weeks to leave room for Track B and ordinary use; it is a scheduling limit, not a claim about measured performance.

Multiply projected solver-loop hours by 1.25 as an explicit planning reserve, then add measured restriction and write overhead. Account for already completed pilots and every known qualification expansion or repair. Schedule ready jobs in phase and case-ID order, assigning each to the machine with the earliest predicted completion time; break ties by device ID. A machine runs one generation job at a time. Compare the resulting load on **each** machine with its cap, rather than checking only the combined 336 GPU-hours.

If either cap is exceeded, apply these reductions in order and recompute the forecast after each:

1. Reuse exact eligible pilot/production runs, counting their compute only once. This removes duplicate work without changing any sample or comparison.
2. Reduce training instances from three to two per family. Retain the lowest-ID k = 2 and k = 3 harmonic instances; for ellipses and squares retain the first two shape IDs. Training changes from `3 families × 3 shapes × 4 Re = 36` cases to `3 × 2 × 4 = 24`; total cases change from 82 to 70. Family balance, both harmonic subtypes and the full Reynolds range remain.
3. Retain training Re 20 and 160 only. Training changes to `3 × 2 × 2 = 12` cases and the total to 58. This reduces supervision density while retaining the same families, physical task and low/high Re endpoints. Recompute sample counts and freeze the smaller training cohort before any project-model training.

Record every triggered reduction in the decision log and dataset manifest. The 46 validation, main-test, transfer and extrapolation cases, the r = 6 reference factor, and all tolerances stay fixed. A failed D-06 representative still triggers the full required qualification expansion; budget pressure cannot delete it. If the reduced plan or later required repairs exceed either cap, both developers must record a revised schedule or resource plan before continuing. There are no further automatic cuts.

**Gate G1.** L-02 is reviewed and all P1 rows pass. Training and validation references meet D-06; retained data is ≤ 40 GiB and peak process memory is ≤ 3.5 GiB. There are no corrupt or silently skipped cases. Held-out classical pilots and qualification may run now; candidate evaluations remain sealed until P4. Missing retained test fields may be regenerated from frozen configurations. Failures stay in manifests and are corrected, never replaced with favourable samples.

**Reviewer self-check**

- Why restrict density and momentum together, and why does a Type B patch lack a unique conservative collision label?
- How do acoustic scaling and the non-equilibrium lifting factor preserve the intended units?
- What makes a halo causal and a split free of trajectory leakage?
- How can one geometry’s onset, a failed reference or a Mach breach change the forecast?

Read [Astoul et al. on grid conversion](https://arxiv.org/abs/2004.14887), [h5py datasets](https://docs.h5py.org/en/stable/high/dataset.html), and review the derivation in D-02–D-05 together.

## 8. Phase 2 — Evaluation harness and the frozen ruler

Owner: Partner builds; Clau reviews physics; joint ownership. Dependency: G1. Project-model selection/evaluation waits for G2; Track B source/periodic sandbox diagnostics are the explicit exception and have no headline eligibility.

### 8.1 Metrics and validity

**E-01. Observation domain.** Compare candidate and reference after D-04 restriction to base in physical units. Score every fluid cell, including cells beside halfway openings; exclude only solids. Also report the region within 2D of the obstacle, wake `(xbody+D/2,xbody+8D)×(ybody−2D,ybody+2D)`, and remaining domain, with masks fixed before model results. Score candidates on the original times and coordinates. Only the D-06 reference-to-reference qualification permits a time shift.

**E-02. Velocity error.** At identical physical times with zero fitted lag, `e_u(t)=sqrt(sum V|u−u_ref|² / max(sum V|u_ref|², 1e-12 U² sum V))`. Primary score is the square-root ratio of sums over cells **and times**, not the average of per-frame ratios. Report per-time curve, maximum and each regional score. Report a separate time-mean-field error over the late interval; it does not replace the trajectory error.

**E-03. Common rollout windows.** Use two modes. Restart mode initializes all methods from identical restricted/lifted fine snapshots at `t*=50,100,150`, then free-runs 20 convective units without resetting. These three windows supply primary trajectory error. Cold-start mode initializes every method at rho=1, u=0, applies the identical D-07 ramp and transverse pulse and runs to `t*=200`; use `[100,200]` for force/statistical metrics. Candidate initialization never receives later reference states. Reference loading and lifting cost are reported separately for restart mode; the headline cost uses cold starts and includes its own initialization. Restart improvement is not described as a cold-start speedup.

E-02, E-03 and every E-09 comparison use zero time shift. A restart never replays the initial disturbance.

**E-04. Forces/frequency.** Report mean CD, CDmax, CLmax, CLrms and St; relative drag error uses reference CD, switching to absolute if `|CD_ref|<1e-6`. Near-zero lift uses absolute error. St uses linearly interpolated upward crossings of demeaned CL, ≥ 10 cycles, period coefficient of variation (CV) ≤ 5%, demeaned lift root-mean-square (RMS) ≥ `1e-4`; `St=D/(U mean_period)`. Cross-check within 2% using Hann-windowed fast Fourier transform (FFT) with a quadratic fit to log power at the peak and adjacent bins. Test synthetic off-bin St {0.133,0.165,0.237}; no raw-bin or doubled drag-frequency estimate.

Classify a reference as **steady** only if RMS of demeaned lift `C'_L,rms<1e-4` and mean drag/velocity change ≤ 0.5% between halves of the late interval; **resolved periodic** requires the cycle/spectral conditions, otherwise **unresolved**. Rotated shapes may have nonzero steady mean lift; raw CLrms remains a separate metric. Unresolved references block frequency qualification. For steady references St=N/A and require candidate `C'_L,rms≤reference C'_L,rms+.01`. Missing/unresolved candidate shedding against a periodic reference fails. Retain traces.

**E-05. Conservation drift.** Report local collision residual separately from global balance. On closed periodic unforced fixtures, compare mass and momentum against initial values, normalizing momentum by `M0 U` even when initial net momentum is zero. In open/walled domains calculate residuals after subtracting **measured discrete population flux** at openings, applied source impulse and wall impulse. Do not demand constant mass in an open flow or constant momentum when walls exert force. Require normalized cumulative mass-balance residual ≤ `1e-5`, momentum residual ≤ `1e-4` over 10,000 fixture steps; report balance drift curves over production horizons. Numerical budgets are project diagnostic criteria; failure invalidates any efficiency claim.

**E-06. Stable horizon.**

- Failure means nonfinite populations or memory, rho ≤ 0, `|rho − 1| > 0.10`, `max|u| > max(0.25, 5U_lu)`, a conservation violation, or `min(f) < −0.01 rho`.
- The separate accuracy-regime limits remain maximum Ma > 0.15 or density deviation > 0.05.
- Untimed validity certification checks every step. Timed diagnostic runs check every `N = 100s` steps at candidate factor s, plus endpoints and outputs, giving equal physical cadence.
- A sampled event identifies an interval. Rerun from the identical start with untimed, every-step checks to locate the exact first failure and any earlier transient. Do not confuse detection time with failure time; flag nonreproducible failures rather than inventing a step.
- Never clamp a failed run. The stable horizon is the earliest failure; completion is right-censored as `≥cap`. Only densely certified trajectories enter timing claims.

**E-07. Largest tested stable Re.** At fixed geometry, diameter 16/32/48, P1-frozen U and boundaries, change only viscosity/tau. Use Re {20, 40, 80,120,160,240,320}, horizon `t*=200`, all six validation shapes and three learned seeds. Report all outcomes, largest **contiguous** stable value from 20, stable islands and next failure; passing 320 means ≥ 320 on this ladder. This is `6 shapes × 7 Re × 3 rungs = 126` trajectories per method/seed: 378 = 3 × 126 for BGK, RBGK and TRT and 378 for each three-seed learned method. At U = 0.03 the 378 classical trajectories cost `42 × 49,152 × 106,667 × Σ_op Σ_s(s³/M_op,s) / (3.6 × 10⁹)` hours, or 6,606.0494/M at one common rate. Forecast this separate post-freeze cost before scheduling. This descriptive sweep is outside checkpoint/adoption selection and runs only after candidate freeze, so the main test remains Re interpolation. Test/extrapolation transfer uses the sealed cases and never reselects a model.

### 8.2 Matched-accuracy efficiency protocol

**E-08. Freeze before evaluation.** G2 freezes metrics, masks, budgets, resolution ladder, split hashes, reference criteria, horizon, timing, seed policy and eligible comparison methods in a versioned evaluation manifest. Every learned result stores that hash. Any later change, including a bug fix affecting numbers, needs both approvals, a new ruler version and reruns of **every previously measured model and classical baseline**. Keep old results visibly superseded. Never pool ruler versions in a headline table.

**E-09. Matching criterion.** A qualifying configuration must satisfy all of these:

- Restart velocity error ≤ 5%, with wake error ≤ 10%.
- Cold-start late time-mean velocity-field error ≤ 5%, with wake error ≤ 10%. Apply the E-02 norm after averaging over [100,200].
- Mean drag-coefficient error ≤ 5%; Strouhal number error ≤ 3% when defined, or the E-04 steady-flow rule.
- Every restart and cold-start horizon completes, E-05 balance limits pass, and maximum Ma ≤ 0.10.

P1-A chooses U using r = 3 pilot maxima ≤ 0.085 before production. A later reference maximum above 0.09 requires a recorded joint decision, not automatic corpus-wide regeneration. Freeze U and the 0.10 matching cap before G2/project-model evaluation; no result-driven relaxation. At U = 0.03, free-stream `Ma = 0.03√3 = 0.051962`, so local peaks matter. Publish instantaneous cold-start error too: the headline matches late statistics and restart trajectories, not phase-exact long cold starts.

**E-10. Validation selection.** Choose each variant's smallest qualifying diameter in {16, 32, 48}, requiring E-09 on all 12 validation cases/all three seeds. Otherwise report unmatched. Compare with the fastest qualifying BGK, RBGK or TRT at its selected rung; reference r=6 is ineligible as comparator. A “coarse learned versus finer classical” claim requires the learned rung strictly smaller. No qualifying classical rung means no matched-accuracy headline; the reference cannot rescue it.

**E-11. Test protocol.** Freeze checkpoints, resolutions and hyperparameters before unsealing the 18 main-test cases. Run every method/case/seed under E-12 without reselection. All 18 must satisfy E-09 for a general matched-accuracy claim; otherwise report exact coverage and every failed or unmatched row.

Report four triangle-transfer cases and twelve extrapolation cases at the P1-frozen pair separately, using the same frozen models. Their velocity metrics use D-09's labelled sparse cadence; they are outside the headline denominator and cannot select or adopt a model. No test-informed extra rung or tuning may rescue a failed claim.

**E-12. Timing boundary.** Use the same physical case, device, environment, precision and horizon. Classical comparison rows use P0.5's qualified fused BGK/RBGK/TRT path; learned operators may also be compiled. Every timed row records `execution_path` as `portable`, `torch.compile` or `cuda_cpp_extension`, with compiler/kernel version and configuration. Portable classical timings remain labelled profiling/reference rows. Finer grids take proportionally more steps. Warm up 200 steps, restore the initial state and synchronize.

- **Core plus outputs:** time initialization, geometry upload, features, collision, projection, routing, memory, streaming, boundaries, force extraction every step, prescribed output transfers and synchronization.
- **With diagnostics:** additionally perform E-06 checks every `100s` steps. Report both speedups; the headline uses core plus outputs. Disable optional diagnostics in the core pass instead of subtracting an estimated cost.
- Exclude reference generation, training, plotting and environment setup, but report their costs separately. Model loading and compilation receive explicit cold-start columns.
- Take five repeats in alternating model/baseline order. Report median, range and coefficient of variation (CV). If CV > 5%, investigate and repeat the complete pair, with at most **three attempts total**: no more than 15 samples per method/profile. Retain all attempts. If the last remains noisy, flag it and exclude it from a positive headline.
- CPU timing uses a fixed thread count and wall clock. Reset GPU peaks after warm-up and report allocated, reserved and process/device memory. See [CUDA timing](https://docs.pytorch.org/docs/stable/notes/cuda.html) and the [peak-memory API](https://docs.pytorch.org/docs/stable/generated/torch.cuda.max_memory_allocated.html).
- For small 2D grids, batch independent same-resolution cases with B ∈{2, 4, 8}. Choose classically the smallest B with < 5% throughput change from B/2, then freeze B and order for every method. If the 3.5 GiB limit prevents this, use CUDA graphs of the qualified fused classical step or the learned step, verify parity and report preparation cost. Unresolved launch overhead precludes positive speedup claims.
- Divide batch elapsed time by B, retain group IDs and bootstrap whole batches. Report batch-average costs, not invented individual-case times.

**E-13. Reporting efficiency.** Speedup=`T_classical/T_learned`, memory ratio=`M_classical/M_learned`; report case or registered-batch medians and geometric mean with paired 95% bootstrap (10,000 resamples, seed 6606; whole batches under E-12). Seeds are not independent geometries. A positive headline requires mean speedup ≥ 1.10, interval lower bound > 1, no memory regression, E-11 qualification and explicit coverage; otherwise “no demonstrated efficiency improvement.” Report GPUs separately.

Show total-cell MLUPS=`B Nx Ny (Nz) steps/(10^6 seconds)` and fluid-cell MLUPS; sparse dispatch counts full solver updates, not just neural cells. Report generation/training separately. Break-even=`training_seconds/(T_classical−T_learned)` if positive, alongside generation cost. Claims concern this PyTorch implementation/hardware, not optimized industrial kernels.

For every learned-versus-classical row, also report these efficiency-bar columns:

- **Measured cost ratio:** learned/BGK cost per total-cell step at the same resolution, precision and device. Use the same core-loop timing boundary, output cadence and batching policy, and state whether initialization is excluded from this diagnostic. Report each classical method’s BGK-normalized cost, including TRT, and identify the fastest qualifying method used for the speedup.
- **Acoustic break-even ratio:** `B_acoustic = (s_classical / s_learned)^(d+1)`. Cell count contributes d powers and the finer timestep contributes one. In 2D, 16 versus 32 cells/D gives 8; 16 versus 48 gives 27; 32 versus 48 gives 3.375.
- **Distance from the bar:** show the measured ratio beside B_acoustic. It predicts an ideal BGK comparison only if per-cell cost is resolution-independent and fixed overhead is negligible. For an RBGK or TRT comparator, its measured relative cost also matters. The measured E-12 end-to-end speedup and unchanged E-13 headline criteria remain authoritative.

### 8.3 Harness milestones and gate

| ID | Owner-hours | Acceptance |
|---|---:|---|
| P2.1 Classical parity and metric fixtures | 6–10 Partner + 2–4 Clau | Review P0.5’s implementations of RBGK and TRT against A-07, TGV and cylinder gates. Use the qualified implementations directly. Analytic/synthetic metrics recover zero error, known sinusoidal St and injected 1% amplitude error within `1e-6` absolute on CPU FP64. |
| P2.2 Baseline matrix | 8–14 Partner | 3 operators × 3 resolutions × 12 validation cases = 108 rows. Report all failures. For each row measure one cold start and three restarts. This gives 108 cold starts + 324 restarts = 432 trajectories before timing repeats. |
| P2.3 Timing/validity harness | 6–10 Partner | Five repeats/profile; injected failures bracketed at sampled cadence and located exactly by untimed rerun; retry cap and batch/graph parity tested. |
| P2.4 Freeze and independence audit | 6–10 Partner +4–6 Clau | Signed manifest; reproducible CPU metrics; training rejects test access; no learned project-ruler evaluation before freeze; Track B labelled separately. |

P2.2 costs `12 × 49,152 × (106,667 + 3 × 10,667) × Σ_s(s³/M_op,s)/(3.6 × 10⁹)` hours per operator at U = 0.03 for s = 1, 2, 3. Summing all three at a common assumed rate M gives 2,453.6914/M hours for one traversal. Forecast actual timing separately for each E-12 profile, device and repeat, plus warm-up, certification, retries and I/O. Fused parity work in P0.5 costs 3 × 2 paths × 2 GPUs × 1,000 steps per applicable fixture before the full gate suite. Multiply each fixture’s updates by its cell count and divide by its measured rate. The Guo fixture uses BGK only.

**Gate G2.** All P2 rows pass, all three classical baselines qualified, complete fixed evaluation manifest and numeric fixtures stored, and two signatures. A poor classical result cannot be hidden by omitting its row. A future operator may use a different training objective while the E-series ruler remains unchanged.

**Reviewer self-check**

- Which cells, times and denominator enter E-02, and where may a time shift be used?
- Which boundary terms enter conservation and what does a censored horizon mean?
- How do the selection and freeze rules protect the test cases?
- Which of BGK, RBGK and TRT sets the speedup, and why must GPU timing include synchronization?

Read [Kochkov et al. on learned coarse solvers](https://doi.org/10.1073/pnas.2101784118), [Latt–Chopard](https://arxiv.org/abs/physics/0506157), and the linked PyTorch timing documentation.

## 9. Phase 3 — Replicate, then explore

Owner: Partner, with Clau reviewing collision physics, data and rollout comparisons. Project 3a/3b depend on G2; Track B has the explicit prerequisites below. The final operator design remains open.

### 9.0 Track B: source reproduction, port and sandbox

**B-01. B1 — source reproduction before correction.** Started 2026-10-20, Partner, GTX 1650 (DEC-007). Both runs use the pinned historical Lettuce release and source script, with **no project code**. Select source training mode and train from scratch; neither run loads `net_preset.pth`. Preserve the full 64² grid, 100-step horizon, FP64 and anomaly detection.

- **B1a, as published:** add seed 11 before initialization and shuffling. Otherwise preserve source training behaviour, including optimizer updates in the pass labelled “testing.” Thus all 40 pairs affect fitted weights; the 32/8 labels do not define a holdout. Expect `50 × (32+8) = 2,000` optimizer updates; record observed counts and the source diff. This is the sole intentional exception to frozen evaluation, carries `evidence=false`, and cannot select or validate a project model.
- **B1b, corrected:** start again from the same seeded initialization and pair split, but freeze parameters and optimizer state during evaluation. Expect `50 × 32 = 1,600` optimizer updates and record unchanged evaluation hashes. The randomized split remains temporally dependent; SBX-02 performs the separate time-blocked audit.
- **Acceptance for each run:** complete 50 epochs; save all 40 pair IDs, split, curves, trained weights and environment/source hashes; complete a finite 100-step comparison; measure peak memory ≤ 3.5 GiB. Record observed behaviour rather than inventing a numerical reproduction tolerance.
- **Published comparison:** reproduce the kinetic-energy curve in Figure 3, vorticity fields in Figure 4 and diagonal vorticity at 4,000 steps in Figure 5 of the [Lettuce paper](https://arxiv.org/html/2106.12929). Compare B1a against those figures, then B1b against B1a. Record discrepancies and any extraction uncertainty; quantitative curve values remain `[VERIFY]` until obtained from auditable source data or documented digitization.

Effort: 14–24 Partner-hours, including the additional 2–4 hours for the second run and comparison, plus 2–3 Clau review hours. Machine time is separate. Appendix B audits may proceed after setup.

**B-02. B2 — port fidelity.** Start after P0.2's periodic BGK/conservation and tagged-streaming checks pass; it need not wait for G0–G2. Use **B1b weights** and the audited moment transform. On 1,000 admissible states require collision relative error ≤ `1e-10` in FP64 and exactly 530 parameters. On the matched periodic fixture, require 100-step velocity disagreement ≤ `1e-8` in FP64. Store direction-order mapping, fixture/weight hashes and zero unexplained deviations. This checks fidelity, not project accuracy. Effort: 4–8 Partner-hours plus 2–3 Clau review hours; completion is required by G3.

**B-03. B3 — sandbox lane.** A finite B1b fixture enables source experiments; B2 enables project periodic shear and Taylor–Green vortex (TGV) fixtures. Store small code/configs/records under `sandbox/` and large artifacts externally. Every run has `evidence=false`, source/commit/config/seed/device hashes and an SBX ID. It has no project-test access or headline/adoption eligibility; README summaries belong only in “what we tried.” Use the §15 fields and entry-specific time boxes of 4–8 hours for SBX-01–03 and 2–6 hours for SBX-04–05. Promotion requires X-02 after G3 on the frozen ruler. Completion records every attempt/failure, hours and PR; negative outcomes count.

### 9.1 Phase 3a: BGK pipeline sanity

**P3a-01.** First fit a scalar coefficient multiplying `(f−feq)/tau`, projected as needed, using Type A data. Starting coefficient 0 must converge to −1 within `1e-5`; validation relative population error must be ≤ `1e-5`. This deliberately easy control checks target timing, normalization and gradients, not architectural capability.

The sanity dataset additionally includes 60,000 training and 6,000 validation synthetic/local TGV pairs, equally divided among tau `.6,.8,1.0`, with separate seeds 7101/7102 and disjoint generated states. Synthetic states use T-01 ranges and projected non-equilibrium perturbations whose L2 norm is uniform in `[0,1e-3 rho]`, rejecting nonpositive populations. Half the pairs come from the first 1,000 steps of independently initialized periodic 64² TGV fixtures with U uniformly in `[.01,.03]` and phase offsets uniform in `[0,2pi)`; entire trajectories remain in one split. This covers the viscosity support of the sanity rollout. The records have no obstacle/Re label and are used only for 3a, not pooled into 3b or final model selection.

**P3a-02.** Then fit a small per-cell learned mapping of local f, feq and tau to a conservative increment, with no call to the BGK target at inference. A suggested sanity configuration is two 64-unit rectified linear unit (ReLU) layers with a nullspace output. This is a disposable pipeline fixture, not the selected research architecture. Use Adam with learning rate `1e-3`, batch size 4,096 and at most 100,000 optimizer steps. Evaluate every 500 steps and choose the best validation loss, without test data. Freeze feature normalization from training data only. Require relative f_post L2 error ≤ `1e-4`, relative increment L2 error ≤ `1e-2` with denominator floor `1e-12`, and A-07 conservation. The increment metric prevents equilibrium from hiding a bad collision.

**P3a-03.** On the 64² TGV development fixture with tau = 0.8, initialize identical f and run 1,000 steps. Require learned-versus-BGK velocity relative error ≤ 1%, no invalid state and mass drift ≤ `1e-5`. Training and inference must each peak at ≤ 3.5 GiB on the GTX 1650. Run seeds 11, 22 and 33; all must pass. If these fail, investigate data phase, units, scaling, masking, gradients and capacity before proceeding. Failure is not evidence that the coarse-grid research idea is bad.

Milestones: scalar/gradient control 3–5 Partner-hours; nonlinear sanity 5–8; rollout/memory verification 4–6; Clau review 3–5. **Gate G3a:** every P3a criterion passes, with no relaxed threshold.

### 9.2 Phase 3b: explicit replication baseline — proposed OD-05

**P3b-01. Choice and scope.** Retain Bedrunka et al.'s Lettuce neural multiple-relaxation-time (MRT) baseline: it targets a finer flow with a small local network. Corbetta's BGK imitation alone does not answer the coarse-grid question. Learned higher-moment relaxation leaves physical shear viscosity fixed; this limitation motivates the separate scaling instrument, not a retroactive baseline change. [Lettuce paper §3.1](https://arxiv.org/html/2106.12929).

Maintain two named records: B1 owns `lettuce-source-reproduction`; `lettuce-project-baseline` retrains the audited operator on this SDD's coarse-grid task. The latter is the mandatory exploration comparator. Source work is consumed here, not repeated after G2.

**P3b-02. Confirmed source facts, read 2026-10-20.** Two biased ReLU multilayer perceptrons (MLPs), `j,n:9→24→1`, have 530 parameters in total. Raw Dellar moments enter without preprocessing. With `P=[0,2,1,5,4,3,6,8,7]`, the output maps are `tau_Jx=.5+exp(j(m))`, `tau_Jy=.5+exp(j(Pm))` and `tau_N=.5+exp(n(m)+n(Pm))`, acting on moments 7, 8 and 6. Other relaxation times use physical tau.

- **Setup:** doubly periodic shear layer, Re = 5,000, Ma = 0.05, 128² fine BGK reference and 64² coarse grid. `grid_fine_to_coarse` uses point sampling and non-equilibrium rescaling.
- **Data:** snapshots every 100 coarse steps yield 40 pairs. Unseeded `torch.randperm` precedes the 32/8 split, interleaving one trajectory across train/test. The split changes every run.
- **Training:** each pair runs on the full 64² grid for 100 steps. Velocity/vorticity/energy sum-of-squares weights are 0.6/0.2/0.2. The script uses Adam at `3e-4`, 50 epochs, StepLR(40, 0.1), FP64 and `torch.autograd.set_detect_anomaly(True)`.
- **Execution:** default `train=False` loads `./net_preset.pth`. The “testing” pass calls the same training function and `optimizer.step()`. Coarse comparison starts from its own initial condition, runs 4,000 steps and compares with the final restricted fine snapshot.

These are source observations, not endorsements. [Released script](https://github.com/lettucecfd/lettuce-paper/blob/main/02_neural_collision_model/script.py).

**P3b-03. B1/B2 source audit.** Pin script/framework hashes; framework 0.2.1 is `ed0535dceb4979a11a0c341f19dc566727bedc39` ([tags](https://github.com/lettucecfd/lettuce/tags)). Record transforms, initialization, sampling and gradients. Tagged Dellar normalization, `torch_gradient` differentiability and preset provenance remain `[VERIFY]`; Appendix B also tracks quantitative figure extraction. These block dependent fidelity claims, not setup. Both B1 runs exclude the preset.

**P3b-04. Deviations.** Seed every run. B1a alone preserves the source's test-pass updates; B1b and every project evaluation freeze parameters and optimizer state. Both B1 runs retain disclosed temporal dependence, SBX-02 blocks time, and project splits separate independent cases. If the historical derivative detaches, preserve that behaviour in B1a; document and test any differentiable correction in B1b/project training. Compare project FP32 against FP64. Source transfer point-samples `f_s=f_f[:,::2,::2]`, then uses `feq_s+2(tau_c/tau_f)(f_s−feq_s)` ([utility](https://lettucecfd.readthedocs.io/en/latest/_modules/lettuce/util.html)); the project uses D-04/D-05. Disclose all changes. The x/y exchange and tau > 0.5 guarantee neither full square-lattice symmetry nor nonlinear stability.

**P3b-05. Project training recipe.** Retain the source architecture, physical shear viscosity and output maps. Use full-field Type C windows with D-14’s physical horizon of one convective unit. K = 100 remains a source-fidelity choice for B1/B2.

- **Data:** each window covers the full 384 × 128 base grid, with `K = ceil(16/U_lu)`, R = 0 and ten sparse D-14 targets. The default corpus has `36 cases × 32 windows = 1,152` training windows. The `12 cases × 8 windows = 96` validation windows are for training-loss monitoring only: they cannot select a checkpoint, tune an idea or establish adoption. Type B patches remain available for explorations and 3D.
- **Fixed visit budget:** define a virtual epoch as 1,024 window-visits, independently of corpus size. Run 50 virtual epochs, giving `50 × 1,024 = 51,200` visits per seed. Cycle through seeded permutations of the entire corpus without resetting at virtual-epoch boundaries. This is `51,200/1,152 = 44.444…` corpus passes. If the P1 budget rule reduces training to 24 or 12 cases, the 768 or 384 windows receive `66.667…` or `133.333…` passes; the visit budget stays fixed.
- **Optimization:** microbatch 1, accumulation to effective batch 8, Adam learning rate `3e-4`, StepLR with step size 40 virtual epochs and factor 0.1, seeds 11, 22 and 33, gradient-norm clip 1. There are `1,024/8 = 128` updates per virtual epoch and `50 × 128 = 6,400` updates per seed.
- **Loss:** at the ten stored target steps, average over valid fluid cells/channels. Use weight 0.6 for velocity squared error divided by `U²`, weight 0.2 for vorticity squared error divided by `(U/D)²`, and weight 0.2 for squared domain-mean kinetic-energy-density error divided by `U⁴`. Energy density is `rho|u|²/2`. Central vorticity differences use an eroded fluid mask and never cross solids. Full-domain energy, sparse target cadence, normalized means and FP32 are disclosed project deviations.
- **Memory.** Start with five-step checkpoint segments, retaining their boundary states and recomputing one segment in backward. At K = 534 there are 107 segments (last length 4) and 108 endpoints × 1.6875 = 182.25 MiB. For two 24-unit source networks with an additional axis-permuted evaluation of each, four width-24 activation fields cost 18 MiB per step × 5 = 90 MiB before other autograd tensors. A full loader window needs 7.3125 MiB. Report actual peak for a complete microbatch forward/backward/update under the 3.5 GiB process cap on GTX 1650. Check T-03. Adjust segment length or use nested recomputation if necessary, preserving every target, gradient and visit. Record endpoints, live activations, gradient/optimizer storage, allocator and context separately. Failure to fit blocks the recipe.
- **Monitoring:** every five virtual epochs, report loss on all 96 Type C validation windows with gradients disabled and parameters unchanged. Store it as a diagnostic curve, separate from the selection score below.

Checkpoint selection uses the frozen E-03 restart protocol, not the Type C monitors:

- Evaluate every five virtual epochs, on three restarts for each of the 12 validation cases: `3 × 12 = 36` windows per selection and ten selections per seed.
- A completed window receives ranking score `min(e_u, 1e6−1)`; an invalid or incomplete window receives `1e6`. This sentinel is only a ranking device. Publish the uncapped valid errors and explicit failure reasons.
- Minimize failed-window count, then the mean of all 36 fixed scores, then choose the earlier virtual epoch. Never rank on a changing survivor subset.
- Run cold-start validation once for the selected checkpoint. No test values enter monitoring or selection.

At U = 0.03 one seed requires 51,200 × 534 = 27,340,800 steps, or 1,343,855,001,600 forward cell-steps. Training, including backward/recomputation, costs `373.2931/M_train` hours. Ten full restart selections cost `36 × 10 × 10,667 × 49,152 / (3.6 × 10⁹ M_eval) = 52.4304/M_eval`. Ten monitor passes cost `10 × 96 × 534 × 49,152 / (3.6 × 10⁹ M_monitor) = 6.9992/M_monitor`. Twelve final cold starts add `17.4763/M_cold`. Sum and multiply by three seeds. At a changed U, use K = ceil(16/U), restart length ceil(320/U) and cold length ceil(3,200/U). All rates require measure-on-device evidence [VERIFY].

**P3b-06. Acceptance.** Link both B1 source runs and the B2 parity checks; do not repeat them here. Train all three project seeds, pass conservation/memory constraints and publish every validation row. For each seed, require all three restart windows of at least one validation case to finish. Record which cases finish and every harder failure; the fixed validation-wide ranking still applies. Improvement over BGK, RBGK or TRT is not a baseline gate condition.

If 3b completes fewer validation cases than RBGK at the base rung, place that finding and both completion counts prominently beside the results and in the README. A weak baseline remains useful replication evidence, but beating it alone does not satisfy X-02.

Milestones: project adaptation/checkpointing 11–18 Partner-hours; results/review 4–8; Clau project review 7–12, in addition to 3a. **Gate G3:** G3a, both B1 runs and B2 are complete; zero unresolved items needed for claimed source/port comparisons; P3b minimal rollout, conservation, GPU-fit and complete-row criteria pass. Unused preset provenance may remain open with the checkpoint excluded. An unavailable dependency requires an explicit OD-05 revision, never an approximation labelled a verified replica.

### 9.3 Phase 3c: continuous exploration process

**X-01. Entry lifecycle.** Use §15 only. Every idea has a hypothesis, target metric/effect size, cheapest falsification, kill criterion, owner, time box, status and result/PR link. New entries or results require a normal SDD PR; existing specifications stay unchanged unless the ruler itself changes. Status is exactly `proposed`, `running`, `killed` or `adopted`. Failed and timed-out entries remain visible.

**X-02. Adoption.** Before starting, nominate one primary gain against the project 3b baseline:

- At least 10% lower validation velocity error.
- At least 20% longer median valid horizon, with at least one additional completed case.
- At least 10% lower matched-accuracy runtime.

Use three seeds, identical case/compute budgets and paired comparisons. Require no additional failed case versus 3b, no relative regression above 2% in other defined accuracy metrics, no conservation/memory violation, and a paired 95% bootstrap interval excluding zero for the nominated improvement.

For adoption and coverage reporting, a completed case must finish all three E-03 restarts and the cold-start horizon with valid states under E-06. This does not impose E-09 accuracy matching on the completion count. P3b-06 retains its weaker, explicitly separate replication gate.

Also compare each candidate seed against **BGK, RBGK and TRT at the same resolution rung**. Completion count must be at least `max(N_complete,BGK, N_complete,RBGK, N_complete,TRT)`. On each case completed by the candidate and at least one classical method, primary velocity error must be ≤ `1.02 × min(e_BGK, e_RBGK, e_TRT)`, taking the minimum only over classical methods that completed that case. Thus the better classical comparator is chosen per metric, not whichever method is easier to beat. A case with no completed classical comparator supplies no error comparison; report it separately. This guard prevents adoption based solely on beating a failing 3b baseline.

Undefined metrics are not zero. If the relevant baseline error is near zero, use the E-02 absolute floor and declare that entry unsuitable for an error-improvement claim. Type C validation-loss monitors do not select checkpoints or determine adoption. Every rejected tradeoff remains reportable.

**X-03. Selection budget.** Allow at most eight entries per reporting cycle and two hyperparameter variants per entry before its kill decision. A later variant is a separately logged entry. Track validation evaluations and failed runs. Confirm adoption on all 12 validation cases after a cheap two-case screening; never substitute a favourable subset. Validation overfitting remains a limitation even with a fixed test set. After G3, every two weeks review time spent against the time box and P4/P5 progress.

**X-04. Test opening.** Freeze the cycle's adopted list and checkpoints before P4 unseals test results. P3c may continue while final evaluation runs, but any idea influenced by test outcomes belongs to a new cycle with a new jointly committed holdout cohort. Test results cannot retroactively adopt, tune or delete an entry. The initial cycle may validly contain zero adopted ideas.

**Reviewer self-check**

- How can correct forward values coexist with incorrect gradients?
- How do conservation and locality constrain a collision update?
- Which source behaviours do B1a and B1b preserve, and how is the project adaptation different?
- What long-horizon failure could a low one-step loss miss?

Read the linked Lettuce source/paper, [Corbetta et al.](https://doi.org/10.1140/epje/s10189-023-00267-w), and [PyTorch checkpointing](https://docs.pytorch.org/docs/stable/checkpoint.html).

## 10. Phase 4 — Generalization, scaling and headline result

Owner: Partner with Clau. Dependency: G3; candidate registry frozen before test opening.

**P4-01. Scaling sweep.** This is a controlled capacity experiment, not architecture search or a final operator choice.

- Stress-capable core: 2 radii {0,1} × 3 widths {4,32,192} × 3 fractions {1/8,1/2,1} × 3 seeds {11,22,33} = 54 runs. Add width 64 on the full-data R = 0 column for 3 runs. At R = 0 run ghost-only on full data at all four widths and all three seeds = 12 more. Total 69 primary runs plus 3 secondary = 72. The paired R = 0 full-data experiment contains 2 × 4 × 3 = 24 protected runs.
- Nest fixed window IDs **within every training case**: 4, 16 or 32 windows per case. With 36 cases this gives 144, 576 or 1,152 windows. The 24-case reduction gives 96/384/768; the 12-case reduction gives 48/192/384. This measures window-count scaling with family/Re support held fixed, not scaling the number of geometries.
- Use microbatch 1, effective batch 4, D-14’s K = ceil(16/U), Adam learning rate `3e-4`, gradient-norm clipping at 1 and P3b-05's loss. Cycle seeded permutations of each subset. Monitor the 96 Type C validation windows every 400 updates on full-data plateau runs and at updates 200, 400 and 600 on screening runs, for loss diagnostics only.
- **Full-data column:** train all 33 arm/radius/width/seed runs until the plateau rule below or **51,200 window visits**, whichever comes first. At batch 4 the cap is 12,800 updates, matching P3b's visit budget. This equals 44.444 passes through the default corpus, or 66.667/133.333 under the training reductions.
- **Fraction columns:** the 36 one-eighth/one-half runs keep 600 updates, or 2,400 visits each. Label them **screening, not converged capacity results**. For the default corpus this is 16.667/4.167 passes. Select among full restart validations at updates 200, 400 and 600.

For the full-data column, normally score all 36 E-03 validation restart windows every **400 updates**. If P4-06's largest-variant pilot forecasts a load above the 160-hour cap on either machine, first switch full-data plateau checks to **12 restart windows**, one per validation case, before reducing seeds. Use the `t* = 100` restart for every case and freeze those window IDs and the validation mode before training. The cadence remains 400 updates; the Type C monitors never drive selection or stopping.

In the reduced mode, rank checkpoints by failed-window count, then mean fixed score across those 12 windows, then earlier update, using P3b-05's score definitions. At stopping, evaluate all 36 windows only for the **three best distinct checkpoints** under that 12-window ranking. Choose the final checkpoint by the full 36-window P3b-05 ranking. If numerical failure leaves fewer than three scored checkpoints, evaluate every available one and retain the failure record; do not substitute a fourth checkpoint based on full-ranking results. Fractional-data and secondary screening runs retain their three full validations at updates 200, 400 and 600.

Define plateau precisely, with N = 36 normally or N = 12 in the budget-triggered mode:

1. The evaluation at update 400 establishes the improvement anchor.
2. If the best-ranked checkpoint has fewer failed windows than the anchor, replace the anchor and reset patience. At an unchanged failure count F, calculate the plateau accuracy score as `q = (sum of the N ranking scores − 1e6 × F) / N`. Removing the constant failure sentinels prevents them from hiding improvements on completed windows; the denominator stays fixed. A reduction of at least 1% relative to the anchor's q replaces the anchor and resets patience. Smaller improvements accumulate against that same anchor, with `relative_improvement = (q_anchor − q_best) / max(q_anchor, 1e-12)`. Final checkpoint selection still uses the full 36-window failure-first P3b-05 ranking, restricted to the three finalists in reduced mode.
3. Stop after six consecutive scored evaluations without such improvement. The earliest plateau stop is update 2,800, or 11,200 visits. Otherwise stop at update 12,800. Retain the checkpoint selected by the applicable full-ranking procedure even if it predates the stop, and record whether plateau, visit cap or numerical failure ended the run.

Report accuracy and stability against parameters, multiply-accumulate operations (MACs) per cell, measured per-cell-step cost and training GPU-seconds. Every row includes the validation mode and restart-window IDs, visits and cumulative GPU-seconds at the selected checkpoint, total run cost and its stopping reason. Report training time separately from scored validation and monitoring time so their sum is auditable. Also compare saved checkpoints at matched training time; neither a capped nor a screening run is described as converged without qualification.

After selection, run all 12 cold-start validation cases once for each selected checkpoint, including screening rows, and report their failures without reselecting.

The secondary Lettuce sweep remains cheap: widths 12/24/48, full data, seed 11, 600 updates at batch 4, with the same three restart evaluations. Mark these three rows as screening; the fully trained 3b baseline remains separate.

**P4-06. Scaling compute cap.** Before scheduling, measure a largest-variant pilot on each machine, including forward/backward checkpoint recomputation, optimizer work, output writing and both 12-window and complete 36-window restart-validation passes. Let `M_train` be effective training MLUPS, counting each prescribed forward cell-step once while elapsed time includes backward/recomputation. Let `M_val` be 36-window restart-validation MLUPS, `M_plateau` be 12-window restart-validation MLUPS, `M_monitor` be Type C monitoring MLUPS, and `M_cold` be cold-start MLUPS with full validity certification. Both restart rates include their prescribed checks. Time all five on the largest variant; other variants may replace these conservative estimates only with their own measured pilot rates.

At the maximum visit budget:

| Budget plan | Full / screening runs | Training visits | 12-window / 36-window passes | Monitor passes | Hours by measured rate at U = 0.03 |
|---|---:|---:|---:|---:|---|
| Default | 33 / 39 | 1,783,200 | 0 / 1,173 | 1,173 | 13,001.0972/T + 6,150.0904/V + 821.0114/Q + 1,258.2951/C |
| First reduction, shorter plateau checks | 33 / 39 | 1,783,200 | 1,056 / 216 | 1,173 | 13,001.0972/T + 1,845.5514/P + 1,132.4975/V + 821.0114/Q + 1,258.2951/C |
| Second reduction, five unprotected seed rows removed | 32 / 35 | 1,722,400 | 1,024 / 201 | 1,129 | 12,557.8117/T + 1,789.6256/P + 1,053.8518/V + 790.2147/Q + 1,170.9135/C |

T, P, V, Q and C denote the five measured throughput rates M_train, M_plateau, M_val, M_monitor and M_cold respectively, in MLUPS. For F full and S screening runs, visits = 51,200F + 2,400S. Default full passes = 32F + 3S. Reduced mode uses 32F short passes and 3F + 3S full passes, charging finalists in full. Monitor passes = 32F + 3S. A full run has 12,800 / 400 = 32 monitor passes at the cap. A screening run has 3, at updates 200, 400 and 600. Cold starts = 12(F + S), hence 864 or 804. Rate coefficients equal counted cell-steps divided by 3.6 × 10⁹. A training visit is K × 49,152, a monitor pass 96K × 49,152, a short/full pass 12/36 × ceil(320/U) × 49,152 respectively, and a cold start ceil(3,200/U) × 49,152. At 0.03 use K = 534, 10,667 restart steps and 106,667 cold steps. For U = 0.025 use (640,12,800,128,000), and for 0.02 use (800,16,000,160,000). Recalculate each coefficient with that tuple. Charge setup and uncovered I/O once and measure actual early stops separately.

- The default and first reduction each use `32 × 33 + 3 × 39 = 1,173` monitor passes. Monitoring costs `1,173 × 96 × 534 × 49,152 / (3.6 × 10⁹ Q) ≈ 821.0114/Q` hours.
- The second reduction uses `32 × 32 + 3 × 35 = 1,129` monitor passes. Monitoring costs `1,129 × 96 × 534 × 49,152 / (3.6 × 10⁹ Q) ≈ 790.2147/Q` hours.

The cap is **160 GPU-hours per machine**, scheduled across both machines using their own measured pilot rates, with a 25% reserve on all forecast loops, including cold starts, plus measured pilot/setup and output overhead not already included in throughput. Assign ready runs in arm/radius/width/fraction/seed order to the device with the earliest predicted finish, one run per device; break ties by device ID. This allows eight weeks of roughly 20 scheduled GPU-hours per machine per week alongside other work. If the forecast exceeds either cap, first apply the 12-window plateau checks and full ranking of the three finalists from P4-01, then recompute both machine loads. If either cap is still exceeded, omit seed 33 only on unprotected width-192 stress rows: both smaller fractions at both radii, plus full data at R = 1. This removes five rows, from 69 to 64 primary. Preserve both paired arms at R = 0, full data, all four widths and three seeds. Dropping a protected row requires a recorded joint decision and disclosure of any lost inference. Keep every full-data run's 400-update cadence, 1% improvement threshold, six-evaluation patience and 51,200-visit cap unchanged. Record which reductions fired before training. If the second reduction still exceeds the cap, record a joint scheduling/resource decision; no further automatic seed, width or training-budget cuts. Measure throughput before assigning wall-clock hours: `[VERIFY]`.

**P4-05. Fixed scaling instrument.** Use Appendix B's Dellar basis `m = M f`. Keep the three conserved moments unchanged and relax all six non-conserved moments `(Pi_xx, Pi_xy, Pi_yy, N, Jx, Jy)`:

`m'_k = m_k − omega_k (m_k − m_eq,k)`,

`omega_k = 2 sigmoid(z_k + b_k)`, with `b_k = logit[1/(2 tau)] = −log(2 tau − 1)`.

- The declared default for **both stress and ghost moments** is the physical BGK rate `1/tau`. Thus `z = 0` reproduces BGK exactly in algebra. Compute b per cell from tau; it is not a trainable parameter. Zero-initialize the final layer so the initial operator is this baseline.
- Set `delta_f = M^-1(m' − m)`. Conservation is algebraic because the first three increments are zero; A-07 checks floating-point residuals.
- In exact arithmetic every rate is in (0, 2), so each isolated moment's relaxation factor `1 − omega` lies in (−1, 1), the classical range around rest. This is **not a nonlinear stability, positivity or viscosity guarantee**. Detect nonfinite values or finite-precision saturation at 0/2; never silently clip rates to rescue a run.
- At the rate-law level, Lettuce is a special case: fix stress deviations at zero and learn only ghost rates. For its `tau_ghost = 0.5 + exp(a)`, choose `z_ghost + b = −a − log(2)`. This makes the comparison of learned moment sets explicit; it does not claim the instrument's normalized inputs and six-output network reproduce the source's raw-moment MLP architecture.

- For the paired comparison, use the same two hidden layers, six biased outputs and initialization in both arms. Split raw outputs into triples a and b. Use stress deviations a and ghost deviations `b + tanh(a)` componentwise in the stress-capable model. In the ghost-only model set just the **applied** stress deviations to zero. This common parameterization leaves all six heads connected to the ghost rates, so both allocated and active parameter counts match. Simply discarding three trainable outputs would give the ghost arm fewer active parameters. At zero both recover BGK. Use the same map for the other stress-capable primary rows. Record the shared change of output coordinates from v0.3 and the fixed operation count in the run manifest. Verify each head’s effect away from initialization and stress rates exactly 1/τ in the restricted arm. Count the extra pointwise operations in measured timing.
- Keep the resolved Taylor–Green effective-viscosity diagnostic, because learned stress rates change viscosity. The operator remains an experimental instrument; final design stays open.

Keep the original network sizes and inputs:

- Two biased width-h rectified linear unit (ReLU) hidden layers and six biased outputs.
- R = 0: nine `(f − feq)/rho` channels and `log(tau − 0.5)`, giving 10 inputs.
- R = 1: nine population features at each of nine neighbouring cells, plus centre tau, giving `9×9 + 1 = 82` inputs.
- Use fixed training-only means/standard deviations, with standard-deviation floor `1e-6`, and A-13 boundary padding.

Recomputed parameter count is `h² + (n_in + 8)h + 6`; dense MACs per cell are `h² + (n_in + 6)h`.

| Width h | R = 0 parameters / MACs | R = 1 parameters / MACs |
|---|---:|---:|
| 4 | 94 / 80 | 382 / 368 |
| 32 | 1,606 / 1,536 | 3,910 / 3,840 |
| 64 | 5,254 / 5,120 | Outside the R = 1 sweep |
| 192 | 40,326 / 39,936 | 54,150 / 53,760 |

The parameter spans remain 429.0× and 141.8×. MAC counts exclude equilibrium, normalization, moment transforms, sigmoid and gathering; measured timing includes them all.

At 384 × 128, one FP32 width-192 activation uses 36 MiB. Two hidden fields for K = 534 would use `2 × 36 × 534 / 1,024 = 37.546875 GiB`. With segments of five steps the population endpoints use 182.25 MiB and one recomputed hidden block uses at most 360 MiB. At K = 640 or 800 the endpoints use (129 or 161) × 1.6875 = 217.6875 or 271.6875 MiB. These partial sums exclude gather, moment transforms, saved intermediates, optimizer and context. Measure the complete largest model’s update below 3.5 GiB on GTX 1650. Equivalent recomputation is allowed; preserve K and every required size.

**P4-07. Pre-registered analysis.** Before any P4 pilot, freeze this analysis, the paired initializations and subset hashes. Use only the protected full-data R = 0 rows and P3b’s full 36-window validation checkpoint ranking. Use identical case, seed, visit cap, plateau rule and validation mode across arms. Publish visits and matched-training-time sensitivity curves. Primary error is the arithmetic mean of the three unaligned E-02 restart errors within a case, with equal weight per case, seed and width. Report failures first. An incomplete required window or protected row precludes confirmatory support. Keep all rows and report censored outcomes.

- H1: estimate the mean paired difference (stress-capable minus ghost-only) over all four widths. Report differences at each width, active parameter counts and both arms’ paired differences from fixed base-rung TRT. Support H1 only if the upper limit of its paired 95% interval is below zero. A wholly nonnegative interval contradicts the predicted gain; an interval crossing zero is inconclusive.
- H2: for each arm fit ordinary least squares to log(mean validation error) versus log(active parameter count) at all four widths with equal weight per width. Report slope, slope difference, intercept, residuals and interval. Fit stress errors normalized by the same TRT error as a second curve, and show the horizontal TRT level. Define a credible power law in advance as a negative slope with upper 95% limit below zero, a span ≥ 100× and every fitted width within a factor 1.25 of its observed error. A nonnegative slope or a point outside the band contradicts the pre-registered form. A slope interval containing zero is inconclusive unless the form already fails. Report whether the between-arm slope difference excludes zero. Flat or better-than-TRT results are empirical outcomes.
- Use 10,000 paired bootstrap resamples, seed 6606. Within each of the three families sample its two validation geometries with replacement. Keep both Reynolds numbers and their windows together. Resample the three seed IDs as blocks shared across widths and arms. Repeat aggregation and fitting in each replicate and use percentile 2.5/97.5 limits. Keep deterministic TRT paired by case. Show the six-shape/three-seed limitation. A failed TRT row makes its paired ratio undefined. Report its coverage and keep all learned rows. Undefined or zero errors preclude the affected log fit; disclose them. Never use monitor loss, selected widths, side rows or test data to repair the fit.

**P4-02. Frozen selection.** Register 3b/adopted models, sizes, checkpoints, resolutions and all seed hashes before test; retain failures. Scaling promotion requires X-02, including retraining at comparable baseline budgets where needed.

**P4-03. Held-out runs.** Generate and qualify references from sealed configurations, unseal once with both humans present, and evaluate BGK, RBGK, TRT, 3b and every adopted entry on all 18 main-test cases through §8. Report the four family-transfer and twelve Re-extrapolation cases separately. Test data never becomes training data for this reporting cycle. Scaling instruments enter the headline only through X-02, including its same-rung classical guard.

**P4-04. Deliver evidence.** At minimum: per-case accuracy/forces table; stability horizon/Re-ladder plot; runtime/video-memory (VRAM) and error–cost curves; model-size/data-size plots; paired headline table on both GPUs; plots of the worst case and one failed case when any fails. Explain instability, no scaling, or no speedup without removing rows.

Milestones: scaling setup and plateau/budget checks 14–26 Partner-hours; sweep/analysis 12–20; held-out execution 6–10; efficiency reporting 6–10; Clau reference review 12–22 total. **Gate G4:** every scheduled primary row (69, or 64 after the recorded seed reduction) and three secondary rows is accounted for. Full-data rows have a plateau/cap/failure reason; screening rows are labelled. All 34 final main/transfer/extrapolation cases for every frozen method and seed are reported, including failures; E-12 evidence is complete, no split violation occurred, and all six evidence families regenerate. Positive improvement is not required.

G4 also requires the P4-07 result (including an inconclusive result), the selected branch (a), (b) or (c), both humans’ sign-offs, committed scope and an updated §18 row. Record the choice before learned 3D work.

**Reviewer self-check**

- Which paired rows identify a change in stress relaxation at equal active parameter count?
- What would falsify the proposed power law across the measured sizes?
- Why resample shapes and keep their Reynolds numbers together, and what uncertainty remains with three seeds?
- How do compute limits, multiple comparisons and unmatched cases constrain a headline?

Read [Kochkov et al.](https://doi.org/10.1073/pnas.2101784118) and [Ortali et al., kinetic subgrid modelling](https://doi.org/10.1103/PhysRevResearch.7.013202); compare the scope of their evidence with the much smaller scope here.

## 11. Testing, precision and reproducibility

**T-01. Required unit properties.** Test every lattice on CPU FP32/FP64, with CUDA counterparts before gates: isotropy/opposites; equilibrium moments/fixed points; conservation; tagged streaming; face/corner handling; unit conversion; restriction/lifting; halo equivalence; invalid-input rejection; deterministic IDs; differentiable-input immutability. Use seeded `rho∈[.95,1.05]`, `|u|≤.05`, `tau∈[.506,1.5]`, non-equilibrium perturbations and masks. Use 10,000 local states per operator at gates and 128 in continuous integration (CI). Add actual configured lower taus for higher-Re 3D pilots.

Normalize each local conserved residual by `max(rho,1e-12)` for mass and by `max(rho cs,1e-12)` for each momentum component; take maximum over cells and channels. Apply A-07 thresholds **after** all gating, limiting, projection and storage conversions. For equilibrium invariance use relative L2 ≤ `1e-6` FP32/`1e-12` FP64. These are numerical error budgets selected near floating-point precision while allowing reduction error, not literature benchmark bands.

**T-02. Symmetry tests.** Classical collision and lattice/geometry permutations must commute for all 8 D2Q9 square symmetries and 48 D3Q19 cubic symmetries to FP32 `1e-5` relative. Learned models declaring exact equivariance must pass the same test, including transformed memory and boundary features. Models not claiming equivariance still report symmetry error; it is not an additional design constraint. Rotate vector/population channels and spatial axes together. Uniform random rotation outside the lattice group is not an exact lattice symmetry.

**T-03. Differentiation.** On 8² periodic FP64 fixtures, compare directional autograd derivatives of a two-step loss with central finite differences at perturbation `1e-6`. Require relative error ≤ `1e-4` when derivative magnitude ≥ `1e-6`, otherwise absolute error ≤ `1e-8`. Verify nonzero gradients from every active loss term, including vorticity, and checkpointed/uncheckpointed gradient agreement within relative `1e-6`.

Project validation/evaluation and B1b preserve parameter, buffer, optimizer and normalization hashes. **B1a is the sole source-reproduction exception:** its source-labelled “testing” loop intentionally updates weights and is not validation evidence. A no-gradient path may share formulas but cannot invent a second solver.

**T-04. CI.** Every PR runs formatting/lint, schema validation and CPU pytest on small 8²/16² and 8³ fixtures, a short TGV test, contract guards, and touched-component regression tests. Use a locked Python/PyTorch CPU environment; record supported version bounds after testing, not “latest.” Target ≤ 10 minutes on GitHub Actions; a slow scientific gate is a separately recorded local run, not an excuse to skip CPU checks. Zero failing or unexpectedly skipped required tests. GPU availability is not assumed in Actions.

**T-05. Hardware qualification.** All 2D production/training recipes run on the 4 GB GTX 1650 with process peak ≤ 3.5 GiB; all 3D deployments on the 12 GB RTX 2060 with peak ≤ 10.4 GiB. Measure allocated, reserved and external/context memory; report limitations if the process meter is unavailable, and verify an actual complete run without an out-of-memory (OOM) error. Default FP32; FP64 is an oracle, not the performance comparator. Lower precision is a named exploration requiring new conservation and accuracy evidence. Do not assume mixed precision is faster on these GPUs.

**T-06. Reproducibility scope.** Save Python/NumPy/PyTorch CPU/CUDA random-number-generator (RNG) states, deterministic-algorithm flags, backend settings and thread count. Require bitwise CPU replay of tiny fixtures in a pinned environment. Cross-GPU FP32 replay compares metrics within declared tolerances, not bitwise identity. Release results come from clean commits. A dirty working tree may produce scratch runs tagged `research_eligible=false`; it cannot generate datasets, gate evidence or headline results.

**T-07. Regression discipline.** A correctness fix reruns affected unit/physics tests; a changed ruler follows E-08. Performance optimizations compare before/after at identical configurations and use paired timing. Never add a test that merely asserts a learned model beat a classical model; scientific outcomes belong in results, correctness properties in tests.

## 12. Phase 5 — D3Q19 and low-Re sphere

Owners: Clau for D3Q19, boundaries and validation. Partner owns training and deployment. Both approve results. P5-01 and P5-02 may begin after G3 alongside P4. At G4 record OD-24. Learned 3D work requires branch (a) and the classical sphere gate. Branch (c) uses P5-01, P5-02, their classical memory checks and SBX-04. Branch (b) uses the 2D completion rule at G5.

**P5-01. Generic-core check.** Enable D3Q19 through lattice data and 3D boundary modules. No 2D-specific rewrite of streaming, conservation, registry, storage or evaluation. Run 3D periodic equilibrium/streaming and an extruded 2D TGV (constant in z, uz=0) with tau=0.8; velocity decay error ≤ 1%, max uz ≤ `1e-6`. At least one 3D CPU/CUDA contract fixture must pass.

**P5-02. Sphere case.** Fixed sphere diameter D at origin; domain `[-8D,16D]×[-8D,8D]²`, uniform inlet, A-12 acoustic outlet, free-slip transverse faces and stationary sphere, using A-12's face/corner rules. Use U_lu=0.03, Re `{20,50,100}` and acoustic parameter conversion. These Re values lie in the steady regime studied by [Johnson & Patel](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/flow-past-a-sphere-up-to-a-reynolds-number-of-300/47906D7124155BF7F14833133FB854F8). The finite-domain starting dimensions are informed by [MFIX-Exa's sphere tutorial](https://mfix.netl.doe.gov/doc/mfix-exa/guide/latest/tutorials/fluid/steady-flow-around-sphere.html); its unconverged numerical drag sequence is not adopted as truth.

Compare measured `CD=Fx/(rho U∞² (pi D²/4)/2)` to Schiller–Naumann `CD=24(1+.15 Re^.687)/Re`, whose low-Re branch is documented in [OpenFOAM's implementation](https://cpp.openfoam.org/v13/SchillerNaumannDragForce_8C_source.html). Evaluated values are 2.60955, 1.53810, 1.09173 for Re 20, 50, 100, respectively, calculated from that correlation. It is an empirical unconfined-sphere correlation, not an exact solution.

Run the BGK diameter ladder **8/12/16**, independently rasterizing the same analytic sphere. Run to at least `t*=100`, at most 300; convergence requires mean drag change ≤ 0.5% over three consecutive 20-unit windows and normalized velocity change `sqrt(sum V|u_end−u_start|² / max(sum V|u_end|²,1e-12 U² sum V))≤1e-4` in each window. Gate at each Re: D = 12 and D = 16 CD within 10% of the correlation, D = 12→D = 16 change ≤ 5%, transverse force ≤ 1% of drag, no invalid state. Report D = 8→D = 12 too; do not infer a convergence order from non-monotone voxel errors. At each Re repeat **both D = 12 and D = 16** on `[-10D,20D]×[-10D,10D]²`, requiring original-to-expanded drag change ≤ 3% at each diameter. This directly separates voxel refinement from finite-domain error at the finest rung. Failure leaves the sphere gate failed rather than shrinking the domain or relaxing tolerances.

**P5-03. Memory and run arithmetic.**

- Use the memory-reduced classical path for the sphere ladder. Two FP32 population buffers use 152 bytes per cell, four macroscopic channels use 16, and two masks use 2: **170 bytes per cell**, plus 0.75 GiB for tiled scratch/context.
- Match the standard path within A-08. Retain no full-grid equilibrium; obtain geometry sparsely or on demand.
- Learned deployment uses 270 bytes per cell: three population buffers (228), eight work channels (32), signed-distance/tau fields (8), and masks (2). Reserve another 1.25 GiB for tiled activations/context.
- These planning values target the 12 GB RTX 2060 with a 10.4 GiB process cap (10.4/12 ≈ 86.7% on nominal capacity). Use measured device capacity and process peaks. Assume 336 GB/s bandwidth for throughput planning [VERIFY]. The larger capacity changes which domains fit. No increase in MLUPS is assumed.

| Sphere D / grid | Cells | Classical GiB including 0.75 GiB reserve | Learned GiB including 1.25 GiB reserve | Steps for t*=100 /300 |
|---|---:|---:|---:|---:|
|8 /192×128×128|3,145,728|1.248047|2.041016|26,667 /80,000|
|12 /288×192×192|10,616,832|2.430908|3.919678|40,000 /120,000|
|16 /384×256×256|25,165,824|**4.734375**|**7.578125**|53,334 /160,000|

At D = 16 the classical ordinary grid uses `25,165,824 × 170 / 2³⁰ + 0.75 = 4.734375 GiB`. Learned deployment there uses `25,165,824 × 270 / 2³⁰ + 1.25 = 7.578125 GiB`. Expanded classical D = 12 (360 × 240 × 240) uses `20,736,000 × 170 / 2³⁰ + 0.75 = 4.033024 GiB`. Expanded D = 16 (480 × 320 × 320) uses `49,152,000 × 170 / 2³⁰ + 0.75 = 8.531982 GiB`. Both D = 16 paths fit on paper. Verify measured fit on the actual target. Tile activations: a single 32-channel FP32 field at 192³ is 0.84375 GiB.

With measured throughput M MLUPS, steps are `ceil(t* D_lu/.03)` and ideal loop hours are `Ncells×steps/(3.6e9 M)`. Original-domain D = 8/D = 12/D = 16 each require respectively `(23.30198–69.90507)/M`, `(117.9648–353.8944)/M`, `(372.83168–1118.48107)/M` hours over t*=100–300; multiply by three Re and add expanded-domain runs. M and end-to-end runtime are `[VERIFY]` until a same-grid pilot includes boundaries/output costs. Human effort below excludes unattended simulation time.

At all three Re the ladder and both extensions require 3 × (3 + 2) = 15 classical trajectories. Each expanded D = 12 run costs (230.40–691.20)/M hours and D = 16 costs (728.18688–2,184.53333)/M, with M measured separately at each size. Branch (a) also measures a D = 16 ordinary-domain learned Re 20 deployment through t* = 100 before claiming measured fit: `25,165,824 × 53,334 / (3.6 × 10⁹ M_learned) = 372.83168/M_learned` hours. Keep D = 12 as the mandatory frozen transfer comparison.

**P5-06. Nontriviality pilot before learning.** Use the periodic field and phase splits in P5-04. Test multipliers `lambda = {1,2,4}` in that order. Training Re is `lambda × {200,400}`, validation Re is `lambda × {300,600}`, and held-out periodic test Re is `lambda × {500,800}`.

For each training and validation trajectory:

- Coarse 32³ BGK is **nontrivial** if it either fails within `t* ∈ [0,2]` under E-06, or completes with velocity error ≥ 5% against restricted 96³ reference fields. For completed runs use 101 aligned observations and the E-02 spacetime norm.
- In either branch, **32³ RBGK must complete the full horizon with valid finite states**. This supplies a stable classical comparator; coarse BGK divergence alone is insufficient.
- The 96³ reference must remain valid and qualify against 160³ at ≤ 1% velocity spacetime error and ≤ 2% kinetic-energy-history error.
- Record `coarse_bgk_diverged` or `coarse_bgk_error_ge_5pct` for every trajectory, with the failure step/reason or measured error. A divergent run has no fabricated terminal error.

Choose the first multiplier for which **all four training and both validation trajectories** pass these rules. Freeze it before fitting; no learned or held-out test score selects lambda. The plumbing fallback below is unchanged.

Adding RBGK checks at most `3 multipliers × 6 trajectories = 18` coarse runs. With the base stop `ceil(2 × 32 / 0.03) = 2,134`, they add at most `18 × 32³ × 2,134 = 1,258,684,416` cell updates, or `0.349635/M_RBGK` hours, where throughput is in MLUPS and includes the prescribed checks. This is a small addition to the existing 96³/160³ reference work, not a measured runtime.

For Re=UL/nu and U_lu=0.03, `tau_N=.5+.09 N/Re`. At lambda=1:

| Re | tau 32 | tau 96 | tau 160 |
|---|---:|---:|---:|
|200|0.5144|0.5432|0.572|
|300|0.5096|0.5288|0.548|
|400|0.5072|0.5216|0.536|
|500|0.50576|0.51728|0.5288|
|600|0.5048|0.5144|0.524|
|800|0.5036|0.5108|0.518|

For lambda 2/4 divide each table entry's excess above 0.5 by 2/4. Classical 96³/160³ memory is `N³×170/2³⁰+.75` =0.890076/1.398499 GiB; actual fit and stability still require measurement. The fine grids therefore fit the 12 GB plan without assuming the high-Re references qualify.

If none passes, retain all pilot results and freeze the original Re `{20,40}` /`{30,60}` /`{50,100}` splits as **dimensional-plumbing only**, with the same reference qualification. Here tau 32 ranges 0.5288–0.644 and the data may teach little beyond BGK. The phase/release must then say it demonstrates 3D conservation, training and deployment, not successful learning of nontrivial 3D coarse dynamics. Never lower 5% or loosen reference tolerances to manufacture that claim. A later redesign requires a fresh entry and holdout.

**P5-04. 3D data and training.** Train new 3D weights on periodic vortices, then measure transfer to the sphere. Use `[0,L]³`, base 32³, reference 96³, U_lu=0.03, rho=1 and equilibrium initialization with `u=(U sin X cos Y cos Z,−U cos X sin Y cos Z,0)`, `X=2pi x/L+phi_x` and similarly Y, Z; `t*=t U/L`, horizon 2. This is a divergence-free initial field, not an analytic 3D decay law. Training phase triples are `{(0,0,0),(pi/4,pi/4,pi/4)}` (four trajectories), validation `(pi/2,pi/4,0)` (two), test `(pi/2,pi/2,pi/2)` (two), using P5-06's frozen Re values. Hash seeds/splits under `3d-v4`; no trajectory feeds 2D selection. Qualify test references 96³ against 160³ automatically after checkpoint freeze, with P5-06's limits. Failed test qualification is reported as unavailable evidence, never repaired by retraining on that test.

Generate 8,000 training patches (2,000/trajectory), 1,000 validation (500/trajectory); choose uniform integer starts whose K-step endpoint is ≤ 2. Interior 8³, K=2, R ≤ 1, h=4, P=16, periodic wrap. Payload=`9,000×(311,296 f0+24,576 targets+36,864 geometry)/2³⁰=3.12424 GiB`, before masks/metadata, within 4 GiB. Optional all-fluid geometry defaults must be declared. Retain 101 coarse rho/j frames at Δt*=0.02 and three coarse lifted restarts at 0.25, 0.75, 1.25; discard fine fields. Four evaluation cases need `4×(101×.5+3×2.375)/1024=.22510 GiB`, within the 2 GiB 3D reference allowance.

Freeze a 3D adaptation entry before coding: select the 2D validation-best architecture, or 3b if none was adopted; document 3D channels, moment basis if used, receptive radius and parameter count. Keep conservation/locality/memory constraints; this is not an original Lettuce 3D replication. Use Adam lr `3e-4`, 50 epochs, effective batch 32 via microbatches 1–4, gradient clipping 1, seeds 11/22/33 and normalized velocity loss averaged over both rollout steps. Evaluate every five epochs on both full periodic validation trajectories; choose fewest failures, then smallest primary error with failures scored worst, then earliest epoch. Require the lower-Re validation trajectory to complete for every seed; harder failures stay visible. Test data never selects or repairs a checkpoint.

**P5-05. Explicit 3D evaluation profile.** Reuse E-02/E-05/E-06 metric formulas and E-12 synchronization/repeat methodology, not the 2D campaign counts, geometry masks or selection ladder:

| Item | Fixed 3D setting |
|---|---|
| Periodic generalization | Both periodic test trajectories; 32³; three restart windows of length `.25` starting at `.25,.75,1.25`; observations every `.02`; cold horizon 2; compare to qualified 96³ reference. |
| Full sphere transfer | Re 20 is the development smoke case; Re 50/100 are frozen final transfer cases. Use D = 12; D = 8 is an optional additional cost row. No sphere fitting or checkpoint selection. Sphere-centre shift is zero; methods at a resolution share its geometry. Compare classical D = 8/12/16 convergence separately. |
| Sphere horizon/observations | Cold start to `t*=100`; report mean drag over `[80,100]`, force every step, full velocity snapshots only at 80, 90,100 and an accumulated late mean field. No oracle restart and no full fine sphere trajectory. |
| Sphere accuracy meaning | Drag discrepancy against Schiller–Naumann and against validated same-grid BGK/RBGK/TRT; transverse force and conservation. Velocity difference against same-grid classical results is labelled **model discrepancy**, never fine-reference error. No 3D matched-accuracy efficiency claim is made without a separate qualified fine velocity reference. |
| Regions | Full fluid domain; sphere-near distance ≤ 2D; wake `x∈[D/2,8D]` and `y²+z²≤(2D)²`, in sphere-centred coordinates; no removed guard strips. |
| Cost/seeds | RTX 2060, FP32, three training seeds, five timing repeats, peak ≤ 10.4 GiB; BGK/RBGK/TRT same-grid cost reported separately. No mandatory 3D run on GTX 1650. |
| Storage | Three sphere rho/j snapshots plus one mean field per method/case are streamed to release-selected images or summary reductions; retain only reference/representative fields. Cap all 3D reference/field evidence at 2 GiB within the 24 GiB allocation. |

Evaluate BGK, RBGK, TRT and at least one trained conservative operator on both periodic tests and both final sphere-transfer cases. At least one selected learned operator must complete both sphere cases to `t*=100` for all three seeds on the validated grid within 10.4 GiB; errors may be worse than classical and must remain visible. A periodic demo alone is not the endpoint. If transfer fails, record that result and explore only on the declared Re 20 development sphere; any subsequent sphere-informed redesign requires a fresh transfer holdout before a generalization claim.

Milestones: generic-core/face tests 6–10 Clau-hours; sphere validation including the D = 16 extension 18–30; memory path 8–12; pilot/data 8–14 shared; training and D = 16 fit review 11–18 Partner; deployment/analysis 8–12 shared. **Gate G5.** Branch (a): P5-01/P5-02 pass, full-grid memory fit is measured, references qualify, and all mandatory comparisons/finite sphere rollouts exist. Record whether P5-06 passed the nontriviality gate or invoked the explicitly labelled plumbing outcome; the latter is a negative research outcome, not a claim of 3D coarse-learning success. No positive speedup is required. Sphere fine-reference velocity accuracy remains outside supported claims.

For branch (b), register one extended 2D growth cycle at G4 with an X-01 entry, fixed budget, paired classical/learned comparison, time box, intended artifact and kill criterion. Complete the entry, report all attempts and review what was learned. Use a fresh jointly committed holdout for any test-informed claim under X-04. Record a negative outcome if appropriate. For branch (c), pass P5-01 and P5-02 including both direct domain checks, verify classical process fit and complete SBX-04 with its exported visualization and failure records. Label it a reduced classical 3D demonstration. For each branch link the appropriate G5 evidence before G6.

**P5-S. Stretch only.** After G5, an Ahmed-like simplified body may be tested at Re ≤ 100 using body length as characteristic scale. Before running, record geometry dimensions, slant, clearance, boundary conditions and reference strategy in an exploration entry; no road-vehicle drag coefficient is used as a low-Re target. This optional entry is capped at 16 combined human-hours and cannot delay G6. If no validated reference exists, label it a qualitative low-Re demonstration and omit quantitative accuracy claims.

**Reviewer self-check**

- What isotropy checks change from D2Q9 to D3Q19?
- Why does sphere drag use projected area, and how do the two domain checks separate blockage from voxel refinement?
- Which parts of memory scale with cells and which with live activations?
- Which G4 branch supports a learned 3D claim, and which reference would that claim require?

Read [Krüger Chapters 10,11,13](https://link.springer.com/book/10.1007/978-3-319-44649-3), the sphere references above and [Hecht–Harting](https://arxiv.org/abs/0811.4593).

## 13. Phase 6 — Reproducible results and README

Owner: both. Reporting scaffolding begins after G3; interim 2D release follows G4; final G6 still requires G4 and the G5 evidence for the recorded branch.

**R-01. Simple experiment records.** Use configs, JSON and comma-separated-value (CSV) tables; TensorBoard is optional and not authoritative. Each run has `run_id`, full clean commit, SDD/ruler/config/dataset/split hashes, parent run if resumed, seeds/RNG state, device model/VRAM/driver, CPU, random-access memory (RAM), operating system (OS), Python/PyTorch/CUDA versions, precision, threads, start/end UTC, elapsed time, model manifest/checkpoint SHA256, dataset IDs, step/time schedule, failure/censoring reason and output hashes. Each metric row includes case, model, seed, resolution, physical units, observation interval, reference ID and eligibility. Every efficiency comparison also stores the E-13 same-resolution learned/BGK cell-step cost ratio, comparator/BGK cost ratio, acoustic break-even ratio, timing profile, E-12 execution-path provenance and initialization inclusion flag. Training rows store selected-checkpoint visits and GPU-seconds, total visits/time and stopping reason. Null means undefined and includes a reason; never encode failure as zero error.

**R-02. Layout.** Track `configs/{validation,data,training,evaluation,scaling}/`, `src/`, `scripts/`, `tests/`, `scripts/sdd_check.py`, `sandbox/learning/` for small tracked L-01/L-02 code/derivations, this SDD, README, LICENSE and small curated `results/<release>/{manifest.json,metrics.csv,tables/,figures/,gates/}`. Keep large `data/`, `checkpoints/`, `runs/`, temporary figures and TensorBoard logs out of git. Published result tables are intentionally tracked evidence, not ignored transient logs. Checkpoints/datasets live in a versioned external archive with download URL and SHA256 in the release manifest; provide regeneration if archive availability changes. No secrets or machine-private paths enter public configs.

Production `src/` must never import `sandbox/learning/`. Keep the human-written learning solver isolated. Link monthly figures or short videos to their configs and label their evidence status.

**R-03. Config completion.** Resolve all defaults into the typed config below before execution; device selection never changes numerical parameters. Resume rejects mismatching core hashes. Source/sandbox runs explicitly set `evidence=false` for project-ruler eligibility; B1/B2 fidelity records may satisfy only their named gates.

Canonical JSON field names/types are fixed as follows; typed records from §2 serialize as objects with those same field names. Optional fields must be explicit null; JSON floats are finite double-precision values under the Institute of Electrical and Electronics Engineers (IEEE) 754 standard before tensor conversion.

| Config | Additional required fields |
|---|---|
| All configs | `schema_version:str`, `config_id:str`, `sdd_commit:str`, `seed:uint64`, `evidence:bool`, `device:Literal["cpu","cuda"]`, `dtype:Literal["float32","float64"]`, `extensions:dict[str,JSON]`. Lower-precision entries register explicit dtype/version. |
| `CaseConfig` | `case_id:str`, `split:Literal["train","validation","test","transfer","extrapolation","physics","sanity","sandbox"]`, `lattice_name:str`, `base_shape:list[int]`, `resolution_factor:int`, `units:Units`, `reynolds:float`, `reference_speed:float`, `reference_length:float`, `tau:float`, `origin:list[float]`, `geometry:{generator:str,parameters:dict[str,JSON],seed:uint64,sha256:str}`, `body_id_order:list[str]`, `initialization:{kind:Literal["rest","equilibrium-field","lifted"],field_id:str\|null,snapshot_id:str\|null}`, `boundaries:BoundaryPlan`, `force:{kind:Literal["guo_bgk"],density_lu:list[float]}\|null`, `stop_step:int`, `observation_steps:list[int]`, `reference_case_id:str\|null`. Speeds/lengths/origin are physical; tau dimensionless. Constant force vectors have d entries. |
| `TrainConfig` | `operator:OperatorSpec`, `operator_parameters:dict[str,JSON]` validated against its registered model schema; `dataset_manifest:str`, `required_features:list[str]`, `normalization:{kind:str,training_statistics_sha256:str\|null}`, `loss:{id:str,weights:dict[str,float],reduction:Literal["mean","sum"]}`, `optimizer:{name:str,learning_rate:float,parameters:dict[str,JSON]}`, `scheduler:{name:str,parameters:dict[str,JSON]}`, `microbatch:int`, `accumulation_steps:int`, `epochs:int`, `max_steps:int\|null`, `rollout_steps:int`, `gradient_clip:float\|null`, `selection_rule_id:str`, `training_cohort_sha256:str`, `window_fraction:float`, `epoch_basis:Literal["corpus","virtual-visits"]`, `visits_per_virtual_epoch:int\|null`, `max_window_visits:int\|null`, `selection_update_steps:list[int]`, `monitor_update_steps:list[int]`, `plateau:{anchor_relative_improvement:float,patience_evaluations:int,score_floor:float}\|null`, `training_seeds:list[uint64]`, `checkpoint_directory:str`. |
| `EvalConfig` | `ruler_sha256:str`, `profile:Literal["2d-v4","3d-v4","source-reproduction","sandbox"]`, `methods:list[{operator_id:str,checkpoint:str\|null,sha256:str\|null,resolution_factor:int}]`, `case_ids:list[str]`, `restart_steps:list[int]`, `restart_length_steps:int`, `cold_stop_step:int`, `mask_definition_id:str`, `validity_rule_id:str`, `timing_repeats:int=5`, `timing_attempts_max:int=3`, `diagnostic_interval:int`, `timing_mode:Literal["core-output","with-diagnostics"]`, `timing_batch:int`, `cuda_graph:bool`, `warmup_steps:int`, `cpu_threads:int`, `output_directory:str`. Resolve physical durations to integer schedules before hashing; execute mixed grid sizes separately. |

For project 3b, virtual epochs contain 1,024 visits and the cap is 51,200. For P4 full-data runs, use the explicit P4-01 selection schedule and plateau fields; fractional and secondary screening runs set plateau to null. Expand all schedules and freeze the training cohort before hashing. Source recipes keep their source-specific epoch basis.

Schema validators enforce positive dimensions/timesteps, `tau>.5`, consistency of physical Re/nu/units within `1e-12` relative, sorted unique in-range observation steps, and compatible boundary faces. A model's private parameter dictionary is the intended exploration seam, not permission to add unvalidated solver or evaluator parameters.

**R-04. Script contracts.** Provide entry points for validation, dataset generation/verification, training, evaluation, scaling, plotting and complete report regeneration, each accepting a config path, output path and device. The command-line interface (CLI) names and exact commands are recorded in README once implemented. Plotting only reads immutable result tables and cannot rerun selection or smooth away failures. Every table/figure embeds or accompanies its producing config/run IDs. No manually edited numerical table is a release source.

**R-05. README.** Approximately 800–1,500 words plus figures: purpose/non-goals; installation and CPU/GPU instructions with measured memory; SDD/config/data/model links; 2D results on both GPUs; replication/reference distinctions; coverage and selection/voxel limitations; “what we tried,” including failures; authors/contributions; MIT license and attribution. State “no demonstrated gain” when appropriate; never headline one favourable case.

If 3b completes fewer validation cases than RBGK at the base rung, state this prominently next to the headline table, with completion counts for each seed and the fixed denominator. Results must show 3b, BGK, RBGK and TRT coverage together. Explain that an improvement over 3b alone is insufficient for adoption; report the same-rung classical guard from X-02.

**R-06. Interim public 2D release.** After G4, both humans review an annotated public `v0.x` tag with MIT license, README, authors/contributions, reproducible 2D configs/data links and G0–G4 results, including negative outcomes. Run a clean-checkout smoke test and regenerate 2D tables. README states the G4 branch and its outstanding evidence; sandbox appears only under “what we tried.” This is a presentable release, not final completion. Budget 2–4 hours each.

Milestones: R6.1 report scripts 4–8 each; R6.2 regeneration 4–6 each; R6.3 final release 2–4 each. **Gate G6:** all published tables/figures regenerate; another human completes clean-checkout CPU smoke and one held-out GPU evaluation within tolerances; contributions, MIT/public status and gate links verified; zero secrets/large artifacts in git. Resolve supporting `[VERIFY]` items or omit affected claims. The recorded branch’s G5 completion evidence is mandatory.

**Reviewer self-check**

- Which run and config produced each figure, including negative results?
- What can a clean checkout reproduce across different GPUs?
- Does every public claim have the complete denominator and its branch-specific gate evidence?

Review [PyTorch reproducibility guidance](https://docs.pytorch.org/docs/stable/notes/randomness.html) and compare each README claim to its complete table.

## 14. Prior work and limits of novelty

The core idea is substantially established. A valid outcome is replication plus careful low-memory obstacle-flow evaluation. No seed below is called unconditionally new.

| Verified work | What it establishes | What this project uses or may add |
|---|---|---|
| Corbetta et al., *Toward learning Lattice Boltzmann collision operators*, European Physical Journal E 46, 10 (2023), [paper](https://doi.org/10.1140/epje/s10189-023-00267-w), [code](https://github.com/agabbana/learning_lbm_collision_operator) | Learns D2Q9 BGK collision from synthetic examples; investigates normalization, symmetry and conservation. | Precedent for 3a and constraints. It is not evidence that imitation alone improves coarse flow. |
| Bedrunka et al., *Lettuce: PyTorch-Based Lattice Boltzmann Framework* (2021), [paper](https://doi.org/10.1007/978-3-030-90539-2_3), [repository](https://github.com/lettucecfd/lettuce) | Differentiable PyTorch LBM and a small learned higher-moment collision example. |3b replication plus explicitly corrected/adapted training. Its framework also provides independent solver checks. |
| Kochkov et al., *Machine learning–accelerated computational fluid dynamics*, Proceedings of the National Academy of Sciences 118 (2021), [paper](https://doi.org/10.1073/pnas.2101784118), [code](https://github.com/google/jax-cfd) | Learns local coarse-grid numerical corrections inside a conventional computational fluid dynamics (CFD) solver with unrolled training. | Methodological precedent for coarse targets and rollout losses, not an LBM operator replication. Its hardware/speedups are not transferred to these GPUs. |
| Ortali et al., *Enhancing lattice kinetic schemes for fluid dynamics with Lattice-Equivariant Neural Networks*, American Institute of Aeronautics and Astronautics (AIAA) Journal 63 (2025), [paper](https://doi.org/10.2514/1.J064453), [preprint](https://arxiv.org/abs/2405.13850) | Built-in lattice equivariance for learned collision, including 2D/3D examples. | Direct precedent for symmetry by construction; a new comparison on this ruler is not invention of equivariance. |
| Ortali et al., *Kinetic data-driven approach to turbulence subgrid modeling*, Physical Review Research 7, 013202 (2025), [paper](https://doi.org/10.1103/PhysRevResearch.7.013202), [preprint](https://arxiv.org/abs/2403.18466) | Local conservative learned LBM collisions trained from fine turbulence data. | Strong direct overlap with the project's central intuition. Possible added evidence is obstacle/Re generalization, failure accounting and same-GPU cost on the 4 GB and 12 GB devices. |
| Horstmann, Bedrunka & Foysi, *Lattice Boltzmann method with artificial bulk viscosity using a neural collision operator* (2024), [paper](https://doi.org/10.1016/j.compfluid.2024.106191) | Learns local relaxation behaviour against a higher-order Navier–Stokes reference. | Local adaptive stabilization already has precedent; compare rather than claim it as new. |
| Lehmann et al., *Accuracy and performance of the lattice Boltzmann method with 64-bit, 32-bit, and customized 16-bit number formats*, Physical Review E 106, 015308 (2022), [paper/preprint](https://arxiv.org/abs/2112.08926) | Studies reduced distribution storage with higher-precision arithmetic. | Mandatory classical precision comparator for EXP-07; bandwidth savings alone are known. |
| *Physics informed data-driven near-wall modelling for lattice Boltzmann simulation of high Reynolds number turbulent flows* (2024), [paper](https://www.nature.com/articles/s42005-024-01832-1) | Data-driven wall modelling is established in LBM. | Related precedent for EXP-05, but a turbulent wall model is not identical to conditioning this low-Re conservative collision on local geometry. |
| *Machine-learning-enhanced collision operator for the lattice Boltzmann method based on invariant networks* (2025), [paper](https://doi.org/10.1103/rbf2-p8tf) | Combines invariant neural inputs with equivariant collision and learned nonphysical relaxation. | Further direct precedent for symmetry and dimensional collision extensions; neither is presumed novel here. |
| *MoE-Bolt* (2025), Computer Physics Communications 310, 109540, [paper](https://doi.org/10.1016/j.cpc.2025.109540) | Mixture-of-experts prediction of velocity sequences from LBM-generated data. | Adjacent conditional-compute precedent; not the same as hard dispatch between conservative collision rules. |
| Lions, Maday & Turinici, Parareal (2001), [original](https://hal.science/hal-00798372v1/document); Ibrahim, Götschel & Ruprecht (2023), [learned coarse propagator](https://arxiv.org/abs/2303.03848) | Coarse/fine temporal correction and learned-coarse variants. | “Speculative physics” is a known family; single-GPU advantage must be measured, and temporal algorithms are outside the core collision interface. |

Searches were checked on 20 October 2026. Absence of an exact search hit is weak evidence, not a novelty certificate. Before a public “new” claim, update the same entry's search record and compare equations/experiments, including recent work. This document establishes neither patentability nor exhaustive literature coverage.

## 15. Exploration log: ranked initial menu

Rank reflects expected information gained per student-hour on the stated hardware, not expected publication novelty. All entries currently have status **proposed**, result **not run**, PR **none**. An assigned owner is accountable for an experiment, not a commitment to adopt its architecture. Every entry below is an independent candidate; the final operator remains undecided.

SBX-01–05 belong to B3 and carry `evidence=false`. They may nominate later experiments. Use pinned B1b source fixtures unless a different fixture is named, and record seeds, split/window IDs and corrections.

### SBX-01 — Does the network beat a constant?

- **Owner / time box / evidence:** Partner / 4–8 hours / `false`.
- **Hypothesis:** State-dependent ghost relaxation may add little on the source shear layer. Use A-15 TRT at Λ = 3/16 as the primary zero-fit constant baseline on the identical periodic fixture. Also replace the two MLPs with three learned scalars `tau_a=.5+exp(s_a)`, keeping shear tau fixed; fit the same data/loss/horizon/optimizer. Include a hand-selected constant-rate control: choose common ghost tau from `{.6,1,1.5}` by training error only, record all three trials and freeze before evaluation.
- **Expected movement:** determine whether 530 parameters reduce source velocity error by ≥ 10% versus both zero-fit TRT and the 3-parameter model.
- **Cheapest kill test:** seed 11; compare the source's final 4,000-step velocity sum-of-squares and eight frozen 100-step evaluation pairs. Kill the hypothesis of useful neural dependence if the network fails to beat each of TRT and the 3-scalar model by ≥ 10% at the final state or cannot complete the same horizon. A surviving hypothesis only nominates an EXP entry.
- **Prior-work label/search:** **Known ablation family; exact source comparison partially explored.** Searched `"Lettuce" "constant" "relaxation" neural` and `"neural collision" relaxation Lettuce`; [Dellar's MRT formulation](https://people.maths.ox.ac.uk/dellar/papers/incompLB.pdf) supplies constant ghost rates, and [Lettuce](https://arxiv.org/abs/2106.12929) supplies learned rates. No verified exact 3-scalar ablation was found; this is not a novelty claim.
- **Status / result / PR:** proposed / not run / none.

### SBX-02 — Clean re-evaluation of the published result

- **Owner / time box / evidence:** Partner / 4–8 hours / `false`.
- **Hypothesis:** Removing temporal interleaving and test-time optimization may change the apparent gain. Fix seed 11; use the first 32 chronological 100-step pairs for training and the last 8 for testing, with no shared target interval, no test updates and no hyperparameter choice on testing. Shared trajectory history remains a disclosed limitation.
- **Expected movement:** measure the fraction of source-case velocity-error improvement over both BGK and RBGK that survives; either sign is informative.
- **Cheapest kill test:** train once under B1b's corrected 50-epoch recipe with this split, freeze weights, and report all eight late-window errors plus the 4,000-step comparison. Kill any robust-improvement claim if the network fails a horizon either classical comparator completes or its late-window error is no lower than either comparator. Completion requires every row, even with no surviving gain.
- **Prior-work label/search:** **Known evaluation practice; source-specific audit.** Searched `"Lettuce" "temporal leakage"` and `"neural collision" "time" "split"`; no direct clean re-evaluation was verified. The [released script](https://github.com/lettucecfd/lettuce-paper/blob/main/02_neural_collision_model/script.py) confirms randomized interleaving and optimizer updates, making this a correction audit rather than a new operator.
- **Status / result / PR:** proposed / not run / none.

### SBX-03 — Transfer

- **Owner / time box / evidence:** Partner / 4–8 hours / `false`.
- **Hypothesis:** Source-trained rates may lose their benefit when viscosity or rollout horizon changes. Freeze B1b's Re 5,000 weights; evaluate the same periodic geometry at Re 2,000 and 10,000, Ma 0.05, for 4,000 and 8,000 coarse steps, with matched 128² fine references and BGK/RBGK controls. No retraining.
- **Expected movement:** locate where source velocity-error improvement falls below 10% or the learned stable horizon becomes shorter than a classical control.
- **Cheapest kill test:** run Re 2,000/10,000 to 4,000 steps first; stop a divergent trajectory and record its first failure, otherwise extend to 8,000. Kill a transfer claim for any row lacking ≥ 10% error improvement over the best finite classical control; retain every failed/unqualified reference as such.
- **Prior-work label/search:** **Known.** Searched `"Lettuce" "neural" "shear" "turbulence"` and `"Toward learning Lattice Boltzmann collision operators" "Reynolds"`; [Lettuce](https://arxiv.org/abs/2106.12929) already transfers shear-trained rates to decaying turbulence, and [Corbetta et al.](https://doi.org/10.1140/epje/s10189-023-00267-w) test other flow/Re settings. This is a bounded transfer audit.
- **Status / result / PR:** proposed / not run / none.

### SBX-04 — 3D Taylor–Green in Lettuce

- **Owner / time box / evidence:** Partner, 2–6 hours, `evidence=false`.
- **Hypothesis and measurement:** On a periodic 128³ Taylor–Green vortex, compare BGK and RBGK from identical states. Start at Re 400, double Re until the first observed instability or the box expires. Fix a two-convective-unit horizon, report maximum speed, first invalid step or censored horizon, and whether RBGK survives at the first failing BGK level.
- **Memory and artifact:** Two D3Q19 FP32 population buffers occupy `128³ × 19 × 4 × 2 / 2³⁰ = 0.296875 GiB`. Record the entire Lettuce process peak separately. Export a vorticity slice or isosurface as VTK for ParaView.
- **Cheapest kill test / prior work:** Complete the Re 400 pair, verify finite fields and export. Stop at the time limit or first unresolved implementation failure. Label **Known**, a teaching demonstration using the [Lettuce solver](https://github.com/lettucecfd/lettuce).
- **Status / result / PR:** proposed / not run / none.

### SBX-05 — Low-Re car silhouette

- **Owner / time box / evidence:** Clau, 2–6 hours, `evidence=false`.
- **Hypothesis and measurement:** Rasterize one documented 2D car silhouette in free stream with free-slip outer walls and no ground plane. Compare BGK/RBGK/TRT at D = 16, 32 and 48 at Re 100 using the same projected length convention across all nine rows. Report force traces, failures and a wake image. After freeze, add any frozen learned models as labelled transfer demos with no tuning.
- **Cheapest kill test / prior work:** Start at D = 16. Stop on unresolved geometry, invalid reference or expiry and record incomplete rows. Label **Known**, a qualitative geometry-transfer exercise. It contributes zero cases to any headline or held-out denominator.
- **Status / result / PR:** proposed / not run / none.

### EXP-01 — Per-cell versus neighbour-aware network (rank 1)

- **Owner / time box:** Partner, 12 hours.
- **Hypothesis:** A small neighbour stencil may resolve local gradients omitted by a per-cell kinetic state and improve coarse-flow predictions enough to justify extra memory traffic. Compare a per-cell 1×1 stack with a matched-parameter model containing exactly one 3×3 layer, conserving through the same adapter.
- **Expected movement:** validation velocity error −10% or more, with runtime increase ≤ 10% and no stability loss.
- **Cheapest kill test:** two validation shapes, same training steps and three seeds, fixed parameter budget within 5%; kill if median error improves < 5% or runtime rises > 20%. Full X-02 adoption rules still apply.
- **Prior-work label/search:** **Partially explored.** Searched `"lattice Boltzmann" "3x3" neural collision` and `"collision operator" convolutional neighborhood`. Per-cell collision is established by [Corbetta](https://doi.org/10.1140/epje/s10189-023-00267-w); neighbour-aware learned CFD corrections by [Kochkov](https://doi.org/10.1073/pnas.2101784118). No claim that this comparison invents neighbourhood awareness.
- **Status / result / PR:** proposed / not run / none.

### EXP-02 — Short multi-step rollout training (rank 2)

- **Owner / time box:** Partner, 12–16 hours.
- **Hypothesis:** Exposure to a model's own evolving states may reduce accumulated error relative to one-step supervision. Compare K=`1,4,8` at equal measured training GPU-seconds, tracking recomputation cost and causal-halo size.
- **Expected movement:** at least 20% longer valid horizon or 10% lower 20-unit velocity error.
- **Cheapest kill test:** one periodic and two obstacle development cases; kill if K=4 gives neither 10% error reduction nor extra completed horizon after equal compute, or no valid configuration fits 3.5 GiB.
- **Prior-work label/search:** **Known.** Searched `learned lattice Boltzmann rollout100 steps` and `Kochkov2021 unroll checkpointing`. Multi-step learning is explicit in [Lettuce](https://arxiv.org/html/2106.12929) and [Kochkov](https://doi.org/10.1073/pnas.2101784118); [checkpointing](https://docs.pytorch.org/docs/stable/checkpoint.html) is a memory/recomputation tradeoff, not free capacity.
- **Status / result / PR:** proposed / not run / none.

### EXP-03 — Lattice symmetry: construction, augmentation, none (rank 3)

- **Owner / time box:** Partner with Clau, 12–16 combined hours.
- **Hypothesis:** Enforcing symmetry may improve data efficiency and rotated-obstacle behaviour, while group averaging could cost too much. Compare no symmetry, D4 training augmentation and a by-construction D4 variant; keep data/parameter/compute differences visible.
- **Expected movement:** 10% lower validation error at one-eighth data, or equal accuracy using half as much data; full-data stability must not regress.
- **Cheapest kill test:** train on two shapes and evaluate their fixed lattice rotations plus validation shapes; kill the construction variant if runtime > 1.25 × 3b and error gain < 10%. An augmentation improvement is a separate recorded outcome.
- **Prior-work label/search:** **Known.** Searched `lattice equivariant neural networks collision D2Q9 D3Q19` and `Corbetta collision symmetry group averaging`; [LENN](https://arxiv.org/abs/2405.13850) and [Corbetta](https://doi.org/10.1140/epje/s10189-023-00267-w) are direct precedents. Augmentation alone does not guarantee symmetry.
- **Status / result / PR:** proposed / not run / none.

### EXP-04 — Which non-conserved modes need learning? (rank 4)

- **Owner / time box:** Clau with Partner, 10–12 hours.
- **Hypothesis:** A more selective moment correction or conservative residual might improve accuracy per parameter compared with learning only the published higher-moment relaxation times. It may also destroy the intended viscosity if shear is changed; measure that through the same TGV diagnostic.
- **Expected movement:** 10% lower validation velocity error at ≤ 3b inference cost.
- **Cheapest kill test:** one conservative residual variant on periodic decay plus two obstacles; kill if inferred viscosity differs from configured viscosity by > 2% on resolved TGV, or obstacle improvement < 5% after the time box.
- **Prior-work label/search:** **Known family; specific comparison partially explored.** Searched `learned LBM non hydrodynamic moments neural collision bulk viscosity`; [Lettuce](https://arxiv.org/abs/2106.12929), [Horstmann et al.](https://doi.org/10.1016/j.compfluid.2024.106191) and [kinetic SGS work](https://arxiv.org/abs/2403.18466) already learn collision/moment behaviour.
- **Status / result / PR:** proposed / not run / none.

### EXP-05 — Local near-wall conditioning (rank 5)

- **Owner / time box:** Clau, 10–12 hours.
- **Hypothesis:** Adding clipped distance and local wall orientation might help distinguish under-resolved boundary layers from bulk non-equilibrium without changing solver boundaries. Any benefit may instead be memorization of the training geometry family.
- **Expected movement:** near-wall velocity error −15%, overall error −10%, with no extra validation failures.
- **Cheapest kill test:** two withheld validation shapes, both rotated and shifted relative to grid; kill if overall error gain < 5% or shifted-geometry error worsens > 10%.
- **Prior-work label/search:** **Partially explored; no novelty claim.** Searched `neural lattice Boltzmann collision wall distance geometry conditioning` and `learned CFD coarse solver boundary geometry features`. These searches found [data-driven LBM near-wall modelling](https://www.nature.com/articles/s42005-024-01832-1), an adjacent established direction, and [Kochkov's learned numerical corrections](https://doi.org/10.1073/pnas.2101784118). They did not establish this exact low-Re collision-feature comparison as either new or already reproduced.
- **Status / result / PR:** proposed / not run / none.

### EXP-06 — Conditional per-cell neural work (rank 6)

- **Owner / time box:** Partner, 12–16 hours.
- **Hypothesis:** A cheap local indicator such as `||f−feq||/max(rho,epsilon)` can select where a learned collision is worth its cost, leaving BGK or RBGK elsewhere. A scalar cell gate preserves conservation if both branches do; irregular gather/scatter may erase savings.
- **Expected movement:** matched-accuracy end-to-end runtime −10% with unchanged E-09 qualification.
- **Cheapest kill test:** profile actual sparse dispatch at active fractions 1%, 5%, 10%, 25%, 50%, including indicator/gather/scatter, then check the two validation cases. Kill if no qualifying fraction saves 10%. Computing both branches and applying `where` is not conditional-compute speedup.
- **Prior-work label/search:** **Partially explored.** Searched `"lattice Boltzmann" "mixture" "experts" neural` and `"collision" "conditional" "neural"`. [MoE-Bolt](https://doi.org/10.1016/j.cpc.2025.109540) is sequence prediction; [Horstmann](https://doi.org/10.1016/j.compfluid.2024.106191) provides local adaptation. Neither establishes this exact dispatch rule; that is not proof of novelty.
- **Status / result / PR:** proposed / not run / none.

### EXP-07 — Reduced storage precision with learned compensation (rank 7)

- **Owner / time box:** Clau with Partner, 12–16 combined hours.
- **Hypothesis:** 16-bit storage with FP32 arithmetic may reduce bandwidth cost; training through the actual quantizer might recover some lost accuracy. Quantization can break mass/momentum even when collision before quantization is conservative. The representation/conservation mechanism is an open part of this entry.
- **Expected movement:** retained-state memory −25% or more and runtime −10% at E-09 accuracy.
- **Cheapest kill test:** first compare classical FP32 against a classical reduced-storage implementation, then train a tiny quantization-aware variant. Kill if post-storage A-07 conservation fails, conversion overhead removes 10% runtime gain, or the learned variant cannot beat the classical reduced-storage control. No sub 16-bit work until 16-bit passes.
- **Prior-work label/search:** **Partially explored; apparently new only as a narrow pairing, unconfirmed.** Searched `"lattice Boltzmann" "rounding error" neural network`, `"16-bit" "learned"`, and `"quantization" neural`. [Lehmann et al.](https://arxiv.org/abs/2112.08926) establishes reduced storage; [stability-guided moment quantization](https://arxiv.org/abs/2602.05295) is also relevant. These searches did not find an exact learned rounding-compensation collision match. The entry must repeat the search before any novelty claim.
- **Status / result / PR:** proposed / not run / none.

### EXP-08 — Coarse predictor/fine corrector over time (rank 8)

- **Owner / time box:** Clau, 6–8 hours, feasibility only.
- **Hypothesis:** Batching temporal subintervals might provide a narrow single-GPU benefit, but a GPU already saturated by one flow is unlikely to gain from the parallel-time idea. This is not automatically a local collision replacement.
- **Expected movement:** at least 10% true wall-clock saving at identical accuracy including all fine corrections; otherwise stop.
- **Cheapest kill test:** measure serial fine integration versus a fixed coarse/fine correction schedule with two or four batched intervals, same memory cap. Kill if one correction iteration already costs as much as the serial baseline or no 10% measured saving appears.
- **Prior-work label/search:** **Known, low priority.** Searched `parareal neural network learned coarse propagator single GPU` and `Lions Maday Turinici2001 parareal`. [Original Parareal](https://hal.science/hal-00798372v1/document) and [PINN coarse propagation](https://arxiv.org/abs/2303.03848) already cover the family. No genuine single-GPU angle was established in the search.
- **Status / result / PR:** proposed / not run / none. Adoption into the core would require an explicit scope/ruler PR because the temporal integrator changes; exploration alone cannot redefine the collision contract.

### EXP-09 — Esoteric Pull in-place streaming

- **Owner / time box:** Clau, 8–12 hours.
- **Hypothesis / expected movement:** One population buffer may reduce traffic and improve MLUPS by 10% on an identical classical or frozen-inference case. The 12 GB target already fits the required paths. Keep training differentiable with the original two buffers.
- **Cheapest kill test:** Test even and odd timesteps, boundaries, force and conservation against the qualified two-buffer path. Require P0.5’s 1,000-step parity and applicable gates before any use. Register a separately named execution path and rerun applicable E-08 comparisons before timing it as an eligible comparator. For learned inference check A-08 and E-12, including neighboring reads. Kill if parity fails, aliasing changes results or timing fails to improve by 10%.
- **Prior-work label / search:** **Known.** The search for “Esoteric Pull in-place streaming LBM” located the original single-buffer scheme. [Lehmann](https://doi.org/10.3390/computation10060092)
- **Status / result / PR:** proposed / not run / none.

### EXP-10 — Stress-capable obstacle-flow adaptation

- **Owner / time box:** Partner with Clau, 12–16 combined hours.
- **Hypothesis / expected movement:** Adapt the local kinetic subgrid approach of Ortali et al. from 3D turbulence to 2D obstacles. Target 10% lower paired validation velocity error than 3b with X-02’s classical guard. Register the 2D moment map, stress freedoms, loss, training budget and departures from the paper.
- **Cheapest kill test:** Check author-released code, license and version first. Search by article title, authors, GitHub and Zenodo. The paper and preprint were located on 18 November 2026; a matching public code release remains [VERIFY]. Record a verified URL/commit or document an independent implementation. Compare on two validation cases against 3b and TRT at equal budget. Kill on failed conservation, missed horizon or less than 5% screening gain.
- **Prior-work label:** **Known family; adaptation.** All obstacle-flow results carry the adaptation label. [Ortali et al., Physical Review Research 7, 013202](https://doi.org/10.1103/PhysRevResearch.7.013202) · [Authors’ methods and supplement](https://arxiv.org/html/2403.18466v2)
- **Status / result / PR:** proposed / not run / none.

### EXP-11 — Rollout-stability training

- **Owner / time box:** Partner, 12–16 hours.
- **Hypothesis / expected movement:** Compare plain D-14 rollout training with detached pushforward starts or bounded adversarial perturbations projected into the conserved-moment nullspace. Target 20% longer median valid horizon with at least one more completion.
- **Cheapest kill test:** Two validation cases, same model, starts, seeds and measured training GPU-seconds including noise generation. Record the perturbation norm before starting. Kill on failed conservation, an additional failed case, or no longer horizon within the time box.
- **Prior-work label / search:** **Partially explored.** A search for neural PDE solvers, pushforward and rollout stability located this training method and related kinetic unrolling. [Brandstetter et al.](https://arxiv.org/abs/2202.03376) · [Ortali et al.](https://arxiv.org/html/2403.18466v2)
- **Status / result / PR:** proposed / not run / none.

### EXP-12 — Bandwidth-aware learned collision

- **Owner / time box:** Clau with Partner, 12–16 combined hours.
- **Hypothesis / expected movement:** Extend EXP-07 with EXP-09 streaming, 16-bit population storage, FP32 arithmetic and learned quantization compensation. Target a further 10% matched-accuracy runtime reduction. Use out-of-place differentiation with the same quantizer during training.
- **Cheapest kill test:** Compare classical FP32, in-place FP32, in-place reduced storage, and the compensated inference path on identical starts. Require EXP-09 parity before quantization, A-07 after storage and E-09 at deployment. Kill on a failed bound or insufficient end-to-end gain versus the best qualifying classical control.
- **Prior-work label / search:** **Partially explored.** “Esoteric Pull FP16C” locates prior in-place reduced storage; EXP-07 records the search on learned rounding compensation. [Single-buffer precision demonstration](https://doi.org/10.3390/computation10060092) · [Reduced storage study](https://arxiv.org/abs/2112.08926)
- **Status / result / PR:** proposed / not run / none.

**Log maintenance.** Add observed effect sizes, all config/run IDs, spent hours, killed/adopted rationale and actual PR URL to each entry when work begins/ends. Preserve the original hypothesis/kill criterion; append amendments with reasons instead of rewriting history. X-01–X-04 in §9.3 identify process rules; EXP-01–EXP-12 identify experiments.

## 16. Collaboration and git workflow

**C-01. Authority and disagreements.** Clau owns solver/boundaries/physics/data generation; Partner owns model/training/scaling and implements the jointly owned harness. Try a cheap measurement to resolve disagreement, within 2–4 human-hours. Otherwise the affected component owner decides. For dataset, evaluation or scope, both decide; if unresolved after one week, choose the simpler option that still meets existing requirements and record why. Simplicity does not authorize dropping conservation, a gate, or human review. Decisions made in person enter §18 through a PR in the same week.

**C-02. Protected main.** Configure main to require PRs, successful lint/CPU checks, resolved conversations and approval by the **other human**; dismiss stale approvals after substantive updates. Disable direct pushes, force pushes and deletion, including administrator bypass where available. Agents may create branches/commits/PRs but cannot provide the required human approval. An initial empty public repository is bootstrapped with a minimal README/license commit only to enable branch rules; every research change afterwards uses a PR. Record that administrative bootstrap separately, not as a gate pass.

**C-03. The two-person approval detail.** Opening a human-authored PR records that author's sign-off; the other human's native Approve review is the second approval, including SDD/data/evaluation/scope changes. Substantive updates require a fresh review. Only agent-authored PRs require explicit current-head `Approved-by: <human> at <head SHA>` comments from both humans, plus the required native human review. Listing two CODEOWNERS does not enforce two approvals; require one native approval and check the appropriate human sign-offs before merge. [GitHub review rules](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

On PRs changing physics, numerics or evaluation, the reviewing human supplies L-04’s own 3–5 sentence explanation before approval.

**C-04. Normal sequence.**

1. Open one issue for a milestone task or exploration entry. Include requirement ID, owner, measurable acceptance and estimated hours. The issue links here rather than becoming a new spec.
2. Update local main from remote using fast-forward only; ensure the working tree is clean or intentionally commit existing work before switching.
3. Create `clau/<short-task>`, `partner/<short-task>` or `explore/exp-01-<short-task>`. Prefer 1–3 working sessions and ≤ 400 changed substantive lines per PR when the task permits; split larger tasks into reviewable dependency PRs.
4. Implement only that issue's scope, run relevant tests, inspect the diff for unintended files and secrets, then commit. Use `feat(component): ...`, `fix(component): ...`, `test(component): ...`, `docs(sdd): ...` or `exp(EXP-01): ...` as appropriate.
5. Push the feature branch and open a draft PR linking `Closes #issue` and the requirement IDs. Include evidence even when results are negative.
6. Mark ready when checks pass; the other human reads code/spec changes, reviews evidence and asks the agent to explain anything unclear. An agent review assists but never substitutes.
7. Address review, rerun affected checks and obtain fresh human approval for substantive changes. Jointly owned changes need C-03 sign-offs.
8. Squash-merge with the PR title as the final commit subject, preserving author/coauthor attribution. Do not merge a failing check or unreviewed numerical change.
9. Delete the merged feature branch, fast-forward local main, and remove obsolete local branches. Never reset another person's branch or discard their changes.

**C-05. Conflicts.** Stop and identify which requirements each side implements. Fetch main, merge it into the feature branch, resolve files jointly with the affected owner, rerun tests and request fresh review. For SDD conflicts combine both decisions with stable IDs; never choose “ours/theirs” wholesale. Do not rebase/force-push a branch the other person is using. A mistaken merged change is reverted through another PR, not rewritten out of main's history.

**C-06. PR template, exact proposed content.**

```markdown
## Change
What changed and why:

## Contract
SDD requirement(s) or exploration entry:
Linked issue:
Ruler/schema change: yes/no; version and required reruns if yes:

## Evidence
Tests and commands/config hashes:
Results, including failures and run IDs:
CPU/GPU/device and peak memory when relevant:

## Human review
Author has inspected the diff and evidence: yes/no
Other human reviewer:
Physics, numerics or evaluation PR: link the reviewer’s own 3–5 sentence explanation.
Human-authored PR: opening is author sign-off; other human approval link:
Agent-authored PR only: both current-head Approved-by comment links:
```

**C-07. CODEOWNERS, exact mapping template.** Replace `@CLAU_HANDLE` and `@PARTNER_HANDLE` with verified GitHub accounts during P0.0. An unresolved placeholder fails that milestone. Native required-codeowner review is **not enabled** for single-owner paths, since the owner often authors the PR and cannot approve it; use this file to route ownership and the required other-human review for enforcement.

```text
*                         @CLAU_HANDLE @PARTNER_HANDLE
/src/lbm/                 @CLAU_HANDLE
/src/data/                @CLAU_HANDLE @PARTNER_HANDLE
/src/models/              @PARTNER_HANDLE
/src/training/            @PARTNER_HANDLE
/src/evaluation/          @CLAU_HANDLE @PARTNER_HANDLE
/src/experiments/          @PARTNER_HANDLE
/configs/data/            @CLAU_HANDLE @PARTNER_HANDLE
/configs/evaluation/      @CLAU_HANDLE @PARTNER_HANDLE
/tests/                   @CLAU_HANDLE @PARTNER_HANDLE
/.github/                 @CLAU_HANDLE @PARTNER_HANDLE
/SDD.md                   @CLAU_HANDLE @PARTNER_HANDLE
/README.md                @CLAU_HANDLE @PARTNER_HANDLE
```

**C-08. Ignore policy, exact minimum patterns.** Tiny synthetic fixtures are generated in tests rather than committed as opaque datasets. Curated `results/` is intentionally not ignored.

```gitignore
/data/
/checkpoints/
/runs/
/logs/
/work/
/tmp/
*.pt
*.pth
*.ckpt
*.h5
*.hdf5
*.npz
*.npy
*.zarr/
events.out.tfevents.*
.env
.env.*
!.env.example
*.pem
*.key
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.ipynb_checkpoints/
```

**C-09. Public hygiene.** Secrets are supplied through local environment or repository secret storage, never notebooks/configs. Inspect staged files and enable available secret scanning. If a secret leaks, revoke it immediately; removing it from the latest file is insufficient. Do not commit datasets/checkpoints through Git Large File Storage (LFS) as a loophole. Third-party code retains its attribution/license; MIT applies to this project's own work.

**C-10. Pace mismatch.** Keep issues current: next review, run budget, exams. Daily contact replaces a weekly meeting. Use spare capacity for Track B or current-phase tests/audits; pair on dataset milestones. Aim for review within two working days; record exam pauses. Retain X-03's two-week review and two-human gates.

## 17. Open decision points and ratification

All choices below are **proposed**, not silently accepted. Recommendations specify the draft's concrete implementation path. Options are listed so a human decision can revise this sole document once rather than leave agents guessing.

| ID / deadline | Options and tradeoff | Recommendation and rationale | Owners / status |
|---|---|---|---|
| OD-01, P0.0 | Fixed-density control, acoustic or convective outlet with halfway velocity inlet. Open-boundary accuracy still needs refinement/domain testing. | Recommend A-12/A-13: characteristic density on outlet links, every face halfway, explicit corner precedence, free-slip D-07 walls; arbitrary integer nesting without rims/guards. Enables candidates 16/32/48 against independent r=6 reference qualified at r=9. | Both; Pending. |
| OD-02, P0.0 | HDF5 shards; Zarr directory/object chunks; NumPy compressed archive (NPZ) files. Zarr suits object stores; NPZ is simple but weak for random partial reads. | Immutable HDF5+JSON, D-10, for local patches and few files. | Both; proposed. |
| OD-03, P0.0 | On-demand versus retained corpus. |D-12: 40 GiB dataset, 5 GiB checkpoints, 10 GiB rolling staging; confirm actual disk/archive before production. Type C replaces default 2D patches. | Both; Pending. |
| OD-04, P0.0 | BGK, RBGK and constant-rate TRT versus other prescribed MRT/KBC methods. | A-15 fixes all three required methods, including Λ = 3/16. Qualify and time each. Any later ruler change invokes E-08. | Both / Pending |
| OD-05, before project 3b | Lettuce adaptation versus a different replicated baseline. |Retain source architecture; B1/B2 forward in Track B, D-14’s longer full-field project training, all-validation restart selection. | Both; Pending. |
| OD-06, P0.0 | Shared voxel averages versus analytic geometry/point sampling. |Retain rho/j averages, candidates 1/2/3 and independent reference 6. D-06 uses 17 representative/spot checks at 9, expanding after failures; P remains a rounding guard. | Both; Pending. |
| OD-07, B1/B2 before parity claim | Source fidelity versus correction; unresolved internals and figure values. |B1a preserves source training/test-update behaviour with a seed; B1b freezes evaluation. Both train from scratch. B2 uses B1b; SBX-02 tests time blocking. | Partner leads; Pending. |
| OD-08, P0.0 | Actual partner name/handles; repository name; supported Python/PyTorch versions; external archive. | Fill verified identities and choose the smallest tested dependency set supporting both GPUs and CPU. Do not invent names or CUDA compatibility. | Both; unresolved factual inputs. |
| OD-09, before P5 data | Useful periodic teaching signal versus dimensional plumbing. |P5-06 accepts coarse BGK divergence or ≥ 5% error only with finite RBGK and qualified 96³/160³ references. Plumbing fallback and sphere ladder remain. | Both; Pending. |
| OD-10, P1 before G2 | In-distribution accuracy versus family/Re transfer; onset and Mach control. |Shared three-family train/validation/main test; separate triangle and P1-frozen extrapolation pair. Mach pilot at r = 3, per-shape onset at 3 with endpoint checks at 6; freeze shared U and margins before fitting. | Both; Pending. |
| OD-11, before P4 | Ghost-only scaling versus bounded stress-capable rates. |P4-05’s fixed R = 0/1 rate family and protected paired R = 0 arms spans > 100× size. Full data trains to plateau/51,200 visits; smaller fractions screen. Final operator remains open. | Both; Pending. |
| OD-12, before G2 | Per-step timed diagnostics versus separate validity/cost profiles. |E-06/E-12: dense untimed certification, sampled diagnostic profile, core/output headline, batching/graphs, three timing attempts. | Both; Pending. |
| OD-13, before production | Classical compute versus training-data density. |P1-C: 168 GPU-hours per machine, measured dispatch, exact reuse then balanced training reductions; held-out counts, tolerances and reference factor stay fixed. | Both; Pending. |
| OD-14, before scaling | Plateau experiments versus available GPU time. |P4-06: 160 GPU-hours per machine; first use 12-window plateau checks and full ranking of three finalists, then remove five unprotected width-192 seed-33 rows if needed. Never shorten full-data training. Further scheduling requires a joint decision. | Both; Pending. |
| OD-15, before adoption | Improvement over weak 3b versus a useful classical comparison. |X-02 retains its original gain criteria and adds the better same-rung BGK/RBGK/TRT guard; disclose baseline coverage deficits. | Both; Pending. |
| OD-16, P0.0 | v0.4-R1. Fixed density, acoustic characteristic or convection. | A-12 acoustic closure and P0-F probe gates plus P0-C extension. | Both / Pending |
| OD-17, before P1 pilots | v0.4-R2. Family envelope or per-shape brackets. | Bracket the 14 held-out shapes and apply D-08 margins individually. | Both / Pending |
| OD-18, P0.0 | v0.4-R3. Roundoff or a common temporary perturbation. | Freeze D-07’s zero-integral inlet pulse and absolute restart clock. | Both / Pending |
| OD-19, before P1 qualification | v0.4-R4. Raw comparison or one bounded lag per window. | D-06 uses at most one convective unit and discloses raw errors. | Both / Pending |
| OD-20, P0.0 | v0.4-R5. Which constant-rate kinetic control to require. | Add zero-fit TRT to the fused path, matrix, adoption and cost ruler. | Both / Pending |
| OD-21, before generating Type C | v0.4-R6. Source step count or a longer physical horizon. | D-14 fixes one convective unit and ten sparse targets for P3b and P4. | Both / Pending |
| OD-22, before P1 pilots | v0.4-R7. Reduce U or address startup and extrapolation first. | Use T = 20, then Re ≤ 200 for extrapolation, then lower U. | Both / Pending |
| OD-23, P0.0 | v0.4-R8. Adopt corrected target and verify actual allocation. | 12 GB RTX 2060, 10.4 GiB process cap and direct finest-grid domain test. | Both / Pending |
| OD-24, at G4 | v0.4-V2. Full Phase 5, extended 2D cycle or classical 3D demonstration. | Record branch, evidence, claims, effort and both humans’ choice before learned 3D. | Both / Pending |

The following are deliberately **not ruler decisions**: final learned architecture, neighbourhood size, conservation mechanism, local state, useful symmetry, training objective and whether conditional compute/precision help. They are explored through §15, with contract-compliant adapters.

## 18. Decision log

Record ID, date, context/options, decision/status, rationale, evidence, responsible humans and PR. A proposed row is not a completed decision. Rows through DEC-035 preserve their historical wording and counts. DEC-036–055 and the current clauses specify the v0.4 proposals. No proposal records human approval.

| ID | Date | Decision / status | Rationale / evidence | Approval / PR |
|---|---|---|---|---|
| DEC-001 | 2026-10-20 | Adopt supplied project scope; pending human ratification — updated by DEC-045 | 2D-first local collision, rigorous fixed evaluation, 3D sphere endpoint; matches the project brief. | Pending / none |
| DEC-002 | 2026-10-20 | Proposed Type B macro-rollout targets | Avoids treating noncommuting restriction/streaming as conservative collision labels; D-01–D-05. | Pending / none |
| DEC-003 | 2026-10-20 | v0.1 odd-factor proposal; superseded in draft by DEC-012 | Historical on-site pairing; removed, never ratified. | None |
| DEC-004 | 2026-10-20 | v0.1 Lettuce proposal; updated by DEC-009/010 | Retain replication, correct documented source flaws. | None |
| DEC-005 | 2026-10-20 | v0.1 retention proposal; updated by DEC-010/012/013 | Full fine histories remain excluded. | None |
| DEC-006 | 2026-10-20 | v0.1 sign-off proposal; superseded in draft by DEC-022 | Remove redundant human-author comments. | None |
| DEC-007 | 2026-10-20 | B1 **Started**: Partner, GTX 1650 | R1 supplied fact; historical Lettuce, no project code. No gate/result claimed. | User instruction / no PR |
| DEC-008 | 2026-10-20 | Pending: early B2/B3, no P3c percentage cap — updated by DEC-046, DEC-048 | R1/R2/R23; replaces serial-only restriction, retains X-02/X-03. | Both / none |
| DEC-009 | 2026-10-20 | v0.2 proposal; updated by DEC-032: disclosed source corrections | R3 confirmed source facts; seeded split, no test optimizer, no downloaded preset; SBX-02 clean audit. | Both / none |
| DEC-010 | 2026-10-20 | v0.2 proposal; updated by DEC-027/033: Type C and K = 100 baseline — updated by DEC-041 | R4; replaces K = 8 patch handicap, 1,120 windows within 40 GiB. | Both / none |
| DEC-011 | 2026-10-20 | v0.2 proposal; updated by DEC-030/031: stress-capable scaling instrument — updated by DEC-049, DEC-050 | R5; fixed R0/R1 family, 54 runs plus 3 cheap Lettuce rows, final design open. | Both / none |
| DEC-012 | 2026-10-20 | v0.2 proposal; updated by DEC-024: halfway boundaries and independent reference — updated by DEC-036, DEC-039 | R6/R16; replaces odd factors/guards; candidate 1/2/3 versus 6 qualified 9, recomputed costs. | Both / none |
| DEC-013 | 2026-10-20 | v0.2 proposal; updated by DEC-026: train/interpolation/extrapolation rebalance — updated by DEC-037, DEC-042 | R7; 32/12/16+8 cases, wider training, separate extrapolation denominator. | Both / none |
| DEC-014 | 2026-10-20 | Pending: free-slip project walls | R8; DFG retains no-slip/parabolic setup. | Both / none |
| DEC-015 | 2026-10-20 | v0.2 proposal; updated by DEC-024: classical-pilot Mach choice — updated by DEC-042 | R9; shared U reduction, 0.10 matching cap/0.15 hard limit. | Both / none |
| DEC-016 | 2026-10-20 | v0.2 proposal; updated by DEC-024/026: resolved families/onset margins — updated by DEC-037, DEC-038 | R10/R11; ≥ 2-cell features, family brackets, deterministic pre-G2 levels. | Both / none |
| DEC-017 | 2026-10-20 | Pending: timing/diagnostic separation — updated by DEC-040, DEC-044 | R12/R18; core/output headline, sampled checks, untimed failure localization, ≤ 3 attempts. | Both / none |
| DEC-018 | 2026-10-20 | v0.2 proposal; updated by DEC-027: restart checkpoint selection | R13; every 5 epochs/all 12 validation cases, failures worst, deterministic ties. | Both / none |
| DEC-019 | 2026-10-20 | v0.2 proposal; updated by DEC-029: 3D nontriviality or labelled plumbing — updated by DEC-045 | R14; ≥ 5% coarse error with qualified reference, final sphere work retained. | Both / none |
| DEC-020 | 2026-10-20 | Pending: sphere 8/12/16 classical ladder — updated by DEC-043, DEC-045 | R15; 170 B/cell fits D = 16; expanded D = 12 only, learned 8–12. | Both / none |
| DEC-021 | 2026-10-20 | Pending: lifting clarification | R17; P only removes rounding residuals, no target change. | Both / none |
| DEC-022 | 2026-10-20 | Pending: review/instruction simplification — updated by DEC-046 | R19–R21; human PR opening plus other approval, agent comments, current issues, CLAUDE import. | Both / none |
| DEC-023 | 2026-10-20 | Pending: intermediate public 2D tag — updated by DEC-045 | R22; release after G4, final G5/G6 unchanged except R14 disclosure. | Both / none |
| DEC-024 | 2026-10-21 | Pending: cheaper pilots and representative qualification — updated by DEC-037, DEC-038, DEC-039, DEC-042 | S1; updates DEC-012/015/016. Use r = 3 pilots, r = 6 onset endpoints, 17 default r = 9 checks and mandatory family/split expansion after failure. Production Mach breaches require a joint decision. | Both / none |
| DEC-025 | 2026-10-21 | Pending: classical compute cap and reductions — updated by DEC-037, DEC-039, DEC-042 | S1; 168 hours per machine with reserve/overhead, exact reuse then balanced training reductions. No held-out, tolerance or reference-factor cuts. | Both / none |
| DEC-026 | 2026-10-21 | Pending: in-distribution headline and separate transfer — updated by DEC-037, DEC-042 | S2; replaces DEC-013/016's split assignment. Default 36/12/18/4/12 cases; all shared families appear in train/validation/main test. Side-row sparse fields keep references within 24 GiB. | Both / none |
| DEC-027 | 2026-10-21 | Pending: preserve baseline compute on the larger corpus — updated by DEC-041 | S2/S5; updates DEC-010. Type C has 1,152 training windows, but 50 virtual epochs preserve 51,200 visits; nested window fractions preserve family/Re support. | Both / none |
| DEC-028 | 2026-10-21 | Pending: adoption also meets classical performance — updated by DEC-040 | S3; adds same-rung BGK/RBGK completion/error guards to X-02 and prominent weak-3b coverage reporting. | Both / none |
| DEC-029 | 2026-10-21 | Pending: coarse divergence can establish nontriviality — updated by DEC-045 | S4; updates DEC-019. BGK divergence or ≥ 5% error counts only when coarse RBGK and qualified references complete. Plumbing fallback stays unchanged. | Both / none |
| DEC-030 | 2026-10-21 | Pending: plateau-controlled full-data scaling — updated by DEC-041, DEC-050 | S5; replaces DEC-011's uniform short budget. Full data uses plateau/51,200 visits, fractions screen; 160-hour machine cap first switches to 12-window plateau checks with full 36-window ranking of three finalists, then drops largest-width seed 33 if needed. | Both / none |
| DEC-031 | 2026-10-21 | Pending: bounded state-dependent moment rates — updated by DEC-049, DEC-050 | S6; supersedes the residual instrument in DEC-011. Rate offsets recover BGK at zero output; rates in (0, 2) do not guarantee nonlinear stability. | Both / none |
| DEC-032 | 2026-10-21 | Pending: reproduce before correcting | S7; updates DEC-009. B1a preserves test-loop updates, B1b freezes evaluation, B2 uses B1b. DEC-007's start record is unchanged. | Both / none |
| DEC-033 | 2026-10-21 | Pending: readable presentation and monitor-only windows — updated by DEC-041, DEC-050 | S8/S9; restore spacing and multi-part rules. The 96 Type C validation windows monitor loss only; restart windows still govern selection/adoption. | Both / none |
| DEC-034 | 2026-10-21 | Pending: visible efficiency break-even bar — updated by DEC-040 | S10; add measured same-resolution learned/BGK cost and acoustic rung ratio to each comparison. E-13 headline criteria stay unchanged. | Both / none |
| DEC-035 | 2026-10-21 | Pending: fused classical path before production — updated by DEC-040, DEC-044 | Final edit: P0.5 adds fused BGK/RBGK with portable-path parity and full P0 gates. Use qualified fused throughput for P1 and fused classical comparators in E-12; record execution paths. | Both / none |
| DEC-036 | 2026-11-18 | Pending | v0.4-R1. A-12 acoustic closure and P0-F probe gates plus P0-C extension (OD-16). | Both / none |
| DEC-037 | 2026-11-18 | Pending | v0.4-R2. Bracket the 14 held-out shapes and apply D-08 margins individually (OD-17). | Both / none |
| DEC-038 | 2026-11-18 | Pending | v0.4-R3. Freeze D-07’s zero-integral inlet pulse and absolute restart clock (OD-18). | Both / none |
| DEC-039 | 2026-11-18 | Pending | v0.4-R4. D-06 uses at most one convective unit and discloses raw errors (OD-19). | Both / none |
| DEC-040 | 2026-11-18 | Pending | v0.4-R5. Add zero-fit TRT to the fused path, matrix, adoption and cost ruler (OD-20). | Both / none |
| DEC-041 | 2026-11-18 | Pending | v0.4-R6. D-14 fixes one convective unit and ten sparse targets for P3b and P4 (OD-21). | Both / none |
| DEC-042 | 2026-11-18 | Pending | v0.4-R7. Use T = 20, then Re ≤ 200 for extrapolation, then lower U (OD-22). | Both / none |
| DEC-043 | 2026-11-18 | Pending | v0.4-R8. 12 GB RTX 2060, 10.4 GiB process cap and direct finest-grid domain test (OD-23). | Both / none |
| DEC-044 | 2026-11-18 | Pending | v0.4-V1. P0.5 time box, compiler probe and qualified fallback (§§5–6). | Both / none |
| DEC-045 | 2026-11-18 | Pending | v0.4-V2. G4 scope choice and branch-specific G5/G6 evidence (§§1, 12–13, OD-24). | Both / none |
| DEC-046 | 2026-11-18 | Pending | v0.4-V3. L-01–05 and phase self-checks (§§5–13, 16). | Both / none |
| DEC-047 | 2026-11-18 | Pending | v0.4-V4. Four-working-week artifact aim (§§5, 13). | Both / none |
| DEC-048 | 2026-11-18 | Pending | v0.4-V5. Two bounded B3 demos (§15). | Both / none |
| DEC-049 | 2026-11-18 | Pending | v0.4-V6. Pre-register H1/H2 and inferential tests (§§1, 10). | Both / none |
| DEC-050 | 2026-11-18 | Pending | v0.4-V7. Protect both full-data arms and recompute P4 budgets (§10). | Both / none |
| DEC-051 | 2026-11-18 | Pending | v0.4-V8. Add EXP-09 through EXP-12 with time boxes and kill tests (§15). | Both / none |
| DEC-052 | 2026-11-18 | Pending | v0.4-V9. Record non-binding future directions (§20). | Both / none |
| DEC-053 | 2026-11-18 | Pending | v0.4-V10. Carry DEC-035 forward into the v0.4 change history (§§6, 8). | Both / none |
| DEC-054 | 2026-11-18 | Pending | v0.4-V11. Track the checker and isolated human learning material (§13). | Both / none |
| DEC-055 | 2026-11-18 | Pending | v0.4-V12. Record shared reading and section coverage before ratification (§1). | Both / none |

Future in-person choices add rows here within the same week. A superseded decision stays visible with the replacing ID. The initial file contains no fabricated PR URLs, measured runs, author handles or completed approvals.

## 19. Risks and responses

| Risk / trigger | Required response | Owner |
|---|---|---|
| Learned operator diverges despite tiny one-step loss | Inspect conservation, units and rollout exposure; retain first-failure evidence; test a simpler compliant model within an exploration time box. Do not add hidden fallbacks or change validity limits. | Partner + Clau |
| Poor shape/Re generalization | Report case-level failures and coverage; improve only on validation; require a fresh holdout after test-informed redesign. | Partner |
| Gains vanish against RBGK or TRT or timing overhead | Report no demonstrated gain; profile included operations; do not replace the stabilized baseline with weaker BGK-only comparisons. | Both |
| Exploration overfits validation | Log trial count, cap variants, confirm with three seeds, freeze candidates before test and create a new reporting cohort if continuing. | Both |
| Reference not converged or boundaries dominate | Fail qualification; refine/check domain or jointly revise boundary/reference contract and rerun all dependent evidence. A model cannot compensate for an untrustworthy ruler. | Clau |
| 4 GB or 12 GB or disk budget exceeded | Reduce microbatch/tile size with equivalent mathematics, stream observations, measure actual peak; do not silently reduce physical domains, horizons or test cases. | Component owner |
| 3D training does not transfer from periodic flow to sphere walls | Report the transfer failure; use the declared development sphere for new exploration and a fresh holdout for subsequent claims. Do not relabel same-grid velocity discrepancy as reference accuracy. | Both |
| No positive model/data scaling | Publish flat or worsening curves and compute-normalized costs; scaling is a research question. | Partner |
| Developers' pace diverges / exams | Shrink issue size, reserve review slots, pause optional exploration and use current-phase fixture work; do not bypass sequential gates. | Both |
| Source/dependency drift or unavailable historical code | Pin hashes, archive permitted source/config provenance, resolve `[VERIFY]`; use a joint replication-choice revision if necessary. | Partner |
| Git/spec fragmentation | One issue per task, short branches, human review; specs only here; generated docs and README link back. | Both |

## 20. Growth paths beyond this project

These paths are outside the project until both developers record a scope decision.

- A turbulent subgrid operator needs qualified high-Re references and spectra, using the local collision and restriction interfaces.
- A car-shape surrogate needs licensed CFD fields, consistent geometry and independent splits, using the dataset and evaluation interfaces with a new task contract. [DrivAerNet++](https://proceedings.neurips.cc/paper_files/paper/2024/hash/013cf29a9e68e4411d0593040a8a1eb3-Abstract.html)
- A short write-up on SBX-02 or the scaling question needs a clean, bounded result, using the immutable run manifests and reproducible figures.
- An upstream Lettuce fix or test needs a minimal reproduction on a pinned version, using the source-fidelity fixtures and parity tests.

## Appendix A. Exact agent instruction files

Create `AGENTS.md` with exactly this content. It is the sole agent instruction file; it points to this specification and restates git rules.

```markdown
# Agent instructions

Read SDD.md in full before making changes. SDD.md is the sole specification.
If a requirement is unclear or conflicts with the current code, record the issue
and propose an SDD.md change; do not invent a separate specification.

Use a short-lived feature branch. Never push directly to main.
Link each PR to its issue and SDD requirement or exploration entry.
Run the required lint and CPU checks and attach relevant numerical evidence.
Every PR requires review and approval by the other human, not only an agent.
Opening a human-authored PR is the author's sign-off; obtain the other's approval.
Agent-authored PRs need both humans' current-head Approved-by comments.
Never write the human reviewer's L-04 explanation; leave it to the human.
Do not merge until required CI and human reviews pass.
Use squash merges; preserve author and coauthor credit.
Do not rewrite shared history or discard another person's changes.
Never commit datasets, checkpoints, transient logs or secrets.
Record in-person decisions in SDD.md through a PR within the same week.
```

`CLAUDE.md` contains only this import line, so the instructions cannot drift:

```text
@AGENTS.md
```

## Appendix B. Source-audited moment definition and outstanding verification

For the proposed 2D replica, define the Dellar moments as `m=(rho,jx,jy,Pi_xx,Pi_xy,Pi_yy,N,Jx,Jy)` with matrix columns

`M[:,i]=(1,cx,cy,cx²,cx cy,cy²,g,g cx,g cy)ᵀ`,

`g=9cx²cy²−3cx²−3cy²+1`.

Thus g is 1 at rest, −2 on axes and 4 on diagonals. Set `m_eq=M feq` and `f_star=M⁻¹[m−diag(1/tau_a)(m−m_eq)]`. This mathematical basis follows [Dellar 2003, equations 4 and 20–21](https://people.maths.ox.ac.uk/dellar/papers/incompLB.pdf). Compare historical normalization/order in B1/B2 before claiming parity; B2 uses B1b weights. Resolve differences with an explicit transform or disclosed adaptation.

Source verification register, updated 2026-10-20:

| Item | Status / reason | Resolving evidence / blocking gate |
|---|---|---|
| Source setup/data/training/comparison facts in P3b-02 |Confirmed script read 2026-10-20: 40 pairs, unseeded pre-split shuffle, test optimizer updates, full-grid 100-step training and own-initial-state 4,000-step comparison. |B1a preserves source behaviour with a seed; B1b freezes evaluation. Store source hashes and both run records. |
| Paper figure identities |Verified: Figure 3 is kinetic-energy evolution; Figure 4 contains vorticity fields; Figure 5 shows diagonal vorticity after 4,000 steps. |[Paper §3.1](https://arxiv.org/html/2106.12929); B1a compares these figures and records discrepancies. |
| `[VERIFY]` quantitative values extracted from published figures |Figure identities are verified; underlying numerical curve arrays and digitization uncertainty are not. |Use auditable source data or document digitization and uncertainty. No invented agreement band; this blocks a quantitative reproduction claim, not a disclosed visual comparison. |
| `[VERIFY]` tagged Dellar normalization |Published mathematical basis is known; historical normalization/order needs inspection. |Pinned transform excerpt and B2 parity fixture; blocks B2/G3 parity claim. |
| `[VERIFY]` `torch_gradient` differentiability |Historical utility's gradient behaviour has not been established. |Inspect/test it in B1. Preserve historical behaviour in B1a; disclose and test any B1b correction before B2 parity. |
| `[VERIFY]` `net_preset.pth` provenance |Default source mode loads it, but origin/config remain unverified. Both B1a and B1b train from scratch and never execute this file. |Keep preset-checkpoint comparison unavailable; the excluded preset does not block G3. |
| Actual names/handles, installed GPU software compatibility and free disk |Not supplied by the brief and must not be invented. |P0.0 records and real smoke/storage checks; G0. |

All other numerical thresholds in this SDD are explicitly project criteria or linked published values. Before merging a gate, verify that its evidence uses the same definitions, units, geometry, reference, precision and ruler version as the requirement it claims to satisfy.

