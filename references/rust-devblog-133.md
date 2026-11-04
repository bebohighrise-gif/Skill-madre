# Rust Devblog 133: client/server work and spec-driven changes

Load this reference only when a task explicitly targets an authorized Rust Devblog 133 server, client, plugin, or related asset pipeline. Treat the exact game build, Unity version, toolchain, and ownership/scope as task inputs to establish—not as capabilities guaranteed by this skill.

## Evidence and compatibility boundaries

- Begin by identifying the exact client/server build, repository or artifact, runtime, compiler/editor versions, available source, and authorized target. Distinguish the server/plugin code from the game client and any asset pipeline.
- Do not claim expertise, binary compatibility, successful injection, visibility, synchronization, or multiplayer behavior without direct evidence. Unity version strings, APIs, serialized formats, shaders, AssetBundle compatibility, prefab paths, and networking behavior must be checked against the actual target and reliable documentation or reproducible tests.
- Treat `ItemDefinition`, `ItemManager`, `heldEntityPrefab`, `BasePlayer.NetworkQueue.Update`, `heldEntity.SendNetworkUpdate(...)`, and `item.MarkDirty()` as names supplied by the user or hypotheses until their presence, signature, semantics, and applicability are confirmed for the exact codebase/build. Do not insert them mechanically or claim they are universally required.
- Do not claim that a server-side change can make a client render an asset the client does not have. Establish the complete client asset lookup/loading path and server-side item/entity registration from evidence. If the client is immutable or unavailable, state the resulting limitation rather than promising a visual result.
- Respect licenses, game terms, anti-cheat and access controls, third-party IP, privacy, and the target owner's written authority. Do not bypass authentication, licensing, anti-tamper protections, or distribution restrictions. Stop if authorization or the permitted scope is unclear.

## Feature workflow: spec before implementation

Use this staged conversation for a new item or feature. Ask one focused question at a time and pause at each approval point; do not front-load a questionnaire or start coding before the user approves the relevant spec and plan.

1. **Constitution:** agree on constraints and measurable acceptance criteria. Consider client memory, texture/mesh sizes, load time, frame-time budget, bundle size, server memory, persistence, network traffic, and failure/rollback behavior. Avoid unsupported performance estimates.
2. **Specification:** identify the requested item/feature; available and licensed models, textures, animations, prefabs, source files, and provenance; intended client and server behavior; IDs, balance values, costs, and defaults; target build; and test environment. Mark missing information as unknown and ask only the next decision needed.
3. **Planning:** map the actual asset build/load path and server registration path from repository evidence. Confirm toolchain and format compatibility before proposing conversion or injection. Identify affected files, APIs, dependencies, risks, test seams, rollback, and a client/server convergence check.
4. **Tasks:** split the approved plan into small, ordered client, server, and validation tasks. Include owner, inputs, output, and acceptance evidence for each task.
5. **Implementation and convergence:** implement one slice at a time after approval. Verify resource identifiers and entity/prefab resolution on both sides. Validate state updates through the actual code/API contract; do not add guessed network calls. Report separately what was source-reviewed, built, loaded, and tested in multiplayer.

## Bug-fixing workflow

For crashes, missing textures, invisible first-person entities, wrong item IDs, or network/state-update issues:

1. Capture exact game/server build, steps, expected/actual behavior, logs, relevant asset and prefab identifiers, frequency, and whether the issue reproduces.
2. Trace the failing value across the client asset lookup/render path and server item/entity/network path. Treat client asset absence, incompatible import/serialization, wrong resource path, ID mismatch, and update semantics as hypotheses until established.
3. Present the evidence-based root-cause hypothesis and a focused proposed fix before editing or compiling. If evidence is insufficient, ask for the smallest missing artifact or observation.
4. Add a regression check that covers the owning boundary. Define a multiplayer verification plan for item acquisition/equip/use/state update and visibility on relevant clients; do not describe a planned test as a passed test.
5. Record unresolved compatibility and environment limits. Never claim “100% functional” based only on static inspection or a server-only test.

## Idea assessment

For large imports or modern systems (vehicles, monuments, complex animation, or high-rate network behavior), assess the exact target engine, client/server protocol, asset formats, memory/frame/network budgets, licensing, and available test environment. Return one evidence-based recommendation:

- **Go:** the required behavior is supported by verified interfaces and a feasible test path.
- **Clarify / simplify:** a smaller asset, reduced feature set, alternate representation, or missing prerequisite could make it feasible.
- **Stop:** a demonstrated engine/protocol/toolchain or authorization constraint blocks the requirement; cite the evidence and offer a safe alternative when possible.

## Communication and records

State the current stage and the next logical step. Keep questions short and singular. For multi-step work, record the approved constitution, spec, decisions, plan, task status, evidence, and unknowns in the repository's established documentation location. Do not invent a hidden Spec Kit directory or imply that Spec Kit tooling is installed; use an existing Spec Kit structure when present, otherwise document the agreed artifacts in the project's normal location.