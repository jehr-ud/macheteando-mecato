# Requirements — ECS Core

## Objetivo
Implementar el núcleo ECS que permita registrar entidades, almacenar componentes y consultar entidades por composición.

## Requisitos
- R1. Crear y destruir entidades.
- R2. Asociar componentes a entidades.
- R3. Eliminar componentes.
- R4. Consultar entidades por uno o varios tipos de componentes.
- R5. Permitir que Systems procesen consultas.
- R6. No acoplar el ECS World a Pygame.
- R7. Incluir pruebas automatizadas para creación, componentes y consultas.

## Criterios de aceptación
- Se puede crear una entidad.
- Se pueden agregar y recuperar componentes.
- Una consulta devuelve solamente entidades que cumplen la composición solicitada.
- Las pruebas pasan sin abrir una ventana de Pygame.
