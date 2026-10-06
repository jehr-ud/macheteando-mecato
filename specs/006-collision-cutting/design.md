# Design — Collision & Cutting

```text
Input Action
     ↓
Cut Trajectory
     ↓
CollisionSystem
     ↓
CutResult
 ├── Mecato
 ├── Bomb
 └── None
```

CollisionSystem trabaja con componentes y no debe depender de clases concretas de fruta.

El resultado de corte puede ser consumido por ScoringSystem y LifeSystem.
