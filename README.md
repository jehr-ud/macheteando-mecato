# MACHETEANDO — Especificaciones del proyecto

## 1. Propósito

**Macheteando** es un juego de acción arcade para escritorio, inspirado en la mecánica de cortar objetos en movimiento, pero con una identidad visual y temática colombiana propia.

El jugador utiliza un machete para cortar elementos de **mecato** que aparecen en pantalla. La partida incorpora tiempo dinámico, dificultad progresiva, vidas, puntuación, récords, niveles y modo multijugador.

Este repositorio contiene las especificaciones que un agente de desarrollo debe utilizar para construir el proyecto.

---

## 2. Objetivo del desarrollo

Construir una primera versión funcional para escritorio utilizando:

- Python
- Pygame
- Arquitectura ECS (Entity Component System)
- Entity Factory para creación de entidades
- Sistemas independientes para lógica de juego
- Configuración externa mediante JSON
- Pruebas automatizadas para la lógica independiente de Pygame

La implementación debe seguir las reglas arquitectónicas de `agents.md`.

---

## 3. Arquitectura inicial

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

### Principios

- El **ECS World** administra entidades y componentes.
- Los **Systems** procesan entidades según sus componentes.
- `EntityFactory` centraliza la construcción de entidades.
- `SpawnSystem` controla cuándo y bajo qué condiciones aparecen entidades.
- `PhysicsSystem` controla movimiento y gravedad.
- `InputSystem` procesa teclado/mouse y la interacción del machete.
- `RenderSystem` representa el estado del juego visualmente.
- Pygame pertenece a la infraestructura y no debe contaminar innecesariamente el dominio.

---

## 4. Organización

```text
macheteando/
├── main.py                 # Punto de entrada de la aplicación
├── assets/
├── config/
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
│   └── config/
├── tests/
├── src/
│   └── prompts/
│       ├── README.md
│       ├── system_prompts.md
│       ├── project_bootstrap_prompt.md
│       ├── agent_prompt_template.md
│       └── spec_implementation_prompt.md
└── specs/
```

La estructura física exacta puede ser refinada durante el diseño, pero no debe romper las responsabilidades arquitectónicas definidas en `agents.md`.

---

## 5. Punto de entrada y Game Loop

`main.py` es el único punto de entrada de la aplicación.

Su responsabilidad es mínima:

```text
main.py
   ↓
Game
   ↓
Game Loop
   ↓
Scene Manager
   ↓
Current Scene
   ↓
ECS World + Systems
```

`main.py` no debe contener lógica de gameplay, creación manual de entidades, renderizado ni reglas de puntuación.

El `Game` debe encargarse de inicializar Pygame, crear las dependencias principales, configurar el `SceneManager` y ejecutar el Game Loop.

## 6. Orden recomendado de implementación

1. ECS World y ciclo básico.
2. Components.
3. Entity Factory.
4. Game Loop.
5. Input System.
6. Render System.
7. Physics System.
8. Spawn System.
9. Mecato.
10. Machete y corte.
11. Colisiones.
12. Puntuación.
13. Vidas.
14. Tiempo dinámico.
15. Dificultad progresiva.
16. Niveles.
17. Objetivos.
18. Multijugador.
19. Récords.
20. UI final, audio y pulido.

---

## 7. Criterio de trabajo del agente

El agente debe implementar una especificación a la vez.

Para cada spec:

```text
requirements.md
      ↓
design.md
      ↓
tasks.md
      ↓
implementation
      ↓
tests
      ↓
validation
      ↓
refinement
```

No debe implementar funcionalidades futuras únicamente porque parezcan convenientes.

---

## 8. Referencia visual

Las imágenes proporcionadas por el usuario sirven como referencia conceptual de:

- pantalla de gameplay;
- mercado colombiano;
- colores vivos;
- frutas/mecato;
- machete;
- puntuación;
- vidas;
- temporizador;
- pantalla de victoria;
- pantalla de derrota;
- progresión por niveles.

No se debe copiar literalmente una interfaz, personaje, ilustración o identidad visual de terceros. El resultado debe mantener una identidad original para Macheteando.
