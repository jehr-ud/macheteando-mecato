# Prompt inicial — Crear proyecto base Macheteando

## Propósito

Este prompt se ejecuta una sola vez al iniciar el proyecto desde cero.

---

## PROMPT

Quiero que construyas el proyecto base de **Macheteando**, un juego arcade de escritorio desarrollado con **Python + Pygame**, siguiendo una arquitectura **ECS (Entity Component System)**.

Antes de implementar funcionalidades de gameplay, debes crear la estructura base del proyecto y dejarla preparada para implementar las specifications posteriormente.

### 1. Lee primero

Antes de crear archivos:

1. Lee `agents.md`.
2. Lee `requirements.md`.
3. Lee `README.md`.
4. Inspecciona el contenido de `specs/`.
5. No implementes todavía todas las specifications.

### 2. Arquitectura

La arquitectura inicial debe ser:

```text
                         ┌───────────────────┐
                         │   Physics System  │
                         └─────────▲─────────┘
                                   │
        ┌──────────────┐     ┌─────┴─────────────┐     ┌──────────────┐
        │ Input System │◄───►│     ECS World     │◄───►│ Spawn System │
        └──────────────┘     │                   │     └──────┬───────┘
                              │    Entities       │            │
                              │  + Components     │            ▼
                              └─────────┬─────────┘     ┌──────────────┐
                                        │               │Entity Factory│
                                        ▼               └──────────────┘
                              ┌───────────────────┐
                              │   Render System   │
                              └───────────────────┘
```

### 3. Estructura

Crear como mínimo:

```text
macheteando/
├── main.py
├── README.md
├── requirements.txt
├── agents.md
├── requirements.md
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── config/
│   ├── game.json
│   ├── levels.json
│   └── fruits.json
│
├── src/
│   ├── components/
│   ├── ecs/
│   ├── entities/
│   ├── factories/
│   ├── systems/
│   ├── scenes/
│   ├── input/
│   ├── rendering/
│   ├── audio/
│   ├── config/
│   ├── game/
│   └── prompts/
│
├── tests/
└── specs/
```

### 4. main.py

`main.py` debe ser pequeño.

Debe funcionar conceptualmente así:

```python
from src.game.game import Game


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
```

No coloques lógica de gameplay en `main.py`.

### 5. Game

Crear `src/game/game.py`.

`Game` debe ser el coordinador inicial de:

- inicialización de Pygame;
- ECS World;
- Scene Manager;
- reloj;
- Game Loop.

El Game Loop debe quedar preparado para:

```text
capture input
     ↓
update systems
     ↓
render
     ↓
next frame
```

No implementes todavía toda la lógica de los sistemas.

### 6. ECS

Crear una implementación mínima de `ECSWorld` que permita posteriormente:

- crear entidades;
- destruir entidades;
- añadir componentes;
- obtener componentes;
- eliminar componentes;
- consultar entidades por componentes.

Debe existir una base testeable sin depender de la ventana de Pygame.

### 7. Components

Preparar componentes base:

```text
Transform
Velocity
Sprite
Collider
Mecato
Bomb
ScoreValue
Lifetime
Player
```

No añadir comportamiento complejo dentro de ellos.

### 8. Entity Factory

Crear:

```text
src/factories/entity_factory.py
```

con una `EntityFactory` preparada para:

```text
create_mecato()
create_bomb()
create_player()
```

La implementación puede ser mínima en esta etapa.

### 9. Systems

Crear interfaces/clases base o esqueletos para:

```text
InputSystem
SpawnSystem
PhysicsSystem
CollisionSystem
ScoringSystem
LifeSystem
ComboSystem
TimeSystem
DifficultySystem
LevelSystem
RenderSystem
```

No implementar todavía toda la funcionalidad.

Cada System debe tener una responsabilidad independiente.

### 10. Scenes

Preparar:

```text
Scene
SceneManager
MenuScene
GameplayScene
PauseScene
VictoryScene
GameOverScene
```

Inicialmente pueden ser esqueletos funcionales.

### 11. Configuration

Crear archivos JSON iniciales para:

- configuración general;
- niveles;
- mecato.

No hardcodear innecesariamente estos parámetros en los Systems.

### 12. Tests

Crear una estructura inicial:

```text
tests/
├── test_ecs.py
├── test_factory.py
└── ...
```

Implementar inicialmente las pruebas correspondientes al núcleo ECS.

### 13. Dependencias

Crear `requirements.txt`.

La dependencia principal del proyecto debe ser Pygame.

No agregar frameworks adicionales sin necesidad justificada.

### 14. Validación

Cuando termines:

1. Ejecuta las pruebas.
2. Ejecuta `python main.py`.
3. Comprueba que Pygame puede inicializarse.
4. Comprueba que la aplicación puede cerrarse correctamente.
5. Comprueba que el ECS puede crear una entidad y asociarle componentes.
6. Comprueba que la arquitectura inicial no depende de código inexistente.

### 15. No implementar todavía

No implementes todavía:

- gameplay completo;
- física final;
- colisiones finales;
- multijugador;
- puntuación completa;
- niveles completos;
- récords;
- arte final.

El objetivo de este prompt es **crear el proyecto base**, no terminar el juego.

### 16. Resultado esperado

Al finalizar debes entregar:

```text
Proyecto base ejecutable
+
Arquitectura ECS inicial
+
Game Loop
+
Scene Manager inicial
+
Entity Factory inicial
+
Systems preparados
+
Components preparados
+
Configuración JSON
+
Tests iniciales
```

Después de completar este bootstrap, el desarrollo debe continuar specification por specification.
