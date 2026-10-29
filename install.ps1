[CmdletBinding()]
param(
  [ValidateSet('user','project','custom')][string]$Scope = 'user',
  [string]$Dest,
  [switch]$Force,
  [string]$Package
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

if ($Package) {
  $output = [System.IO.Path]::GetFullPath($Package)
  python (Join-Path $root 'scripts\package_skill.py') --output $output
  Write-Host "Package created: $output"
  exit 0
}

$args = @('--scope', $Scope)
if ($Dest) { $args += @('--dest', $Dest) }
if ($Force) { $args += '--force' }
python (Join-Path $root 'scripts\install_skill.py') @args
