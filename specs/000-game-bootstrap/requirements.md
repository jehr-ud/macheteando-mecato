# Requirements — Game Bootstrap

## Objetivo

Crear el punto de entrada y bootstrap de la aplicación Macheteando.

## Requisitos

- R1. El proyecto debe tener un `main.py` en la raíz.
- R2. `main.py` debe exponer una función `main()`.
- R3. `main.py` debe crear la instancia principal de `Game`.
- R4. `main.py` debe iniciar el método `run()`.
- R5. `main.py` no debe contener lógica de gameplay.
- R6. La clase `Game` debe controlar el ciclo principal de ejecución.
- R7. La inicialización debe permitir posteriormente conectar SceneManager y ECS World.

## Criterios de aceptación

Ejecutar:

```bash
python main.py
```

debe iniciar la aplicación sin que `main.py` contenga lógica específica de frutas, bombas, puntuación o física.
