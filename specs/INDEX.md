# Índice de Specifications

| ID | Spec | Propósito |
|---|---|---|
| 001 | ECS Core | Núcleo ECS |
| 002 | Components & Factory | Componentes y creación |
| 003 | Input & Machete | Interacción de corte |
| 004 | Spawn System | Aparición dinámica |
| 005 | Physics | Movimiento y gravedad |
| 006 | Collision & Cutting | Detección de cortes |
| 007 | Score, Lives & Combo | Puntuación, vidas y combos |
| 008 | Time, Difficulty & Levels | Tiempo y progresión |
| 009 | Local Multiplayer | Multijugador |
| 010 | UI, Scenes & Assets | Interfaz y recursos |
| 011 | Records & Objectives | Récords y competencia |

## Dependencias

```text
001 ECS
  ↓
002 Components + Factory
  ↓
003 Input ─────────┐
005 Physics ───────┤
004 Spawn ─────────┤
                   ▼
              006 Collision
                   ↓
              007 Score/Lives
                   ↓
          008 Time/Difficulty
                   ↓
          009 Multiplayer
                   ↓
          010 UI/Scenes
                   ↓
          011 Records
```
