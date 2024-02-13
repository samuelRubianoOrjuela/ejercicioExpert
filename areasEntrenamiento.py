import os

def opciones(data, sala, salaBool):
    for dict in data.values():
        if (sala in dict.values()):
            salaBool = True
    if (salaBool):
        os.system(("cls"))
        print(f"Estudiantes que se encuentran en la sala {sala}:")
        for dict in data.values():
            if ('aula' in dict and dict['aula'] == sala):
                print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
        os.system("pause")
    else:
        print("No se encuentra ningun Camper registrado en esta aula.")
        os.system("pause")

def aulas(data):
    isActiveAulas = True
    while (isActiveAulas):
        salones = ["Apolo","Artemis","Sputnik","Salir al menu principal"]
        os.system("cls")
        print("Areas de Entrenamiento.")
        for i, item in enumerate(salones):
            print(f"{i+1}. {item}")
        try:
            opMenuAulos = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (opMenuAulos == 1):
                apolo = False
                opciones(data, "Apolo", apolo)
            elif (opMenuAulos == 2):
                artemis = False
                opciones(data, "Artemis", artemis)
            elif (opMenuAulos == 3):
                sputnik = False
                opciones(data, "Sputnik", sputnik)
            elif (opMenuAulos == 4):
                isActiveAulas = False
            else:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")

# COMPLETO