# Auditoría y refactorización de Skill-madre

Repositorio revisado: [bebohighrise-gif/Skill-madre](https://github.com/bebohighrise-gif/Skill-madre). La revisión se hizo sobre el contenido clonado y sobre el comportamiento real de sus scripts, no solo sobre el README.

## Problemas confirmados

El `SKILL.md` central tenía 239 líneas y mezclaba contrato de seguridad, selección de flujo, software, plataformas, UX, investigación, reverse engineering, release e instalación. Eso hacía difícil saber qué debía cargarse para cada tarea y aumentaba el riesgo de reglas duplicadas o contradictorias.

El empaquetador declaraba una lista fija de 16 archivos, mientras `SKILL.md` referenciaba otros recursos. En particular, el archivo `references/rust-devblog-133.md` podía ser requerido por el skill pero no entrar en el `.skill`; el validador existente no comprobaba el grafo de referencias internas ni que el archivo que se instalaba coincidiera con lo que el skill podía cargar.

El instalador original copiaba una lista fija distinta de la del empaquetador. Con `--force`, movía primero la instalación existente a un respaldo y solo después comenzaba a copiar; si la copia fallaba, el destino quedaba incompleto o ausente. Tampoco rechazaba symlinks en los recursos ni validaba el paquete antes de escribir.

La documentación presentaba el instalador como un subagente separado y mantenía referencias a módulos que ya no formaban parte de la estructura efectiva. También describía capacidades que debían quedar explícitamente limitadas por el host, la autorización y las pruebas reales.

## Arquitectura aplicada

El nuevo `SKILL.md` funciona como router. Carga primero el contrato del sistema, después el modo de trabajo, luego únicamente el lane necesario y finalmente los controles de calidad.

Los módulos ahora son: `system-contract.md` para verdad, autorización, secretos y alcance; `workflow-routing.md` para seleccionar el modo; `software-engineering.md` para código y cambios técnicos; `security-and-reverse-engineering.md` para pruebas autorizadas; `research-and-creative.md` para investigación, UX y medios; `platforms.md` para adaptadores; `quality-gates.md` para evidencia de entrega; e `installation.md` para empaquetado e instalación.

El validador reconstruye el conjunto de archivos runtime, revisa frontmatter, tamaño, symlinks, archivos sensibles y referencias locales rotas. El empaquetador usa ese mismo conjunto y falla si el archivo de salida ya existe o está dentro del árbol fuente. El instalador valida antes de escribir, prepara un staging completo, rechaza overwrite sin `--force`, y conserva un backup con marca de tiempo al reemplazar.

## Verificación ejecutada

Se ejecutó `python3 scripts/validate_project.py`, que terminó correctamente con 10 archivos runtime y referencias locales válidas. Se creó `/tmp/madre-refactor.skill` con 12 archivos, incluidos todos los módulos referenciados y sin copiar `scripts/` al skill instalado.

Se probó instalación en un destino temporal. La primera instalación terminó correctamente; una segunda instalación sin `--force` fue rechazada; la instalación con `--force` terminó correctamente y creó un backup. También pasaron `python3 -m py_compile scripts/*.py`, `git diff --check` y `bash -n install.sh`.

## Límites restantes

Esto valida la estructura, los scripts y los controles estáticos del paquete. No demuestra que un host externo descubra o active automáticamente la skill, ni demuestra compilación, ejecución o comportamiento de runtime de proyectos a los que la skill pueda aplicarse. Esas comprobaciones dependen del host y del proyecto objetivo.

## Fase de endurecimiento de la versión final

El instalador ya no ejecuta `scripts/validate_project.py` ni depende de otro script del paquete para decidir si instala. Hace sus comprobaciones mínimas internamente, calcula un manifiesto SHA-256 del grafo runtime, valida la copia staged antes de reemplazar y verifica de nuevo la copia final. Si la verificación final falla después de un `--force`, elimina la copia defectuosa y restaura el backup.

También se recuperó profundidad técnica como cinco módulos enfocados: contratos API, migraciones de datos, dependencias/supply chain, observabilidad/rendimiento/confiabilidad y arquitectura/release. Se eliminó la evaluación obsoleta de Rust Devblog, se subió el esquema de evaluaciones a la versión 6 y se añadieron casos de autorización, integridad de instalación y selección de playbooks.
