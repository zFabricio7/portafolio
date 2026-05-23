---
title: "Práctica 3: Markdown, Git, GitHub, Hugo y GitHub Actions"
date: 2026-05-01
draft: false
weight: 4
---

# Reporte: Instalación y uso de Haskell

**Alumno:** Fabricio Reyes Villavicencio
**Materia:** Paradigmas de la programación  
**Profesor:** José Carlos Gallegos Mariscal  
**Grupo:** 941   
**Fecha:** 01/05/2028  

---

# Primera sesión

## Instalación del entorno de desarrollo

Para comenzar la práctica ingresé al sitio oficial de Haskell y posteriormente a la sección Downloads.

Dentro de la página utilicé la herramienta GHCup, la cual permite instalar automáticamente todas las herramientas necesarias para trabajar con Haskell.

El procedimiento que realicé fue el siguiente:

1. Entré a la página oficial de Haskell.
2. Abrí la sección Downloads.
3. Di clic en el enlace GHCup.
4. Copié el comando de instalación para Windows.
5. Abrí PowerShell sin permisos de administrador.
6. Pegué el comando y ejecuté la instalación.

Durante el proceso instalé las siguientes herramientas:

## Ghcup

Herramienta utilizada para instalar y administrar el entorno de desarrollo de Haskell.

## Ghc

Compilador principal de Haskell.

## Hugs

Intérprete interactivo para ejecutar código Haskell.

## Hls

Haskell Language Server. Proporciona soporte para editores de código y contiene librerías utilizadas por otras herramientas.

## Stack

Administrador de proyectos y dependencias.

## Cabal

Herramienta utilizada para compilar proyectos y empaquetar aplicaciones.

También aprendí que los archivos fuente de Haskell utilizan la extensión `.hs`.

---

# Verificación de instalación

Después de finalizar la instalación ejecuté los siguientes comandos en PowerShell para confirmar que las herramientas funcionaban correctamente:

```powershell
ghc --version
stack --version
cabal --version
```

Los comandos mostraron correctamente las versiones instaladas, confirmando que el entorno funcionaba correctamente.

---

# Segunda sesión

## Introducción a Haskell

Posteriormente revisé la guía “Haskell Tutorial for C Programmers”, donde se explican las diferencias entre la programación imperativa y la programación funcional.

Entre los conceptos que aprendí destacan:

- Uso de funciones como elemento principal.
- Variables inmutables.
- Tipado fuerte y estático.
- Uso de recursividad.
- Evaluación funcional.

También revisé un tour de sintaxis de Haskell para comprender mejor la estructura del lenguaje.

---

# Aplicación TODO en Haskell

La práctica incluyó revisar una aplicación TODO escrita en Haskell utilizando Stack.

La aplicación permite:

- Agregar tareas.
- Mostrar tareas.
- Eliminar tareas.
- Guardar información.

Para crear el proyecto utilicé el siguiente comando:

```powershell
stack new todo-app
```

Después ingresé a la carpeta del proyecto:

```powershell
cd todo-app
```

Posteriormente compilé el proyecto:

```powershell
stack build
```

Finalmente ejecuté la aplicación:

```powershell
stack run
```

La aplicación utiliza archivos con extensión `.hs` y funciones escritas en Haskell.

---

# Ejemplo básico en Haskell

```haskell
main :: IO ()
main = putStrLn "Hola Mundo desde Haskell"
```

---

# Conclusión

Durante esta práctica aprendí a instalar y configurar el entorno de desarrollo de Haskell utilizando GHCup.

También conocí herramientas importantes como GHC, Stack y Cabal, las cuales permiten administrar, compilar y ejecutar proyectos escritos en Haskell.

Además, revisé conceptos básicos del paradigma funcional y el funcionamiento de una aplicación TODO.

Aunque Haskell posee una sintaxis diferente a otros lenguajes como C, considero que es un lenguaje potente y muy interesante para desarrollar aplicaciones mediante el uso de funciones.