# Design — Game Bootstrap

```text
main.py
   │
   ▼
 Game
   │
   ├── Pygame initialization
   ├── ECS World
   ├── Scene Manager
   └── Game Loop
```

`main.py` debe ser deliberadamente pequeño.

La clase `Game` pertenece a `src/game/game.py`.

El Game Loop será responsable de:

1. Capturar eventos.
2. Actualizar el estado/sistemas.
3. Renderizar.
4. Mantener el control temporal de la aplicación.
