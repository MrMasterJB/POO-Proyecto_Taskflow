
# TaskFlow — Análisis mediante inteligencia artificial

## 1. Objetivo

Utilizar la inteligencia artificial como herramienta de apoyo para contrastar el diseño de TaskFlow, identificar posibles problemas y valorar mejoras en el modelo de objetos.

## 2. Prompt de análisis

El siguiente prompt recoge de forma consolidada el planteamiento utilizado durante el análisis del laboratorio.

---

Estoy diseñando una aplicación de gestión de proyectos llamada TaskFlow mediante programación orientada a objetos en Python.

La aplicación debe permitir:

- Crear proyectos.
- Registrar usuarios.
- Crear tareas.
- Asignar tareas a usuarios.
- Cambiar el estado de las tareas.
- Listar las tareas de un responsable concreto.
- Listar los proyectos y sus tareas asociadas.

He identificado tres objetos principales: Proyecto, Tarea y Usuario.

### Estado de los objetos

**Proyecto:**

- nombre: cadena de texto.
- tareas: colección de objetos Tarea.

**Tarea:**

- titulo: cadena de texto.
- descripcion: cadena de texto.
- estado: cadena de texto.
- responsable: objeto Usuario o None.

**Usuario:**

- nombre: cadena de texto.

### Comportamientos

**Proyecto:**

- Consultar y modificar su nombre.
- Consultar las tareas asociadas.
- Añadir tareas.

**Tarea:**

- Consultar y modificar su título.
- Consultar y modificar su descripción.
- Consultar su estado.
- Consultar y asignar su responsable.
- Iniciar la tarea.
- Completar la tarea.

**Usuario:**

- Consultar y modificar su nombre.

### Decisiones iniciales de diseño

- Una tarea comienza en estado pendiente.
- Una tarea puede existir sin responsable asignado.
- Para iniciar una tarea debe tener un responsable.
- Asignar un responsable no implica iniciar la tarea.
- Las transiciones de estado deben seguir un orden establecido:

      pendiente --> en progreso --> completada

- No se permite saltar estados ni retroceder.
- Un proyecto puede contener varias tareas.
- Una tarea únicamente puede pertenecer a un proyecto.
- Un usuario puede ser responsable de varias tareas.
- El usuario no almacena directamente las tareas que tiene asignadas.
- Las relaciones inicialmente planteadas son unidireccionales.
- Se utilizarán getters y setters para gestionar el acceso y la modificación de los atributos.

Analiza este diseño como si fueras un analista de software especializado en programación orientada a objetos.

Indica:

1. Qué decisiones parecen coherentes.
2. Qué responsabilidades podrían estar mal asignadas.
3. Qué información podría faltar.
4. Qué información podría sobrar.
5. Qué problemas podrían aparecer durante la implementación.
6. Qué preguntas debería hacerme antes de programar.

Para este análisis:

- No escribas código.
- No rediseñes la solución completa.
- No introduzcas clases adicionales sin justificar su necesidad.
- No introduzcas conceptos avanzados innecesarios.
- Cuestiona las decisiones que consideres incorrectas.
- Justifica las sugerencias realizadas.
- Si no sabes algo, no te lo inventes.

---

## 3. Comparación entre el diseño inicial y las aportaciones de la IA

### 3.1. Coincidencias

- Identificación de Proyecto, Tarea y Usuario como clases principales.
- Representación del estado como un atributo de Tarea.
- Separación entre la asignación de responsables y los cambios de estado.
- Gestión de las transiciones de estado desde la clase Tarea.
- Gestión de la colección de tareas desde la clase Proyecto.
- Posibilidad de crear tareas sin responsable.
- Ausencia de una colección de tareas dentro de Usuario.

### 3.2. Diferencias y problemas detectados

La IA permitió identificar los siguientes problemas:

1. La colección interna de tareas podía modificarse directamente desde fuera de la clase Proyecto.

2. Una misma instancia de Tarea podía incorporarse varias veces al mismo proyecto.

3. Una misma instancia de Tarea podía incorporarse a diferentes proyectos, incumpliendo la condición de pertenencia exclusiva.

### 3.3. Decisiones modificadas

| Identificador | Sugerencia de la IA | Decisión |
|---|---|---|
| IA-01 | Devolver una copia de la colección de tareas mediante `.copy()`. | Aceptada |
| IA-02 | Comprobar si una instancia de Tarea ya pertenece al proyecto antes de incorporarla. | Aceptada |
| IA-03 | Incorporar una referencia al proyecto dentro de Tarea y establecer una relación bidireccional. | Aceptada |

## 4. Justificación de las decisiones adoptadas

### IA-01. Protección de la colección de tareas

Se acepta la sugerencia para evitar que la colección interna pueda modificarse directamente desde fuera de la clase Proyecto.

De esta manera, la incorporación de tareas debe realizarse mediante el método correspondiente y sus validaciones.

### IA-02. Validación de tareas duplicadas

Se acepta la sugerencia para impedir que una misma instancia de Tarea aparezca varias veces dentro de un proyecto.

Esto no impide que existan tareas diferentes con idéntico título, descripción y responsable.

### IA-03. Pertenencia exclusiva de las tareas

Se acepta la sugerencia de incorporar una referencia al proyecto dentro de la clase Tarea.

Esta modificación permite comprobar si una tarea ya pertenece a otro proyecto antes de incorporarla.

Como consecuencia, la relación inicialmente unidireccional entre Proyecto y Tarea pasa a ser bidireccional.

## 5. Valoración del uso de la IA

La utilización de inteligencia artificial ha permitido contrastar las decisiones de diseño, detectar problemas que no se habían contemplado inicialmente y valorar posibles soluciones.

Las sugerencias se han analizado individualmente antes de incorporarlas al modelo definitivo.

También se ha utilizado la IA como apoyo durante la implementación en Python.

