
# TaskFlow — Análisis y diseño orientado a objetos

## 1. Identificación de objetos

Tras analizar los requisitos de la aplicación, se identifican tres objetos principales:

### Proyecto

Representa un proyecto de trabajo que contiene un conjunto de tareas necesarias para su realización.

Es necesario para organizar y agrupar las tareas relacionadas con un mismo objetivo.

### Tarea

Representa un trabajo concreto que debe realizarse dentro de un proyecto.

Cada tarea dispone de información propia, un estado y la posibilidad de tener un usuario responsable de su realización.

### Usuario

Representa a una persona registrada en la aplicación a la que se le pueden asignar tareas.

No se considera necesario diferenciar entre supervisores y responsables mediante clases independientes, puesto que un mismo usuario puede desempeñar diferentes funciones.

## 2. Estado de los objetos

### 2.1. Proyecto

| Atributo | Tipo | Descripción |
|---|---|---|
| nombre | str | Nombre identificativo del proyecto. |
| tareas | list | Colección de tareas pertenecientes al proyecto. |

Al crear un proyecto, su colección de tareas estará vacía.

### 2.2. Tarea

| Atributo | Tipo | Descripción |
|---|---|---|
| titulo | str | Título identificativo de la tarea. |
| descripcion | str | Descripción del trabajo que debe realizarse. |
| estado | str | Estado actual de la tarea. |
| responsable | Usuario o None | Usuario encargado de realizar la tarea. |
| proyecto | Proyecto o None | Proyecto al que pertenece la tarea. |

Una tarea recién creada tendrá el estado "pendiente", no tendrá ningún responsable asignado y todavía no pertenecerá a ningún proyecto.

Los posibles estados de una tarea son:

- pendiente
- en progreso
- completada

### 2.3. Usuario

| Atributo | Tipo | Descripción |
|---|---|---|
| nombre | str | Nombre identificativo del usuario. |

No se considera necesario que el usuario almacene una colección de las tareas que tiene asignadas, puesto que esta información puede obtenerse consultando las tareas de los proyectos.

## 3. Comportamiento de los objetos

### 3.1. Proyecto

- Consultar su nombre.
- Modificar su nombre.
- Consultar las tareas que contiene.
- Añadir una tarea.

### 3.2. Tarea

- Consultar su título.
- Modificar su título.
- Consultar su descripción.
- Modificar su descripción.
- Consultar su estado.
- Consultar su responsable.
- Asignar o sustituir su responsable.
- Consultar el proyecto al que pertenece.
- Iniciar la tarea.
- Completar la tarea.

### 3.3. Usuario

- Consultar su nombre.
- Modificar su nombre.

## 4. Asignación de responsabilidades

Cada objeto será responsable de gestionar su propia información y los comportamientos directamente relacionados con ella.

| Responsabilidad | Responsable |
|---|---|
| Validar el nombre de un proyecto. | Proyecto |
| Gestionar la colección de tareas de un proyecto. | Proyecto |
| Validar la incorporación de una tarea a un proyecto. | Proyecto |
| Validar el título y la descripción de una tarea. | Tarea |
| Gestionar los cambios de estado de una tarea. | Tarea |
| Gestionar la asignación de responsables. | Tarea |
| Validar el nombre de un usuario. | Usuario |
| Crear proyectos. | Aplicación principal (main.py) |
| Crear tareas. | Aplicación principal (main.py) |
| Registrar usuarios. | Aplicación principal (main.py) |
| Listar proyectos y sus tareas. | Aplicación principal (main.py) |
| Listar las tareas de un usuario. | Aplicación principal (main.py) |

Se ha decidido que la asignación de un responsable y el inicio de una tarea sean comportamientos independientes.

Por tanto, asignar un responsable no implica que la tarea haya comenzado.

## 5. Modelo conceptual

### 5.1. Relación entre Proyecto y Tarea

- Un proyecto puede contener ninguna, una o varias tareas.
- Una tarea puede existir antes de incorporarse a un proyecto.
- Una tarea únicamente puede pertenecer a un proyecto.
- Un proyecto conoce las tareas que contiene.
- Una tarea conoce el proyecto al que pertenece.

### 5.2. Relación entre Tarea y Usuario

- Una tarea puede tener un único usuario responsable.
- Una tarea puede existir sin responsable.
- Un usuario puede ser responsable de varias tareas.
- Una tarea conoce al usuario que tiene asignado.
- Un usuario no almacena directamente las tareas que tiene asignadas.

### 5.3. Representación conceptual

    Proyecto  <---------->  Tarea  ---------->  Usuario
       0..1                  0..*
    
    Tarea  ------------------------------->  Usuario
    0..*                                       0..1

La relación entre Proyecto y Tarea es bidireccional, mientras que la relación entre Tarea y Usuario es unidireccional.

## 6. Decisiones de diseño

### 6.1. Validación de datos

Los nombres de proyectos y usuarios, así como los títulos y descripciones de las tareas, deben ser cadenas de texto no vacías.

Se eliminarán los espacios exteriores de las cadenas introducidas.

Los datos no válidos provocarán una excepción ValueError.

### 6.2. Gestión de los estados de una tarea

El estado de una tarea se representa mediante una cadena de texto.

Las transiciones permitidas son:

    pendiente --> en progreso --> completada

No se permite saltar estados ni retroceder a un estado anterior.

Para iniciar una tarea será necesario que:

- La tarea se encuentre en estado pendiente.
- La tarea tenga un responsable asignado.

Para completar una tarea será necesario que se encuentre en estado en progreso.

### 6.3. Restricciones según el estado de la tarea

| Operación | Pendiente | En progreso | Completada |
|---|---|---|---|
| Modificar el título | Sí | No | No |
| Modificar la descripción | Sí | Sí | No |
| Asignar o sustituir responsable | Sí | Sí | No |
| Retirar responsable | No | No | No |
| Iniciar tarea | Sí, con responsable | No | No |
| Completar tarea | No | Sí | No |

Una vez completada una tarea, no se permitirá modificar su título, descripción, responsable ni estado.

### 6.4. Identidad de las tareas

Dos tareas pueden tener el mismo título, descripción y responsable sin representar el mismo trabajo.

Por ejemplo, pueden existir dos proyectos:

- Pintado de una casa.
- Pintado de una habitación.

Ambos proyectos pueden contener una tarea denominada "Acopio de pintura", con la misma descripción y el mismo responsable.

Sin embargo, cada tarea representa un trabajo diferente y debe disponer de su propio estado.

Por este motivo, se utilizarán instancias independientes de la clase Tarea.

### 6.5. Pertenencia a proyectos

Una misma instancia de Tarea no podrá incorporarse varias veces al mismo proyecto ni pertenecer simultáneamente a varios proyectos.

Sí se permitirá que existan diferentes instancias de Tarea con atributos idénticos.

### 6.6. Encapsulación básica

Se utilizarán atributos internos, getters y setters para controlar el acceso y la modificación de la información de los objetos.

El estado, el responsable y el proyecto de una tarea no dispondrán de setter público.

La colección de tareas de un proyecto tampoco dispondrá de setter público.

### 6.7. Organización de la aplicación

Cada clase se implementará en un archivo independiente:

- usuario.py
- tarea.py
- proyecto.py

El archivo main.py será el encargado de crear los objetos, relacionarlos y demostrar el funcionamiento de la aplicación.

Para esta primera implementación se utilizarán objetos previamente definidos en el código, sin desarrollar una interfaz interactiva.

### 6.8. Requisitos de ampliación

Para listar las tareas de un usuario concreto, se recorrerán los proyectos y sus respectivas tareas, comprobando el responsable asignado a cada una.

Para listar los proyectos y sus tareas asociadas, se recorrerá la colección de proyectos y la colección de tareas de cada proyecto.

No se considera necesario incorporar nuevas clases para implementar estos comportamientos.

## 7. Análisis y aportaciones de la inteligencia artificial

Durante el desarrollo del laboratorio se ha utilizado inteligencia artificial como herramienta de apoyo para contrastar el análisis, detectar posibles problemas de diseño y colaborar en la implementación.

### 7.1. Coincidencias

El análisis realizado con la IA permitió confirmar las siguientes decisiones:

- Utilizar Proyecto, Tarea y Usuario como clases principales.
- Considerar el estado como un atributo de Tarea.
- Permitir la existencia de tareas sin responsable asignado.
- Separar la asignación de responsables de los cambios de estado.
- Asignar a Tarea la responsabilidad de gestionar sus estados.
- Asignar a Proyecto la responsabilidad de gestionar su colección de tareas.
- Evitar almacenar una colección de tareas dentro de Usuario.

### 7.2. Diferencias y problemas detectados

Durante el análisis se identificaron tres aspectos que podían mejorarse:

- La posibilidad de modificar externamente la colección interna de tareas de un proyecto.
- La posibilidad de incorporar varias veces una misma instancia de Tarea a un proyecto.
- La posibilidad de incorporar una misma instancia de Tarea a diferentes proyectos.

### 7.3. Cambios realizados después de utilizar IA

#### IA-01. Protección de la colección de tareas

**Sugerencia de la IA:**

Utilizar el método .copy() al consultar la colección de tareas de un proyecto.

**Justificación:**

Devolver directamente la lista interna permitiría añadir o eliminar elementos sin utilizar los métodos de la clase Proyecto.

**Decisión:**

Se acepta la sugerencia y se implementa una copia superficial de la lista.

#### IA-02. Validación de tareas duplicadas

**Sugerencia de la IA:**

Comprobar si una instancia de Tarea ya pertenece a la colección de tareas antes de incorporarla.

**Justificación:**

Evitar que una misma instancia pueda aparecer varias veces dentro de un proyecto.

**Decisión:**

Se acepta la sugerencia y se incorpora la correspondiente validación al método añadir_tarea().

Se permite que diferentes instancias tengan el mismo título, descripción y responsable.

#### IA-03. Pertenencia exclusiva de las tareas

**Sugerencia de la IA:**

Incorporar un atributo a la clase Tarea que permita identificar el proyecto al que pertenece.

**Justificación:**

La relación unidireccional planteada inicialmente no permitía controlar desde el propio modelo si una tarea ya pertenecía a otro proyecto.

**Decisión:**

Se acepta la sugerencia y se establece una relación bidireccional entre Proyecto y Tarea.

De esta manera, se puede impedir que una misma instancia de Tarea pertenezca simultáneamente a varios proyectos.

## 8. Verificación de la implementación

Se ha ejecutado el archivo main.py para comprobar el funcionamiento conjunto de las clases.

Durante la ejecución se han demostrado los siguientes comportamientos:

- Creación de proyectos.
- Registro de usuarios.
- Creación de tareas.
- Incorporación de tareas a proyectos.
- Asignación de responsables.
- Cambios de estado.
- Existencia de tareas sin responsable.
- Independencia de tareas con atributos idénticos.
- Listado de proyectos y sus tareas.
- Listado de tareas de un usuario concreto.

La ejecución ha proporcionado los resultados esperados.


## 9. Conclusión

El modelo desarrollado permite representar los objetos principales de una aplicación básica de gestión de proyectos, estableciendo sus atributos, comportamientos, responsabilidades y relaciones.

