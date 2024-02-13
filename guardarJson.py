import os
import json

ruta = "data/campers.json"

def guardarArchivo(campers):
    with open(ruta, "w") as archivo:
        json.dump(campers, archivo, indent=4)

def archivoJson():
    if os.path.exists(ruta):
        with open(ruta, "r") as archivo:
            data = json.load(archivo) 
        return data
    else:
        print("No se encuentra ningun estudiante registrado, intentelo de nuevo.")
        os.system("pause")

def actualizarData(newData):
    with open(ruta, "w") as archivo:
        json.dump(newData, archivo, indent=4)

# COMPLETO