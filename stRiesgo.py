import os

def campersRiesgo(data):
    os.system("cls")
    print("Estudiantes en Riesgo ⚠️")
    for dict in data.values():
        if ("riesgo" in dict):
            print(f"'{dict['id']}' {dict['nombre']} {dict['apellidos']}\nNota del Modulo: {dict['notaModulo']}")
    os.system("pause")

# COMPLETO