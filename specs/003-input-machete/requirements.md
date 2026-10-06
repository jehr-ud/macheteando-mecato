# Requirements — Input & Machete

## Objetivo
Permitir que el jugador utilice un machete mediante interacción de mouse.

## Requisitos
- R1. Capturar movimiento del mouse.
- R2. Registrar una trayectoria corta de movimiento.
- R3. Representar la acción de corte.
- R4. El sistema debe permitir detectar segmentos de movimiento.
- R5. La entrada no debe contener reglas de puntuación.
- R6. El diseño debe permitir más de un jugador.

## Criterios de aceptación
- Mover el mouse genera datos de trayectoria.
- La trayectoria puede ser consumida por CollisionSystem.
- El InputSystem no modifica directamente la puntuación.
