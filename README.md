# Para la visualizacion del proyecto visitar el sitio web:

El proyecto del repositorio tiene una pagina web en Github  con el link:
"https://reynoldsdarwin.github.io/LP2-POO/"

# Proyecto LP2-POO 

Este proyecto contiene ejemplos y ejercicios prácticos de Programación Orientada a Objetos (POO) en Python, desarrollados para el curso de Lenguaje de Programación II. El objetivo es mostrar conceptos clave de POO como encapsulamiento, herencia, polimorfismo y relaciones entre clases, aplicados en distintos contextos y problemas.

## Estructura del Proyecto

La carpeta principal `LP2-POO` está organizada en subcarpetas, cada una dedicada a un tema o conjunto de ejercicios específicos:

### 1. **RelacionesDeClase**
Contiene ejemplos de relaciones entre clases como asociación, agregación y composición.  
**Ejemplo destacado:**  
- `53-Estudiante.py`: Simula la gestión de estudiantes, profesores, cursos y universidades, mostrando cómo se relacionan entre sí.

### 2. **Encapsulamiento**
Ejercicios que demuestran el uso de atributos privados y métodos para proteger la información de los objetos.

### 3. **Herencia**
Ejemplos donde las clases heredan atributos y métodos de otras clases, mostrando la reutilización y extensión de código.

### 4. **Polimorfismo**
Ejercicios donde diferentes clases implementan métodos con el mismo nombre pero comportamientos distintos.

### 5. **Otros Ejercicios**
Incluye problemas variados de POO, como calculadoras, figuras geométricas, y más.

## Ejemplo de Uso

En el archivo `RelacionesDeClase/53-Estudiante.py` se puede ver cómo crear objetos de las clases `Estudiante`, `Profesor`, `Curso` y `Universidad`, inscribir estudiantes en cursos y mostrar la información de todos los cursos y estudiantes.

```python
# Crear profesores, cursos y estudiantes
profe1 = Profesor("Ing. Juan Carlos", "01323043", "Programación")
curso1 = Curso("Lenguaje de Programación II", profe1)
est1 = Estudiante("Milena Kely", "013123456", "2025007")

# Inscribir estudiante en curso
est1.inscribirse(curso1)

# Mostrar información
curso1.mostrar_detalles()
est1.mostrar_informacion()
```

## Requisitos

- Python 3.7 o superior
- No se requieren librerías externas

## Ejecución

Puedes ejecutar cualquier archivo `.py` desde la terminal con:

```sh
python nombre_del_archivo.py
```

## Autoría

Desarrollado por estudiantes de la Universidad Nacional del Altiplano para el curso de Lenguaje de Programación II.

---

**¡Explora las carpetas y archivos para aprender y practicar POO en Python!**
