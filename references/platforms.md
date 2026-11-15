# Platform adapters

Use only the applicable adapter and state which checks were actually run.

- **Web/desktop:** routes, deep links, browser support, resize/zoom, focus, keyboard, network failure, storage permissions, CSP/security headers, packaged assets, and production build. Separate renderer, preload, and main-process trust boundaries where applicable.
- **Android:** manifest, min/target SDK, runtime permissions, configuration changes, back navigation, process death/state restoration, offline behavior, accessibility, density variants, APK/AAB packaging, and signing assumptions. Static code does not prove device behavior.
- **iOS/iPadOS:** safe areas, Dynamic Type, VoiceOver order, reduced motion, dark mode, lifecycle, privacy descriptions, entitlements, deep links, signing, and simulator/device distinction.
- **3D/animation/media:** target device, frame budget, color space, aspect ratio, codec/container, texture and memory limits, LOD, draw calls, UVs, normals, scale, pivots, timing, interruption, and reduced-motion fallback. Upscaling is not native 4K.
