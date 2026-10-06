# Design — Components & Entity Factory

## Componentes

```text
Transform
Velocity
Sprite
Collider
Mecato
Bomb
ScoreValue
Lifetime
```

## Factory

```text
EntityFactory
 ├── create_mecato(...)
 ├── create_bomb(...)
 └── create_powerup(...) [futuro]
```

La Factory recibe el ECS World y registra los componentes.

La Factory puede recibir referencias a un AssetManager o claves de assets, pero no debe cargar archivos directamente si existe un AssetManager.
