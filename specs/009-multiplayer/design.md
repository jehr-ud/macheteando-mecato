# Design — Local Multiplayer

No duplicar todos los Systems por jugador.

Los Systems procesan componentes que incluyen `player_id` cuando sea necesario.

Conceptualmente:

```text
Player 1 → Input mapping → Player entity
Player 2 → Input mapping → Player entity
                         ↓
                    ECS World
```

La arquitectura debe separar:

```text
Input source
Player identity
Game rules
```

La red queda fuera del primer alcance.
