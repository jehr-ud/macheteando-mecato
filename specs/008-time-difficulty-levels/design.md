# Design — Time, Difficulty & Levels

Separar responsabilidades:

```text
TimeSystem
DifficultySystem
LevelSystem
ObjectiveSystem
```

El DifficultySystem calcula un factor normalizado de progreso.

Ejemplo conceptual:

```text
progress = 1 - remaining_time / total_time
```

El factor puede influir en velocidad, spawn y otros parámetros.

No fijar una fórmula definitiva si no está validada; mantenerla configurable.

Los niveles se almacenan en `levels.json`.
