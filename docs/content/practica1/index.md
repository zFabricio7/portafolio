---
title: "Práctica 01: Cola de impresión en lenguaje C"
date: 2026-03-13
draft: false
weight: 2
---

# Práctica 01: Cola de impresión en lenguaje C

**Alumno:** Fabricio Reyes  
**Materia:** Paradigmas de la programación  
**Profesor:** José Carlos Gallegos Mariscal  
**Grupo:** 941  
**Fecha:** 13/03/2026  

---

# Introducción

En la presente práctica se desarrolló un simulador de cola de impresión utilizando el lenguaje de programación C. El objetivo principal fue comprender el funcionamiento de las estructuras de datos tipo cola (Queue) y su aplicación en sistemas reales como los sistemas de impresión.

Una cola sigue el principio **FIFO (First In, First Out)**, lo cual significa que el primer elemento en entrar es el primero en salir. Este comportamiento es común en diversos sistemas informáticos como colas de procesos, colas de red y colas de impresión.

Durante la práctica se implementaron tres versiones del sistema:

1. Implementación con **memoria estática**
2. Implementación con **memoria dinámica**
3. **Simulación del proceso de impresión**

Además, se analizaron conceptos importantes del lenguaje C como el manejo de memoria, el alcance de variables, el uso de estructuras y el diseño de funciones.

---

# Diseño del sistema

## Estructura de los trabajos de impresión

Cada trabajo de impresión se representa mediante una estructura que almacena la información necesaria para el proceso de impresión.

```c
#define MAX_USER 32
#define MAX_DOC 48

typedef enum { NORMAL=0, URGENTE=1 } Prioridad_t;

typedef enum {
    EN_COLA=0,
    IMPRIMIENDO=1,
    COMPLETADO=2,
    CANCELADO=3
} Estado_t;

typedef struct {
    int id;
    char usuario[MAX_USER];
    char documento[MAX_DOC];
    int paginas_total;
    int paginas_restantes;
    int copias;
    Prioridad_t prioridad;
    Estado_t estado;
    int ms_por_pagina;
} PrintJob_t;
} PrintJob_t;
