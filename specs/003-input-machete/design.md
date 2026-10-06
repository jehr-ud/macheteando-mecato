# Design — Input & Machete

```text
Pygame Events
      ↓
Input Adapter
      ↓
Input Component / Player Action
      ↓
Collision System
```

El machete se modela como interacción/trayectoria, no como una clase que contiene todas las reglas del juego.

Para multijugador local, cada jugador debe tener un identificador de entrada.
