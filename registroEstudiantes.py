import os
import guardarJson as gj

def registroAlumnos():
    campers = {}
    isActiveCamper = True
    while(isActiveCamper):
        opReg = ["Registrar camper","Salir al menu principal"]
        os.system("cls")
        print("Registre al camper.")
        for i, item in enumerate(opReg):
            print(f"{i+1}. {item}")
        try:
            opMenuReg = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (opMenuReg == 1):
                alumno = {
                    'id': '', 
                    'nombre': '', 
                    'apellidos': '', 
                    'direccion': '', 
                    'acudiente': '',
                    'estado': 'inscrito',
                    'telefonos': {
                        'fijo': '',
                        'celular': ''
                    }
                }
                for info in alumno:
                    correctInput = False 
                    while (not correctInput):
                        os.system("cls")
                        print("Registre al camper.")
                        if (info == 'estado'):
                            correctInput = True
                        elif (info != 'telefonos'):
                                alumno[info] = input(f"Ingrese {info.capitalize()} del camper: ")
                                if (alumno[info] == ''):
                                    print("Debe ingresar la informacion para continuar.")
                                    os.system("pause")
                                elif os.path.exists(gj.ruta):
                                    data = gj.archivoJson()
                                    if (alumno['id'] in data):
                                        print(f"Este Id ya fue registrado en el alumno '{data[alumno['id']]['nombre']}'")
                                        os.system("pause")
                                    elif (alumno['id'] in campers):
                                        print(f"Este Id ya fue registrado en el alumno '{campers[alumno['id']]['nombre']}'")
                                        os.system("pause")
                                    else:     
                                        correctInput = True
                                else:
                                    correctInput = True
                        else:
                            correct = False
                            while (not correct):
                                os.system("cls")
                                print("Registre al camper.")
                                if (alumno['telefonos']['fijo'] == ''):
                                    try:
                                        alumno['telefonos']['fijo'] = int(input("Ingrese en Nro de Telefono Fijo del camper: "))
                                        alumno['telefonos']['celular'] = int(input("Ingrese en Nro de Celular del camper: "))    
                                    except ValueError:
                                        print("El valor ingresado no es valido, intentelo de nuevo.")
                                        os.system("pause")
                                    else:
                                        correct = True
                                        correctInput = True
                                else:
                                    try:
                                        print(f"Ingrese en Nro de Telefono Fijo del camper: {alumno['telefonos']['fijo']}")
                                        alumno['telefonos']['celular'] = int(input("Ingrese en Nro de Celular del camper: "))    
                                    except ValueError:
                                        print("El valor ingresado no es valido, intentelo de nuevo.")
                                        os.system("pause")
                                    else:
                                        correct = True
                                        correctInput = True
                campers.update({alumno['id']:alumno})
            elif (opMenuReg == 2):
                isActiveCamper = False
    if os.path.exists(gj.ruta):
        data = gj.archivoJson()
        data.update(campers)
        gj.actualizarData(data)
    else:
        gj.guardarArchivo(campers)
    return campers

def registroPrueba(data): 
    if (data):
        for dict in data.values():
            if (dict['estado'] == 'inscrito'):
                aprobados = False
            else:
                aprobados = True
        if (not aprobados):
            isActivePrueba = True
            while (isActivePrueba):
                opReg = ["Registrar prueba","Salir al menu principal"]
                os.system("cls")
                print("Prueba de Admision.")
                for i, item in enumerate(opReg):
                    print(f"{i+1}. {item}")
                try:
                    opMenuPrueba = int(input("->"))
                except ValueError:
                    print("El valor ingresado no es valido, intentelo de nuevo.")
                    os.system("pause")
                else:
                    if (opMenuPrueba == 1):
                        correct = False
                        while (not correct):
                            os.system("cls")
                            print("Prueba de Admision.")
                            id = input("Ingrese el id del camper: ")
                            if (id not in data):
                                print(f"No hay ningun camper registrado con el id: {id}")
                                os.system("pause")
                            elif (data[id]['estado'] != "inscrito"):
                                print(f"Al parecer la prueba del camper registrado con el id '{id}' ya fue registrada, intentelo con otro estudiante.")
                                os.system("pause")
                            else:
                                correct = True
                        correct = False
                        while (not correct):
                            os.system("cls")
                            print("Prueba de Admision.")
                            print(f"Ingrese el id del camper: {id}")
                            try:
                                notaTeorica = int(input(f"Ingrese la nota de la prueba Teorica del estudiante {data[id]['nombre']}: "))
                            except ValueError:
                                print("El valor ingresado no es valido, intentelo de nuevo.")
                                os.system("pause")
                            else:
                                if (not 1<= notaTeorica <= 100):
                                    print("El valor ingresado no es valido, intentelo de nuevo.")
                                    os.system("pause")
                                else:
                                    correct2 = False
                                    while (not correct2):
                                        os.system("cls")
                                        print("Prueba de Admision.")
                                        print(f"Ingrese el id del camper: {id}")
                                        print(f"Ingrese la nota de la prueba Teorica del estudiante {data[id]['nombre']}: {notaTeorica}")
                                        try:
                                            notaPractica = int(input(f"Ingrese la nota de la prueba Practica del estudiante {data[id]['nombre']}: "))
                                        except ValueError:
                                            print("El valor ingresado no es valido, intentelo de nuevo.")
                                            os.system("pause")
                                        else:
                                            if (not 1<= notaPractica <= 100):
                                                print("El valor ingresado no es valido, intentelo de nuevo.")
                                                os.system("pause")
                                            else:
                                                correct2 = True
                                                correct = True 
                        prom = ((notaTeorica + notaPractica) / 2) 
                        if (prom >= 60):
                            estado = "aprobado"
                        else:
                            estado = "no aprobado"
                        newInfo = {
                            'estado': estado,
                            'notaTeorica': notaTeorica,
                            'notaPractica': notaPractica,
                        }
                        data[id].update(newInfo)
                        gj.actualizarData(data)
                    elif (opMenuPrueba == 2):
                        isActivePrueba = False
                    else:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
        else:
            print("Ya fueron registradas las pruebas de todos los campers.")
            os.system("pause")

# COMPLETO