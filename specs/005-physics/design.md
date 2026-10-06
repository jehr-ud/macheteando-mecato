# Design — Physics System

El sistema consulta:

```text
Transform + Velocity
```

y actualiza:

```text
position += velocity * dt
velocity += gravity * dt
```

La gravedad debe ser configurable.

El sistema no conoce el tipo concreto de entidad.
