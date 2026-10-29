# Madre — Open Quality Engineering

Skill open source y portable para agentes de software. Enseña un proceso evidence-first para inspeccionar repositorios, investigar, diseñar, escribir código, depurar, revisar seguridad, mejorar UX/UI, validar calidad y entregar cambios sin romper lo que ya funciona.

## Qué incluye

El núcleo está en [SKILL.md](SKILL.md). Incluye protocolo de arranque, rutas de trabajo, uso responsable de herramientas, investigación, bugs, TDD, siete controles de calidad, UX/UI, accesibilidad, Web, desktop, Android, iOS, 3D, 4K, animaciones, ingeniería inversa autorizada, rollback y entrega.

El paquete funciona como una carpeta portable: contiene `SKILL.md` y recursos que el agente puede cargar progresivamente. No depende de un proveedor, modelo, SDK, navegador, emulador, GPU, MCP, credencial o ruta fija.

## Instalación genérica

El instalador no adivina ni escribe en cuentas externas. Instala la carpeta en un destino neutral y configurable:

```bash
# Instalar en el ámbito de usuario
./install.sh --scope user

# Instalar dentro de un proyecto
./install.sh --scope project --dest /ruta/de/tu/proyecto

# Elegir una carpeta de skills explícita
./install.sh --scope custom --dest /ruta/de/skills

# Crear un archivo portable para cargar manualmente
./install.sh --package /tmp/madre.skill
```

En Windows PowerShell:

```powershell
.\install.ps1 -Scope user
.\install.ps1 -Scope project -Dest C:\ruta\de\tu\proyecto
.\install.ps1 -Scope custom -Dest C:\ruta\de\skills
.\install.ps1 -Package C:\temp\madre.skill
```

La instalación por usuario utiliza una carpeta neutral en `$HOME/.agent/skills/`. La instalación por proyecto utiliza `.agent/skills/` dentro del proyecto indicado. Si el host necesita otra ruta, usa `--scope custom` o `-Scope custom`.

El instalador rechaza sobrescribir una instalación existente por defecto. `--force` o `-Force` crea primero un respaldo con marca de tiempo. No instala runtimes, paquetes globales, credenciales ni servicios.

## Instalador como subagente

La especificación del instalador está en [installer/SKILL.md](installer/SKILL.md). Ese subagente debe inspeccionar el paquete y el destino, validar antes de escribir, calcular un plan, pedir autorización para una sobrescritura, ejecutar de forma idempotente y entregar un reporte de ruta, versión, respaldo y resultado.

El script determinista que ejecuta la parte mecánica está en [scripts/install_skill.py](scripts/install_skill.py). Separar instrucciones de decisión y script de instalación evita que una instrucción ambigua copie archivos a un lugar incorrecto.

## Herramientas y SDKs

El agente puede escribir arquitectura, código, estilos, componentes, estados, tests, animaciones y documentación sin tener instalado cada SDK. Compiladores, emuladores, dispositivos, navegadores, GPU y herramientas 4K solo son necesarios para ejecutar o medir. La skill exige separar el trabajo estático realizado de la validación de runtime pendiente; nunca permite inventar una compilación o una prueba.

## Validación

```bash
python3 scripts/validate_project.py
python3 scripts/package_skill.py --output /tmp/madre.skill
```

Consulta también [references/platform-playbooks.md](references/platform-playbooks.md), [references/quality-matrix.md](references/quality-matrix.md), [references/portable-installation.md](references/portable-installation.md), [references/research-derived-methods.md](references/research-derived-methods.md) y [evidence-ledger.md](evidence-ledger.md). La referencia de investigación integra métodos públicos como activación progresiva, planificación por fases, handoffs durables, revisión independiente, evaluación por casos y límites de seguridad; no copia código, prompts, texto propietario ni branding.

## Licencia

MIT. Consulta [LICENSE](LICENSE) y [ATTRIBUTIONS.md](ATTRIBUTIONS.md).
