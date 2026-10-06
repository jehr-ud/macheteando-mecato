# AGENTS.md — Macheteando

## 1. Rol del agente

Actúas como agente de desarrollo de software para el proyecto **Macheteando**.

Tu responsabilidad es transformar especificaciones aprobadas en una implementación funcional, testeable y mantenible.

No debes implementar funcionalidades que no estén especificadas o autorizadas.

---

## 2. Fuente de verdad

Prioridad de información:

1. Requisitos de la especificación actual.
2. `requirements.md` general.
3. `design.md` de la especificación actual.
4. `tasks.md` de la especificación actual.
5. `README.md`.
6. Código existente.
7. Decisiones explícitas tomadas durante el desarrollo.

Cuando exista una contradicción, detén la implementación y señala la contradicción antes de inventar una solución.

---

## 3. Arquitectura obligatoria

El proyecto utiliza:

- ECS (Entity Component System).
- Entity Factory.
- Systems.
- Scene/State management.
- Game Loop.
- Configuración externa.
- Pygame como infraestructura.

Arquitectura conceptual:

```text
Input System ─────┐
Physics System ───┤
Spawn System ─────┤
Collision System ─┤
Scoring System ───┼──► ECS World ◄── Entity Factory
Level System ─────┤
Time System ──────┤
Render System ────┘
```

---

## 4. Reglas ECS

### Regla 1

Las entidades representan identidad/composición; no deben convertirse en objetos monolíticos que contengan toda la lógica.

### Regla 2

Los componentes deben contener principalmente datos/estado.

### Regla 3

Los Systems contienen comportamiento y procesan entidades que cumplen determinados criterios de componentes.

### Regla 4

No crear una jerarquía profunda de herencia para frutas, bombas, power-ups, etc.

Preferir composición mediante componentes.

### Regla 5

La creación de entidades debe realizarse mediante `EntityFactory`.

### Regla 6

Los Systems no deben duplicar la lógica de construcción de entidades.

---

## 5. Spawn

`SpawnSystem` es responsable de decidir:

- cuándo aparece una entidad;
- qué tipo puede aparecer;
- posición inicial;
- parámetros de lanzamiento;
- intervalo;
- reglas/probabilidades de aparición.

`EntityFactory` es responsable de construir la entidad.

El `SpawnSystem` no debe encargarse de actualizar la física de la entidad después de crearla.

---

## 6. Física

`PhysicsSystem` es responsable del movimiento, velocidad, aceleración y gravedad de entidades que tengan los componentes correspondientes.

No debe decidir qué entidad debe aparecer.

---

## 7. Entrada

`InputSystem` debe traducir eventos de Pygame a acciones del juego.

No debe contener reglas de puntuación, vidas o niveles.

La lógica central no debe depender directamente de `pygame.event` cuando sea posible.

---

## 8. Renderizado

`RenderSystem` es responsable de representar entidades y estado visual.

No debe modificar reglas de puntuación, vidas o dificultad.

---

## 9. Configuración

Los valores que razonablemente puedan cambiar entre niveles deben estar fuera del código:

- duración;
- velocidades;
- intervalos;
- probabilidad de bombas;
- puntuaciones;
- objetivos;
- dificultad.

Usar archivos JSON.

---

## 10. Pygame

Pygame debe estar principalmente en:

- input;
- rendering;
- audio;
- ventana;
- integración de tiempo.

El dominio y la lógica de juego deben depender de Pygame lo menos posible.

---

## 11. Assets

No cargar imágenes directamente desde las entidades.

Usar un `AssetManager`.

Ejemplo conceptual:

```python
asset_manager.get_image("mecato.mango")
```

en lugar de:

```python
pygame.image.load("assets/mango.png")
```

dentro de una entidad.

---

## 12. Testing

Cada funcionalidad debe incluir pruebas cuando la lógica pueda aislarse de Pygame.

Priorizar pruebas para:

- puntuación;
- vidas;
- dificultad;
- temporizador;
- spawn;
- probabilidades;
- objetivos;
- creación de entidades;
- reglas de nivel.

---

## 13. Flujo de trabajo

Para cada spec:

1. Leer `requirements.md`.
2. Leer `design.md`.
3. Leer `tasks.md`.
4. Revisar arquitectura existente.
5. Implementar una tarea.
6. Ejecutar pruebas.
7. Corregir errores.
8. Ejecutar nuevamente pruebas.
9. Validar criterios de aceptación.
10. Reportar cambios.

No marcar una tarea como terminada si no se puede demostrar que funciona.

---

## 14. Regla de cambios

Antes de introducir una nueva abstracción, comprobar si una solución más sencilla satisface la especificación.

No agregar frameworks o librerías innecesarias.

No reemplazar ECS por otro patrón arquitectónico sin autorización.

---

## 15. Calidad

El código debe:

- ser legible;
- utilizar nombres descriptivos;
- mantener funciones pequeñas;
- evitar duplicación;
- tener dependencias claras;
- incluir pruebas relevantes;
- respetar la arquitectura.

---

## 16. Criterio de parada

Si una decisión arquitectónica no está determinada por las specs y afecta significativamente al diseño, no asumir silenciosamente.

Documentar la decisión propuesta y solicitar confirmación cuando sea necesario.
