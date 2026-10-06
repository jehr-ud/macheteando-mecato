# Prompts del agente — Macheteando

Esta carpeta contiene los prompts base utilizados para iniciar y dirigir un agente de desarrollo sobre el proyecto Macheteando.

## Archivos

- `system_prompts.md`: instrucciones de sistema y reglas permanentes para el agente.
- `project_bootstrap_prompt.md`: prompt inicial para crear el proyecto base desde cero.
- `agent_prompt_template.md`: plantilla reutilizable para solicitar al agente la implementación de una specification.
- `spec_implementation_prompt.md`: plantilla compacta para ejecutar una spec concreta.

## Flujo recomendado

```text
project_bootstrap_prompt.md
            ↓
      proyecto base
            ↓
      leer agents.md
            ↓
   seleccionar una spec
            ↓
agent_prompt_template.md
            ↓
 requirements → design → tasks
            ↓
       implementation
            ↓
          tests
            ↓
       verification
```

El agente debe respetar `agents.md` y los archivos de especificación como fuente de verdad.
