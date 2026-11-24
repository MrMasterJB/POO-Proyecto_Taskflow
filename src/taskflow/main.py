from taskflow.usuario import Usuario
from taskflow.tarea import Tarea
from taskflow.proyecto import Proyecto


def main() -> None:

    # 1. Registro de usuarios.
    usuario1 = Usuario("Pedro")
    usuario2 = Usuario("María")

    usuarios = [usuario1, usuario2]

    # 2. Creación de proyectos.
    proyecto1 = Proyecto("Pintado de casa")
    proyecto2 = Proyecto("Pintado de habitación")

    proyectos = [proyecto1, proyecto2]

    # 3. Creación de tareas.
    tarea1 = Tarea(
        "Acopio de pintura",
        "Recoger los botes de pintura"
    )

    tarea2 = Tarea(
        "Pintado de paredes",
        "Pintar las paredes de la casa"
    )

    tarea3 = Tarea(
        "Acopio de pintura",
        "Recoger los botes de pintura"
    )

    tarea4 = Tarea(
        "Pintado de techo",
        "Pintar el techo de la habitación"
    )

    # 4. Incorporación de tareas a los proyectos.
    proyecto1.añadir_tarea(tarea1)
    proyecto1.añadir_tarea(tarea2)

    proyecto2.añadir_tarea(tarea3)
    proyecto2.añadir_tarea(tarea4)

    # 5. Asignación de responsables.
    tarea1.asignar_responsable(usuario1)
    tarea2.asignar_responsable(usuario2)
    tarea3.asignar_responsable(usuario1)

    # 6. Modificación del estado de las tareas.
    tarea1.iniciar()
    tarea1.completar()

    tarea2.iniciar()

    # 7. Listado de usuarios registrados.
    print("\n--- USUARIOS REGISTRADOS ---")

    for usuario in usuarios:
        print(usuario.nombre)

    # 8. Listado de proyectos y tareas asociadas.
    print("\n--- PROYECTOS Y TAREAS ---")

    for proyecto in proyectos:
        print(f"\nProyecto: {proyecto.nombre}")

        for tarea in proyecto.tareas:
            print(f"  Tarea: {tarea.titulo}")
            print(f"  Descripción: {tarea.descripcion}")
            print(f"  Estado: {tarea.estado}")

            if tarea.responsable is None:
                print("  Responsable: Sin asignar")
            else:
                print(f"  Responsable: {tarea.responsable.nombre}")

            print()

    # 9. Listado de tareas de un responsable concreto.
    responsable = usuario1

    print(f"\n--- TAREAS DE {responsable.nombre.upper()} ---")

    for proyecto in proyectos:
        for tarea in proyecto.tareas:
            if tarea.responsable is responsable:
                print(f"Proyecto: {proyecto.nombre}")
                print(f"Tarea: {tarea.titulo}")
                print(f"Estado: {tarea.estado}")
                print()


if __name__ == "__main__":
    main()