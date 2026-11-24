from taskflow.usuario import Usuario


class Tarea:
    def __init__(self, titulo, descripcion):
        self._estado = "pendiente"
        self._responsable = None
        self._proyecto = None
        self.titulo = titulo
        self.descripcion = descripcion
        
    
    # Cambia el estado de la tarea a "en progreso".
    def iniciar(self):
        if self._estado != "pendiente":
            raise ValueError("La tarea debe estar pendiente")

        if self._responsable is None:
            raise ValueError("La tarea debe tener un responsable asignado")

        self._estado = "en progreso"

    # Cambia el estado de la tarea a "completada".
    def completar(self):
        if self._estado != "en progreso":
            raise ValueError("La tarea debe estar en progreso")

        self._estado = "completada"

    # Asigna o sustituye al responsable de una tarea.
    def asignar_responsable(self, usuario):
        if self._estado == "completada":
            raise ValueError("No se puede modificar el responsable de una tarea completada")

        if not isinstance(usuario, Usuario):
            raise ValueError("El responsable debe ser un Usuario")

        self._responsable = usuario

    # Permite consultar el proyecto al que pertenece la tarea.
    @property
    def proyecto(self):
        return self._proyecto

    # Permite consultar y modificar el título.
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        # Solo se permite modificar el título de tareas pendientes.
        if self._estado != "pendiente":
            raise ValueError("Solo se puede modificar el título de una tarea pendiente")

        if not isinstance(nuevo_titulo, str):
            raise ValueError("El título debe ser una cadena de texto")

        if not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío")

        self._titulo = nuevo_titulo.strip()

    # Permite consultar y modificar la descripción.
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        # No se permite modificar la descripción de tareas completadas.
        if self._estado == "completada":
            raise ValueError("No se puede modificar la descripción de una tarea completada")

        if not isinstance(nueva_descripcion, str):
            raise ValueError("La descripción debe ser una cadena de texto")

        if not nueva_descripcion.strip():
            raise ValueError("La descripción no puede estar vacía")

        self._descripcion = nueva_descripcion.strip()

    # Permite consultar el estado, pero no modificarlo directamente.
    @property
    def estado(self):
        return self._estado

    # Permite consultar el responsable asignado.
    @property
    def responsable(self):
        return self._responsable