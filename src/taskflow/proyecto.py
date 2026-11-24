from taskflow.tarea import Tarea


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self._tareas = []

    # Permite consultar y modificar el nombre del proyecto.
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto")

        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        self._nombre = nuevo_nombre.strip()

    # Permite consultar las tareas sin modificar la lista interna.
    @property
    def tareas(self):
        return self._tareas.copy()

    # Añade una tarea al proyecto previa validación.
    def añadir_tarea(self, tarea):
        if not isinstance(tarea, Tarea):
            raise ValueError("Debe ser un objeto de tipo Tarea")

        if tarea in self._tareas:
            raise ValueError("La tarea ya pertenece al proyecto")

        if tarea.proyecto is not None:
            raise ValueError("La tarea ya pertenece a otro proyecto")

        self._tareas.append(tarea)
        tarea._proyecto = self