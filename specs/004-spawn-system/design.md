# Design — Spawn System

```text
SpawnSystem
 ├── SpawnTimer
 ├── SpawnConfiguration
 ├── RandomSource
 └── EntityFactory
```

El sistema genera un nuevo intervalo después de cada aparición.

Configuración:

```json
{
  "min_interval": 0.45,
  "max_interval": 1.20,
  "min_speed": 650,
  "max_speed": 900,
  "min_angle": 50,
  "max_angle": 130,
  "bomb_probability": 0.08
}
```

La aleatoriedad debe poder sustituirse en pruebas por una fuente determinista.

SpawnSystem decide cuándo y con qué parámetros iniciales crear la entidad. EntityFactory construye la composición ECS.
