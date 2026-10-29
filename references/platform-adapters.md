# Neutral host adapter guidance

Do not encode a vendor name, model name, account identifier, secret, or fixed installation path in the skill. Let the host choose its discovery mechanism.

A compatible host can load the package from a user skill root, project skill root, custom configured path, uploaded folder, `.zip`, or `.skill` archive. The installer uses a neutral default: `$HOME/.agent/skills/madre/` for user scope and `<project>/.agent/skills/madre/` for project scope.

If the host has a documented native folder, use `--scope custom --dest PATH`. If it accepts uploads, run `./install.sh --package /tmp/madre.skill` and upload the resulting archive. If it only accepts text instructions, load `SKILL.md` and preserve the referenced resources where the host can read them.

Installation, discovery, activation, and tool permission are separate events. Report each one separately. The skill never grants shell, browser, filesystem, network, MCP, device, package, or account access by itself.
