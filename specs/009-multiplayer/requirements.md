# Requirements — Local Multiplayer

## Objetivo
Permitir que dos o más jugadores participen en la misma partida local.

## Alcance inicial
Multijugador local en el mismo equipo.

## Requisitos
- R1. Soportar al menos dos jugadores.
- R2. Cada jugador debe tener identidad independiente.
- R3. Cada jugador debe tener puntuación independiente.
- R4. Cada jugador debe tener vidas independientes.
- R5. Cada jugador debe tener entrada configurable.
- R6. El ECS debe permitir entidades asociadas a un jugador.
- R7. El diseño no debe impedir una futura implementación de red.

## Criterios de aceptación
- Dos jugadores pueden realizar acciones durante la misma partida.
- Los resultados de ambos jugadores se mantienen separados.
- La interfaz puede mostrar los resultados de ambos.
