class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

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
        
        
        