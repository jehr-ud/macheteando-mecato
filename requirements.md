# Requisitos generales — Macheteando

## 1. Visión

Macheteando será un juego arcade de escritorio de temática colombiana en el que uno o más jugadores utilizan un machete para cortar elementos de mecato que aparecen dinámicamente en pantalla.

El juego debe ser rápido, visualmente llamativo, fácil de entender y progresivamente más desafiante.

## 2. Requisitos funcionales

### RF-01 — Plataforma

El juego debe ejecutarse como aplicación de escritorio.

La primera plataforma objetivo será desktop con Python + Pygame.

### RF-02 — Machete

El jugador debe utilizar un machete como mecanismo principal de interacción.

El movimiento del mouse debe permitir realizar cortes sobre elementos cortables.

La arquitectura debe permitir posteriormente soportar otros dispositivos de entrada sin modificar la lógica central del juego.

### RF-03 — Mecato

El mecato será el elemento principal del gameplay.

Debe existir una variedad de objetos de mecato que puedan aparecer, moverse, ser cortados y generar puntuación.

Los elementos podrán variar en:

- tipo;
- tamaño;
- velocidad;
- trayectoria;
- valor de puntuación;
- comportamiento.

### RF-04 — Aparición dinámica

Los elementos deben aparecer mediante un `SpawnSystem`.

El intervalo entre apariciones debe ser variable.

El sistema debe permitir configurar:

- intervalo mínimo;
- intervalo máximo;
- posiciones de salida;
- ángulos;
- velocidades;
- probabilidad de elementos especiales;
- composición del mecato por nivel.

### RF-05 — Bombas / elementos peligrosos

El juego debe permitir la aparición ocasional de bombas u otros elementos peligrosos.

Las bombas no deben otorgar puntos y deben producir una penalización al jugador cuando sean cortadas.

La frecuencia de aparición debe ser configurable.

### RF-06 — Vidas

Cada jugador debe comenzar con un máximo de **5 vidas**.

El sistema no debe permitir superar el límite configurado de 5 vidas.

La pérdida de una vida debe ser claramente comunicada mediante la interfaz.

### RF-07 — Puntuación

El juego debe mantener un contador de puntos.

La puntuación debe depender de las reglas configuradas para cada elemento.

Debe ser posible definir:

- puntos base;
- multiplicadores;
- combos;
- bonificaciones;
- penalizaciones.

### RF-08 — Récords y competencia

El sistema debe almacenar y mostrar récords de puntuación.

El diseño debe permitir comparar resultados entre jugadores.

La persistencia inicial puede ser local. La sincronización remota no forma parte de este alcance salvo que posteriormente se especifique.

### RF-09 — Tiempo

Cada partida debe tener un temporizador.

El tiempo restante debe mostrarse claramente.

El comportamiento del juego debe cambiar progresivamente a medida que disminuye el tiempo.

### RF-10 — Dificultad dinámica

La dificultad debe aumentar durante la partida.

El aumento puede modificar:

- velocidad;
- frecuencia de aparición;
- variedad de objetos;
- frecuencia de bombas;
- trayectorias;
- cantidad simultánea de entidades;
- objetivos.

La dificultad debe ser configurable.

### RF-11 — Niveles

El juego debe tener niveles de dificultad progresiva.

Cada nivel debe poder definir:

- duración;
- dificultad inicial;
- dificultad máxima;
- tipos de mecato;
- velocidad;
- frecuencia de aparición;
- probabilidad de bombas;
- objetivo;
- puntuación mínima;
- condiciones de victoria.

### RF-12 — Objetivos medibles

Cada partida/nivel debe tener objetivos específicos y verificables.

Ejemplos:

- alcanzar determinada puntuación;
- cortar una cantidad de elementos;
- completar un nivel antes de que termine el tiempo;
- conseguir un combo mínimo;
- perder menos de determinada cantidad de vidas.

### RF-13 — Multijugador

El juego debe soportar modo multijugador.

**Supuesto inicial de diseño:** el primer alcance será multijugador local en el mismo equipo, con posibilidad de ampliar posteriormente a multijugador por red.

La arquitectura debe evitar acoplar las reglas del juego a una única fuente de entrada.

### RF-14 — Interfaz

La interfaz debe mostrar como mínimo:

- puntuación;
- vidas;
- tiempo;
- nivel;
- objetivo;
- jugador activo/identificación cuando corresponda.

Debe existir una interfaz diferenciada para:

- menú;
- gameplay;
- pausa;
- victoria;
- derrota;
- resultados.

### RF-15 — Identidad visual

La interfaz debe utilizar colores vivos y llamativos y una ambientación inspirada en mercados y elementos colombianos.

La identidad visual debe ser original.

### RF-16 — Audio

El diseño debe permitir música y efectos de sonido.

Los sonidos deben estar desacoplados de los sistemas de gameplay mediante un servicio/manager de audio.

---

## 3. Requisitos no funcionales

### RNF-01 — Arquitectura ECS

El núcleo del juego debe utilizar Entity Component System.

### RNF-02 — Entity Factory

La creación de entidades debe estar centralizada en `EntityFactory`.

### RNF-03 — Separación de responsabilidades

Los sistemas no deben convertirse en objetos monolíticos.

Cada sistema debe tener una responsabilidad claramente definida.

### RNF-04 — Configuración

Los parámetros de niveles, dificultad, mecato y spawn deben ser configurables externamente mediante JSON siempre que sea razonable.

### RNF-05 — Testabilidad

La lógica que no dependa directamente de Pygame debe poder probarse mediante pruebas automatizadas.

### RNF-06 — Rendimiento

El juego debe mantener una experiencia fluida durante el gameplay.

El objetivo inicial es trabajar alrededor de 60 FPS, sujeto a validación en hardware de referencia.

### RNF-07 — Mantenibilidad

El código debe utilizar nombres claros, módulos pequeños y dependencias explícitas.

### RNF-08 — Extensibilidad

Debe ser posible agregar nuevos tipos de mecato, niveles y elementos especiales sin modificar múltiples sistemas no relacionados.

---

## 4. Alcance inicial

Incluido:

- desktop;
- ECS;
- Factory;
- gameplay;
- machete;
- mecato;
- bombas;
- vidas;
- puntuación;
- tiempo;
- dificultad progresiva;
- niveles;
- objetivos;
- récords locales;
- multijugador local;
- UI;
- audio básico.

Fuera del primer alcance:

- cuentas de usuario;
- servidores;
- matchmaking online;
- ranking global;
- compras;
- monetización;
- backend;
- multijugador online.

Estos elementos pueden convertirse en specs futuras.
