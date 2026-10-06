# Requirements — Spawn System

## Objetivo
Controlar la aparición dinámica de mecato y bombas.

## Requisitos
- R1. Generar entidades a intervalos variables.
- R2. Configurar intervalo mínimo y máximo.
- R3. Variar posición de salida.
- R4. Variar ángulo de impulso.
- R5. Variar velocidad inicial.
- R6. Seleccionar diferentes tipos de mecato.
- R7. Permitir aparición ocasional de bombas.
- R8. La probabilidad de bomba debe ser configurable.
- R9. SpawnSystem debe utilizar EntityFactory.
- R10. SpawnSystem no debe controlar la física después de crear la entidad.

## Criterios de aceptación
- Las apariciones no utilizan un intervalo fijo.
- Las velocidades están dentro del rango configurado.
- Los ángulos están dentro del rango configurado.
- Una probabilidad 0 impide bombas.
- Una probabilidad 1 permite generar bombas, respetando las reglas configuradas.
