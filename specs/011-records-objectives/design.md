# Design — Records & Objectives

Separar:

```text
GameResult
RecordService
ObjectiveSystem
```

La persistencia inicial puede utilizar un archivo JSON local.

Ejemplo:

```json
{
  "player": "P1",
  "score": 7890,
  "level": 4,
  "cut_items": 120,
  "remaining_time": 45
}
```

La estructura debe poder migrar posteriormente a una base de datos o servicio remoto.
