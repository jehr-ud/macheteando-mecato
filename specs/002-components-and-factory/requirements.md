# Requirements — Components & Entity Factory

## Objetivo
Definir los componentes base y centralizar la creación de entidades mediante EntityFactory.

## Requisitos
- R1. Crear Transform.
- R2. Crear Velocity.
- R3. Crear Sprite.
- R4. Crear Collider.
- R5. Crear componentes de mecato.
- R6. Crear componentes de bomba.
- R7. Crear ScoreValue.
- R8. EntityFactory debe crear entidades con la composición adecuada.
- R9. La Factory no debe implementar física, colisiones ni puntuación.

## Criterios de aceptación
- `create_mecato()` crea una entidad válida.
- `create_bomb()` crea una entidad válida.
- Las entidades tienen los componentes requeridos.
- La Factory puede probarse sin ejecutar el render de Pygame.
