# Design — UI, Scenes & Assets

Utilizar State/Scene Pattern:

```text
Menu
 ↓
Gameplay
 ├→ Pause
 ├→ Victory
 └→ GameOver
```

`AssetManager` administra imágenes, fuentes y animaciones.

`AudioManager` administra música y efectos.

La UI consume estado de juego y no debe modificar directamente las reglas del dominio.

La referencia visual proporcionada por el usuario se utiliza para orientar la composición general, pero el arte final debe ser original.
