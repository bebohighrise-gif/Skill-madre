# Platform implementation playbooks

These are source-level patterns. They help an agent create code and design without claiming that a native SDK, emulator, device, GPU, compiler, or browser is installed. Choose the actual stack from the repository before applying a pattern.

## iOS-style interfaces

When the request says “estilo iOS” but the project is Web or cross-platform, reproduce the interaction language rather than pretending it is a native iOS build: clear hierarchy, large readable titles, grouped surfaces, safe-area spacing, compact navigation, semantic controls, restrained shadows, purposeful transitions, Dynamic Type-like scaling, dark mode, and reduced motion. Use the project's actual components and CSS/design tokens.

When native SwiftUI is requested, use semantic views, state-driven rendering, previews when available, accessibility labels/hints, Dynamic Type, safe-area APIs, navigation state, and explicit loading/error/empty states. Do not claim a Swift compile or simulator result without Xcode evidence.

Example source-level shape:

```swift
struct ProfileView: View {
    @State private var isLoading = false
    let profile: Profile?

    var body: some View {
        Group {
            if isLoading { ProgressView("Loading") }
            else if let profile { ProfileContent(profile: profile) }
            else { ContentUnavailableView("No profile", systemImage: "person") }
        }
        .navigationTitle("Profile")
        .accessibilityElement(children: .contain)
    }
}
```

## Android-style interfaces

For Web or cross-platform projects, use Material-like tokens only when they fit the product: clear surface hierarchy, touch targets, visible focus/pressed states, predictable back behavior, resilient forms, system bars/safe insets, and accessible semantics. Do not claim Material compliance from color alone.

For Jetpack Compose, keep UI state explicit, separate state holders from composables, use semantic modifiers, stable keys for lists, lifecycle-aware collection, previews when available, and explicit loading/error/empty states. Do not claim an APK/AAB build or device result without Android toolchain evidence.

## Web and desktop

Use semantic HTML, progressive enhancement, keyboard-first interaction, visible focus, responsive constraints, reduced motion, resilient network states, URL/deep-link behavior, and accessible forms. For React or similar frameworks, keep server/client boundaries explicit, avoid unnecessary effects, model async state, preserve stable list keys, and test the owning boundary. For Electron-like apps, keep privileged APIs behind a narrow preload contract and treat renderer input as untrusted.

## Cross-platform architecture

Separate domain state, platform adapters, presentation tokens, and I/O. Keep a shared behavior contract while allowing platform-specific navigation, permissions, typography, haptics, safe areas, and lifecycle handling. Do not flatten important platform differences into user-agent conditionals scattered through the codebase. Prefer a small adapter boundary.

## 3D and 4K source work

A tool is not required to author scene code, materials, animation data, shaders, camera rules, asset manifests, or export configuration. Define target resolution and frame budget first. Keep source meshes and textures separate from delivery variants. Use LODs, bounded texture sizes, compressed delivery formats, deterministic camera framing, explicit color space, and fallback assets. Treat 4K as an output specification that must be preserved through the pipeline; do not call a stretched lower-resolution asset native 4K.

For animation, model states and transitions rather than adding an always-running loop. Use easing and timing to communicate cause and effect, make transitions interruptible, cancel work when state changes, and provide reduced-motion and low-power variants. A code review can check these properties without a GPU; frame-rate claims require measurement.

## Static validation without a toolchain

When the needed SDK is unavailable, still perform source-level checks: inspect types and imports, verify API names against authoritative documentation, check state transitions, inspect null/error paths, review permissions and secrets, format the code if a project-local formatter exists, and add tests or fixtures. Report exactly which checks were static and which runtime checks remain pending. Never downgrade a missing compiler into a fictitious pass.
