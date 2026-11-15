# Dependencies and supply chain

Load this module before adding or changing a package, image, action, tool, or generated artifact.

First check whether the project already provides the capability. Inspect the exact source, version, owner, maintenance, license, platform support, transitive footprint, install scripts/native code, advisories, lockfile effect, provenance, and checksum or signature where applicable. Do not execute newly fetched install hooks merely to inspect a dependency.

Pin or constrain versions according to project policy and preserve reproducible lockfiles. Do not upgrade unrelated packages. If source, license, integrity, or maintenance cannot be established, mark it unknown and do not present the dependency as approved.
