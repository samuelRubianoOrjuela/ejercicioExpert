import os
import guardarJson as gj
import funcionOpciones as fo

def op1(data, id):
    isActiveFiltro = True
    while (isActiveFiltro):
        os.system("cls")
        print("Notas del Filtro.")
        try:
            notaTeorica = int(input(f"Ingrese la nota de la prueba Teorica del estudiante {data[id]['nombre']}: "))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (not 0 <= notaTeorica <= 100):
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")
            else:
                correct = False
                while (not correct):
                    os.system("cls")
                    print("Notas del Filtro.")
                    print(f"Ingrese la nota de la prueba Teorica del estudiante {data[id]['nombre']}: {notaTeorica}")
                    try:
                        notaPractica = int(input(f"Ingrese la nota de la prueba Practica del estudiante {data[id]['nombre']}: "))
                    except ValueError:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
                    else:
                        if (not 0 <= notaPractica <= 100):
                            print("El valor ingresado no es valido, intentelo de nuevo.")
                            os.system("pause")
                        else:
                            correct = True
                            isActiveFiltro = False
    nT = (notaTeorica * 0.3)
    nP = (notaPractica * 0.6)
    nTotal = (nT + nP)
    return nTotal

def op2(data, id):
    menuOtros = ["Trabajos","Quices","Salir a Modulo"]   
    regNotas = 0 
    conf1 = True
    conf2 = True
    isActiveOtros = True
    while (conf1 or conf2 or isActiveOtros):
            os.system("cls")
            print("Otras Notas.")
            print("Elija una opcion.")
            for i, indice in enumerate(menuOtros):
                print(f"{i+1}. {indice}")
            try:
                opMenuOtros = int(input("->"))
            except ValueError:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")
            else:
                if (conf1 or conf2):
                    if (opMenuOtros == 1):
                        if (conf1):
                            trabajos = (fo.opciones(data, id, "trabajo"))
                            regNotas += 1
                            conf1 = False
                        else:
                            print("Los Trabajos ya fueron registrados.")
                            os.system("pause")
                    elif (opMenuOtros == 2):
                        if (conf2):
                            quices = (fo.opciones(data, id, "quiz"))
                            regNotas += 1
                            conf2 = False
                        else:
                            print("Los Quices ya fueron registrados.")
                            os.system("pause")
                    else:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
                elif (opMenuOtros == 3):
                        if (regNotas == 2):
                            isActiveOtros = False
                        else:
                            print("Debe registrar los Trabajos y los Quices del estudiante para poder salir.")
                            os.system("pause")
                else:
                    print("Ya fueron ingresadas las notas de Quices y Trabajos.")
                    os.system("pause")
    nOtros = (((trabajos[0] + quices[0]) / 2) * 0.1)
    return (nOtros)

def modulo(data):
    if (data):  
        menuModulo = ["Notas del Filtro","Otras Notas","Salir al menu principal"]
        isActiveModulo = True 
        while isActiveModulo:
            opReg = ["Registrar notas del modulo","Salir al menu principal"]
            os.system("cls")
            print("Notas del modulo.")
            for i, item in enumerate(opReg):
                print(f"{i+1}. {item}")
            try:
                opMenuNotas = int(input("->"))
            except ValueError:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")
            else:
                if (opMenuNotas == 1):    
                    os.system("cls")
                    print("Nota del Modulo.")
                    id = input("Ingrese el id del camper: ")
                    if (id not in data):
                        print(f"No hay ningun camper registrado con el id: {id}")
                        os.system("pause")
                        break
                    elif (data[id]['estado'] == "inscrito"):
                        print("Aun no se ha registrado la pueba de admision de este camper, primero registrela.")
                        os.system("pause")
                        break
                    elif (data[id]['estado'] == "no aprobado"):
                        print(f"Al parecer el camper registrado con el id '{id}' no fue aprobado, intentelo con otro estudiante.")
                        os.system("pause")
                    else:
                        rgM = 0
                        conf1 = True
                        conf2 = True
                        isActiveMCamper = True
                        while (conf1 or conf2 or isActiveMCamper):
                            os.system("cls")
                            print("Nota del Modulo.")
                            print("Elija una opcion.")
                            for i, indice in enumerate(menuModulo):
                                print(f"{i+1}. {indice}")
                            try:
                                opMenuModulo = int(input("->"))
                            except ValueError:
                                print("El valor ingresado no es valido, intentelo de nuevo.")
                                os.system("pause")
                            else:
                                if (opMenuModulo == 1):
                                    if (conf1):
                                        filtro = (op1(data, id))
                                        rgM += 1
                                        conf1 = False
                                    else:
                                        print("Ya fueron registradas las notas del filtro .")
                                        os.system("pause")
                                elif (opMenuModulo == 2):
                                        if (conf2):
                                            otros = (op2(data, id))
                                            rgM += 1
                                            conf2 = False
                                        else:
                                            print("Ya fueron ingresadas las notas de Quices y Trabajos.")
                                            os.system("pause")
                                elif (opMenuModulo == 3):
                                    if (rgM == 2):
                                        isActiveMCamper = False
                                    else:
                                        print("Debe registrar todas las notas del modulo para poder salir.")
                                        os.system("pause")
                                else:
                                    print("El valor ingresado no es valido, intentelo de nuevo.")
                                    os.system("pause")
                        nFinal = (filtro + otros)
                        if (nFinal < 60):
                            nModulo = {
                                'riesgo': 'riesgo',
                                'notaModulo': round(nFinal, 1)
                            }
                        else:
                            nModulo = {
                                'notaModulo': round(nFinal, 1)
                            }
                        data[id].update(nModulo)
                        gj.actualizarData(data)
                elif (opMenuNotas == 2):
                    isActiveModulo = False
                else:
                    print("El valor ingresado no es valido, intentelo de nuevo.")
                    os.system("pause")

# COMPLETO        