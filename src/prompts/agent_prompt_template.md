# Agent Prompt Template — Implementación de una Specification

Copia este prompt para solicitar al agente la implementación de una specification concreta.

---

## PROMPT

Actúa como agente de desarrollo del proyecto **Macheteando**.

Debes implementar exclusivamente la specification:

```text
SPEC_ID: {{SPEC_ID}}
SPEC_PATH: {{SPEC_PATH}}
```

### Contexto

Lee primero:

```text
agents.md
requirements.md
README.md
{{SPEC_PATH}}/requirements.md
{{SPEC_PATH}}/design.md
{{SPEC_PATH}}/tasks.md
```

Después inspecciona el código existente antes de modificarlo.

### Objetivo

Implementar la specification respetando exactamente:

- sus requisitos;
- su diseño;
- sus criterios de aceptación;
- la arquitectura ECS;
- las reglas de `agents.md`.

### Proceso obligatorio

#### Paso 1 — Analizar

Explica brevemente:

- qué necesita la specification;
- qué módulos existentes utilizarás;
- qué dependencias tiene;
- qué archivos probablemente deberán cambiar.

#### Paso 2 — Revisar arquitectura

Comprueba:

- ECS World;
- Components;
- Systems;
- EntityFactory;
- Scenes;
- configuración;
- tests.

No dupliques responsabilidades existentes.

#### Paso 3 — Implementar

Implementa las tareas de:

```text
{{SPEC_PATH}}/tasks.md
```

en orden lógico.

Mantén los cambios pequeños y verificables.

#### Paso 4 — Tests

Después de cada grupo lógico de cambios:

- ejecuta tests;
- analiza errores;
- corrige;
- vuelve a ejecutar.

No ignores fallos.

#### Paso 5 — Validación

Comprueba cada criterio de aceptación de:

```text
{{SPEC_PATH}}/requirements.md
```

### Restricciones

No:

- implementar funcionalidades de otras specifications;
- cambiar ECS por otro patrón;
- introducir dependencias innecesarias;
- mover lógica a `main.py`;
- convertir componentes en objetos monolíticos;
- crear Systems con responsabilidades múltiples;
- ignorar `agents.md`.

### Si encuentras un problema

Clasifica el problema como:

```text
BUG
ARCHITECTURAL CONFLICT
MISSING REQUIREMENT
AMBIGUITY
DEPENDENCY
```

Si es posible resolverlo sin cambiar la arquitectura, hazlo.

Si requiere una decisión arquitectónica importante, detente y explica la decisión necesaria.

### Resultado final

Al terminar responde:

```text
SPEC:
{{SPEC_ID}}

STATUS:
COMPLETED / PARTIAL / BLOCKED

IMPLEMENTED:
- ...

FILES CHANGED:
- ...

TESTS:
- ...

VALIDATION:
- ...

OPEN ISSUES:
- ...
```
