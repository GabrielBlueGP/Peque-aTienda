# Pequeña Tienda en Python

Este es un proyecto personal realizado con fines de práctica y refuerzo en programación en Python. Fue desarrollado en base a la materia **Introducción a la Algoritmia**, parte del plan de mi carrera en la **UADE**.

## Objetivo

Simular una tienda simple, aplicando solo conceptos básicos del lenguaje, usando lógica, y evitando el uso de herramientas avanzadas.

## Características y funciones

- Compra de productos desde distintos catálogos
- Manejo de una billetera personal
- Gestión de inventario
- Reventa de productos adquiridos

## Contenidos aplicados

- Variables
- Condicionales (`if`, `elif`, `else`)
- Bucles (`for`, `while`)
- Listas
- Funciones
- Librería `random` (para generar valores aleatorios)

## Herramientas utilizadas

- Visual Studio Code
- Python (sin librerías externas)

## Estructura y secuencia del código

El programa se ejecuta en consola y presenta un menú principal con acceso a varios submenús:

1. Gestión de billetera:
   - Ver saldo
   - Recargar billetera

2. Visualización de productos por categoría:
   - Ver los catálogos
   - Realizar compras

3. Gestión del inventario:
   - Ver contenido
   - Calcular valor total
   - Vender productos

Todos los submenús permiten volver al menú principal para seguir realizando tareas.  
El programa finaliza al seleccionar la opción de salida desde el menú principal.

## Repositorio

Este proyecto está disponible en:  
[https://github.com/GabrielBlueGP/Peque-aTienda](https://github.com/GabrielBlueGP/Peque-aTienda)

---

## Notas y consideraciones

1. El programa se maneja completamente mediante listas, debido al uso constante de funciones.
2. La billetera inicia siempre en **$0**. Si se desea modificar este valor inicial, debe editarse directamente la lista que la representa.
3. Algunas situaciones de error o invalidez están acompañadas de un listado con posibles causas, debido a la limitación impuesta de usar únicamente estructuras básicas.
