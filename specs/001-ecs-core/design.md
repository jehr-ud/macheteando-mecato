# Design — ECS Core

## Componentes principales

```text
ECSWorld
 ├── EntityManager
 ├── ComponentStore
 └── Query
```

Una entidad se identifica mediante un ID.

Los componentes son datos independientes.

Los Systems reciben acceso al World y realizan consultas.

## Dependencias

`ECSWorld` no depende de Pygame.

## Consulta conceptual

```python
world.query(Transform, Velocity)
```

debe devolver las entidades que poseen ambos componentes.

## Decisión

No implementar un ECS industrial completo. El objetivo es un núcleo pequeño y comprensible para el juego.
