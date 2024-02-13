import os
import guardarJson as gj

def trainers(opTrainer, data, id, aulas):
    if (33 > aulas["apolo"] or 33 > aulas["artemis"] or 33 > aulas["sputnik"]):
        if (opTrainer == 1):
            if (33 > aulas["apolo"]):
                aulas["apolo"] +=1
                trainer = {
                    'trainer': 'Trainer 1',
                    'ruta': 'NodeJS',
                    'aula': 'Apolo',
                    'fecha entrada': 'Enero 5',
                    'fecha salida': 'Octubre 10'
                }
                data[id].update(trainer)
                gj.actualizarData(data)
            else:
                print("La sala Apolo está llena.")
                os.system("pause")
        elif (opTrainer == 2):
            if (33 > aulas["artemis"]):
                aulas["artemis"] +=1
                trainer = {
                    'trainer': 'Trainer 2',
                    'ruta': 'Java',
                    'aula': 'Artemis',
                    'fecha entrada': 'Marzo 28',
                    'fecha salida': 'Enero 30'
                }
                data[id].update(trainer)
                gj.actualizarData(data)
            else:
                print("La sala Artemis está llena.")
                os.system("pause")
        elif (opTrainer == 3):
            if (33 > aulas["sputnik"]):
                aulas["sputnik"] +=1
                trainer = {
                    'trainer': 'Trainer 3',
                    'ruta': 'NetCore',
                    'aula': 'Sputnik',
                    'fecha entrada': 'Agosto 15',
                    'fecha salida': 'Junio 21'
                }
                data[id].update(trainer)
                gj.actualizarData(data)
            else:
                print("La sala Sputnik está llena.")
                os.system("pause")

def matriculacion(data):
    if (data): 
        aulas = {
            'apolo': 0,
            'artemis': 0,
            'sputnik': 0
        }
        for dict in data.values():
            if ("aula" not in dict):
                pass
            elif (dict['aula'] == "Apolo"):
                aulas['apolo'] += 1
            elif (dict['aula'] == "Artemis"):
                aulas['artemis'] += 1
            elif (dict['aula'] == "Sputnik"):
                aulas['sputnik'] += 1
        isActiveMt = True
        while(isActiveMt):
            opIng = ["Matricular a un estudiante","Salir al menu principal"]
            os.system("cls")
            print("Matriculacion.")
            for i, items in enumerate(opIng):
                print(f"{i+1}. {items}")
            try:
                opMatricula = int(input("->"))
            except ValueError:
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")
            else:   
                if (opMatricula == 1):
                    id = input("Ingrese el id del camper: ")
                    if (id not in data):
                            print(f"No hay ningun camper registrado con el id: {id}")
                            os.system("pause")
                    elif ("aula" in data[id]):
                        print("Al parecer a este camper ya se le ha registrado la ruta, intentelo con otro estudiante.")
                        os.system("pause")
                    elif (data[id]['estado'] == "no aprobado"):
                        print(f"Al parecer el camper registrado con el id '{id}' no fue aprobado, intentelo con otro estudiante.")
                        os.system("pause")
                    elif (data[id]['estado'] == "inscrito"):
                        print(f"Al parecer al camper con el id '{id}' no se le ha registrado su prueba de admision, registre su prueba de admision primero")
                        os.system("pause")
                    else:
                        opciones = { 
                            "Trainer 1": "NodeJS",
                            "Trainer 2": "Java",
                            "Trainer 3": "NetCore"
                        }
                        os.system("cls")
                        print("Rutas.")
                        for i, items, in enumerate(opciones.items()):
                            print(f"{i+1}. {items[0]}: {items[1]}")
                        print("Elija la ruta que llevara el estudiante ")
                        try:
                            opTrainer = int(input("->"))
                        except ValueError:
                            print("El valor ingresado no es valido, intentelo de nuevo.")
                            os.system("pause")
                        else:
                            if (not 1 <= opTrainer <= 3):
                                print("El valor ingresado no es valido, intentelo de nuevo.")
                                os.system("pause")
                            else:
                                trainers(opTrainer, data, id, aulas)
                elif (opMatricula == 2):
                    isActiveMt = False
                else:
                    print("El valor ingresado no es valido, intentelo de nuevo.")
                    os.system("pause")

# COMPLETO