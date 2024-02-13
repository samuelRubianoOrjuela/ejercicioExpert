import os

def opciones(data, trainer, trainerBool):
    for dict in data.values():
        if (trainer in dict.values()):
            trainerBool = True
    if trainerBool:
        os.system(("cls"))
        print(f"Estudiantes que se encuentran en la sala {trainer}:")
        for dict in data.values():
            if ('trainer' in dict and dict['trainer'] == trainer):
                print(f"{dict['id']}: {dict['nombre']} {dict['apellidos']}")
        os.system("pause")
    else:
        print(f"No se encuentra ningun Camper registrado en la clase del {trainer}.")
        os.system("pause")

def trainers(data):
    isActiveAulas = True
    while (isActiveAulas):
        profesores = [["Trainer 1", "NodeJS"],["Trainer 2","Java"],["Trainer 3","NetCore"],"Salir"]
        os.system("cls")
        print("Areas de Entrenamiento.")
        for i, item in enumerate(profesores):
            if (i != 3):
                print(f"{i+1}. {item[0]}")
            else:
                print(f"{i+1}. {item}")
        try:
            opMenuAulos = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (opMenuAulos == 1):
                trainer1 = False
                opciones(data, "Trainer 1", trainer1)
            elif (opMenuAulos == 2):
                trainer2 = False
                opciones(data, "Trainer 2", trainer2)
            elif (opMenuAulos == 3):
                trainer3 = False
                opciones(data, "Trainer 3", trainer3)
            elif (opMenuAulos == 4):
                isActiveAulas = False
            else:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")

# COMPLETO