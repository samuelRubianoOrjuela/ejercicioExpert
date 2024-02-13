import os

head = """
======================
| MODULO DE REPORTES |
======================"""

menu = """
1. Campers que se encuentren en estado de inscrito.
2. Campers que aprobaron el examen inicial.
3. Trainers que se encuentran trabajando con campuslands.
4. Estudiantes que cuentan con bajo rendimiento.
5. Rutas de entrenamiento.
6. Reporte de modulos
7. Salir al menu principal"""

trainers = {
    'trainer1': {
        'trainer': 'Trainer 1',
        'ruta': 'NodeJS',
        'aula': 'Apolo'
    },
    'trainer2': {
        'trainer': 'Trainer 2',
        'ruta': 'Java',
        'aula': 'Artemis'
    },
    'trainer3': {
        'trainer': 'Trainer 3',
        'ruta': 'NetCore',
        'aula': 'Sputnik'
    }
}

rutas = ["NodeJS","Artemis","Sputnik","Salir"]

def reportes(data):
    isActiveReportes = True
    while (isActiveReportes):
        os.system("cls")
        print(head)
        print(menu)
        try:
            opMenuReportes = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (opMenuReportes == 1):
                os.system("cls")
                print("Campers en estado de inscrito:")
                for dict in data.values():
                    if (dict['estado'] == 'inscrito'):
                        print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
                os.system("pause")
            elif (opMenuReportes == 2):
                os.system("cls")
                print("Campers aprobados:")
                for dict in data.values():
                    if (dict['estado'] == 'aprobado'):
                        print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
                os.system("pause")
            elif (opMenuReportes == 3):
                os.system("cls")
                print("Trainers:\n")
                for dict in trainers.values():
                    for item, valor in dict.items():
                        if ( item != 'aula'):
                            print(f"{item}: {valor}")
                        else:
                            print(f"{item}: {valor}\n")
                os.system("pause")
            elif (opMenuReportes == 4):
                os.system("cls")
                print("Estudiantes en riesgo:")
                for dict in data.values():
                    if ('riesgo' in dict):
                        print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']}, nota del Modulo: {dict['notaModulo']}")
                os.system("pause")
            elif (opMenuReportes == 5):
                isActiveRutas = True
                while (isActiveRutas):
                    os.system("cls")
                    print("Rutas de entrenamiento.")
                    for i, indice in enumerate(rutas):
                        print(f"{i+1}. {indice}")
                    try:
                        opMenuRutas = int(input(("->")))
                    except ValueError:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
                    else:
                        if (opMenuRutas == 1):
                            os.system("cls")
                            print("NodeJS:\nTrainer: Trainer 1")
                            for dict in data.values():
                                if ("NodeJS" in dict.values()):
                                    print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
                            print("Fecha entrada: Enero 5\nFecha salida: Octubre 10")
                            os.system("pause")
                        elif (opMenuRutas == 2):
                            os.system("cls")
                            print("Java:\nTrainer: Trainer 2")
                            for dict in data.values():
                                if ("Java" in dict.values()):
                                    print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
                            print("Fecha entrada: Marzo 28\nFecha salida: Enero 30")
                            os.system("pause")
                        elif (opMenuRutas == 3):
                            os.system("cls")
                            print("NetCore:\nTrainer: Trainer 3")
                            for dict in data.values():
                                if ("NetCore" in dict.values()):
                                    print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
                            print("Fecha entrada: Agosto 15\nFecha salida: Junio 21")
                            os.system("pause")
                        elif (opMenuRutas == 4):
                            isActiveRutas = False
                        else:
                            print("El valor ingresado no es valido, intentelo de nuevo.")
                            os.system("pause")
            elif (opMenuReportes == 6):
                isActiveRepM = True
                while (isActiveRepM):
                    os.system("cls")
                    print("Reporte del Modulo.")
                    for i, indice in enumerate(rutas):
                        print(f"{i+1}. {indice}")
                    try:
                        opMenuRutas = int(input(("->")))
                    except ValueError:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
                    else:
                        if (opMenuRutas == 1):
                            aprobadosJS = False
                            reprobadosJS = False
                            os.system("cls")
                            print("Reporte del modulo.")
                            print("NodeJS:\nTrainer: Trainer 1")
                            print("Estudiantes que aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "NodeJS" and "riesgo" not in dict):
                                    aprobadosJS = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not aprobadosJS):
                                print("No se encontraron estudiantes aprobados en esta ruta.")
                            print("Estudiantes que no aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "NodeJS" and "riesgo" in dict):
                                    reprobadosJS = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not reprobadosJS):
                                print("No se encontraron estudiantes reprobados en esta ruta.")
                            os.system("pause")
                        elif (opMenuRutas == 2):
                            aprobadosJava = False
                            reprobadosJava = False
                            os.system("cls")
                            print("Reporte del modulo.")
                            print("Java:\nTrainer: Trainer 1")
                            print("Estudiantes que aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "Java" and "riesgo" not in dict):
                                    aprobadosJava = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not aprobadosJava):
                                print("No se encontraron estudiantes aprobados en esta ruta.")
                            print("Estudiantes que no aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "Java" and "riesgo" in dict):
                                    reprobadosJava = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not reprobadosJava):
                                print("No se encontraron estudiantes reprobados en esta ruta.")
                            os.system("pause")
                        elif (opMenuRutas == 3):
                            aprobadosNet = False
                            reprobadosNet = False
                            os.system("cls")
                            print("Reporte del modulo.")
                            print("NetCore:\nTrainer: Trainer 1")
                            print("Estudiantes que aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "NetCore" and "riesgo" not in dict):
                                    aprobadosNet = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not aprobadosNet):
                                print("No se encontraron estudiantes aprobados en esta ruta.")
                            print("Estudiantes que no aprobaron el modulo:")
                            for dict in data.values():
                                if (dict['ruta'] == "NetCore" and "riesgo" in dict):
                                    reprobadosNet = True
                                    print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']} Nota del Modulo: {dict['notaModulo']}")
                            if (not reprobadosNet):
                                print("No se encontraron estudiantes reprobados en esta ruta.")
                            os.system("pause")
                        elif (opMenuRutas == 4):
                            isActiveRepM = False
                        else:
                            print("El valor ingresado no es valido, intentelo de nuevo.")
                            os.system("pause")
            elif (opMenuReportes == 7):
                isActiveReportes = False
            else:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")

# COMPLETO