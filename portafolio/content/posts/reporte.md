---
title: "Reporte: Markdown, Git, GitHub, Hugo y GitHub Actions"
date: 2026-02-20
draft: false
---

# Reporte: Markdown, Git, GitHub, Hugo y GitHub Actions

**Alumno:** Fabricio Reyes  
**Materia:** Paradigmas de la programación  
**Profesor:** Jose Carlos Gallegos Mariscal  
**Fecha:** 20/02/2026  

---

# Introducción

En el presente reporte se documenta el aprendizaje adquirido durante tres sesiones enfocadas en herramientas fundamentales para el desarrollo moderno de software y publicación web. Se estudió el uso de Markdown para documentación, Git y GitHub para control de versiones, y finalmente Hugo junto con GitHub Actions para la generación y publicación automática de sitios web estáticos.

Estas herramientas son ampliamente utilizadas en entornos profesionales basados en Linux, Unix y servicios en la nube.

---

# Primera Sesión: Markdown

## ¿Qué es Markdown?

Markdown es un lenguaje de marcado ligero que permite dar formato a texto plano de manera sencilla. Fue creado por John Gruber con el objetivo de convertir texto simple en HTML estructurado sin complicaciones.

Es ampliamente utilizado para:

- Documentación técnica  
- Archivos README  
- Blogs  
- Portafolios  
- Sitios web estáticos  

---

## Sintaxis Básica de Markdown

### Encabezados

```markdown
# Título nivel 1
## Título nivel 2
### Título nivel 3
```

### Negritas y cursivas

```markdown
**Texto en negrita**
*Texto en cursiva*
```

### Listas

Lista no ordenada:

```markdown
- Elemento 1
- Elemento 2
- Elemento 3
```

Lista ordenada:

```markdown
1. Paso uno
2. Paso dos
3. Paso tres
```

### Enlaces

```markdown
[GitHub](https://github.com)
```

### Código en línea

```markdown
`printf("Hola mundo");`
```

### Bloques de código

```c
#include <stdio.h>

int main() {
    printf("Hola mundo");
    return 0;
}
```

---

# Segunda Sesión: Git y GitHub

## ¿Qué es Git?

Git es un sistema de control de versiones distribuido creado por Linus Torvalds. Permite registrar cambios en archivos y proyectos a lo largo del tiempo.

Con Git podemos:

- Controlar versiones  
- Trabajar en equipo  
- Recuperar versiones anteriores  
- Gestionar ramas de desarrollo  

---

## ¿Qué es GitHub?

GitHub es una plataforma en la nube que permite alojar repositorios Git. Facilita la colaboración, el almacenamiento remoto y la publicación de proyectos.

Repositorio del proyecto:

https://github.com/zFabricio7/portafolio

---

## Comandos utilizados en el proyecto

Inicializar repositorio:

```bash
git init
```

Ver estado:

```bash
git status
```

Agregar archivos:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Primer commit del portafolio"
```

Conectar repositorio con GitHub:

```bash
git remote add origin https://github.com/zFabricio7/portafolio.git
```

Subir cambios:

```bash
git branch -M main
git push -u origin main
```

---

# Tercera Sesión: Hugo y GitHub Actions

## ¿Qué es Hugo?

Hugo es un generador de sitios web estáticos desarrollado en Go. Permite crear sitios web rápidos utilizando archivos Markdown como contenido principal.

Es ideal para:

- Blogs  
- Portafolios  
- Documentación técnica  

---

## Creación del sitio en Hugo

Crear sitio:

```bash
hugo new site portafolio
cd portafolio
```

Crear contenido:

```bash
hugo new posts/reporte.md
```

Ejecutar servidor local:

```bash
hugo server
```

El sitio se ejecuta en:

http://localhost:1313

---

## ¿Qué es GitHub Actions?

GitHub Actions es una herramienta de automatización integrada en GitHub que permite ejecutar procesos automáticamente cuando se realizan cambios en un repositorio.

En este proyecto se utiliza para:

- Construir automáticamente el sitio Hugo  
- Publicarlo en GitHub Pages  

---

## Publicación en GitHub Pages

Pasos realizados:

1. Subir el proyecto al repositorio en GitHub.
2. Ir a Settings → Pages.
3. Seleccionar "GitHub Actions" como método de publicación.
4. Configurar el workflow para construir el sitio con Hugo.
5. Realizar push para activar la publicación automática.

Página publicada:

https://zfabricio7.github.io/portafolio/

---

# Conclusión

Durante estas sesiones se adquirieron conocimientos fundamentales para el desarrollo profesional en ingeniería de software. Markdown facilita la documentación estructurada, Git permite el control de versiones, GitHub ofrece almacenamiento y colaboración en la nube, Hugo permite generar sitios estáticos eficientes y GitHub Actions automatiza su publicación.

El dominio de estas herramientas es esencial en entornos profesionales basados en Linux, servicios en la nube y desarrollo colaborativo moderno.

---

# Conversión a PDF

Para convertir este archivo Markdown a PDF se utilizó la extensión "Markdown PDF" en Visual Studio Code.

Prueba 47.