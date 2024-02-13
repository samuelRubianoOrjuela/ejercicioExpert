import os
import registroEstudiantes as rg
import guardarJson as gj
import matricula as mt
import notaModulo as nf
import areasEntrenamiento as ae
import trainers as tr
import stRiesgo as sr
import moduloReportes as mr

head = """
=============
|CAMPUSLANDS|
============="""
menu = ["Registro campers","Registro Prueba","Matriculacion","Notas Modulo","Areas de entrenamiento","Trainers","Estudiantes en riesgo","Modulo de reportes","Salir"]

isActive = True
while (isActive):
    os.system("cls")
    print(head)
    for i, indice in enumerate(menu):
        print(f"{i+1}. {indice}")
    try:
        opMenu = int(input("->"))
    except ValueError:
        print("El valor ingresado no es valido, intentelo de nuevo.")
        os.system("pause")
    else:
        if (opMenu == 1):    
            rg.registroAlumnos()
        elif (opMenu == 2):
            rg.registroPrueba(gj.archivoJson())
        elif (opMenu == 3):
            mt.matriculacion(gj.archivoJson())
        elif (opMenu == 4):
            nf.modulo(gj.archivoJson())
        elif (opMenu == 5):
            ae.aulas(gj.archivoJson())
        elif (opMenu == 6):
            tr.trainers(gj.archivoJson())
        elif (opMenu == 7):
            sr.campersRiesgo(gj.archivoJson())
        elif (opMenu == 8):
            mr.reportes(gj.archivoJson())
        elif (opMenu == 9):
            isActive = False
        else:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause") 

# COMPLETO