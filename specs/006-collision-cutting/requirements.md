# Requirements — Collision & Cutting

## Objetivo
Detectar cuándo el machete corta una entidad cortable.

## Requisitos
- R1. Detectar intersección entre trayectoria de corte y Collider.
- R2. Identificar entidades con componente Mecato.
- R3. Identificar bombas.
- R4. Generar resultado de corte.
- R5. Evitar cortar repetidamente la misma entidad en el mismo evento.
- R6. No calcular directamente la puntuación final.

## Criterios de aceptación
- Una trayectoria que cruza una fruta genera un corte.
- Una trayectoria que no cruza ninguna entidad no genera corte.
- Una bomba se identifica de forma diferente a un mecato.
