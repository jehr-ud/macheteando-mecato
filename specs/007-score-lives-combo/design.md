# Design — Score, Lives & Combo

Separar:

```text
ScoringSystem
LifeSystem
ComboSystem
```

Todos pueden consumir eventos/resultados de corte.

Modelo conceptual:

```text
CutResult
   ├── Mecato → ScoreSystem
   └── Bomb   → LifeSystem + ComboSystem
```

El máximo de vidas debe ser una constante/configuración validada contra el requisito de 5.
