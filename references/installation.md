# Installation and packaging

Use the repository scripts rather than copying files by hand. Validate the source package and all referenced resources before writing. Resolve user, project, or custom scope explicitly; never guess a custom destination.

Do not execute bundled code during inspection. Do not copy repository metadata, caches, credentials, private keys, or undeclared files. Refuse unsafe symlinks and path escapes. Stage the complete destination first, validate the staged copy, then replace the old destination. With `--force`, create a timestamped backup only after the new copy is ready; if replacement fails, preserve the backup and report failure.

Report source revision, destination, files installed, backup path, validation result, host activation still required, rollback, and warnings. Do not claim host activation unless the host confirms it.
