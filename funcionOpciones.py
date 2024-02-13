import os

def opciones(data, id, title):
    correct = False
    while (not correct):
        os.system("cls")
        if (title == "trabajo"):
            print(f"{title.capitalize()}.")
        else:
            print(f"{title.capitalize()}.")
        try:
            ob1 = int(input(f"Ingrese la nota del {title} 1 del estudiante {data[id]['nombre']}: "))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            if (not 1 <= ob1 <= 100):
                print("El valor ingresado no es valido, intentelo de nuevo.")
                os.system("pause")
            else:
                while (not correct):
                    os.system("cls")
                    print(title)
                    print(f"Ingrese la nota del {title} 1 del estudiante {data[id]['nombre']}: {ob1}")
                    try:
                        ob2 = int(input(f"Ingrese la nota del {title} 2 del estudiante {data[id]['nombre']}: "))
                    except ValueError:
                        print("El valor ingresado no es valido, intentelo de nuevo.")
                        os.system("pause")
                    else:
                        if (not 0 <= ob2 <= 100):
                            print("El valor ingresado no es valido, intentelo de nuevo.")
                            os.system("pause")
                        else:
                            while (not correct):
                                os.system("cls")
                                print(title)
                                print(f"Ingrese la nota del {title} 1 del estudiante {data[id]['nombre']}: {ob1}")
                                print(f"Ingrese la nota del {title} 2 del estudiante {data[id]['nombre']}: {ob2}")
                                try:
                                    ob3 = int(input(f"Ingrese la nota del {title} 3 del estudiante {data[id]['nombre']}: "))
                                except ValueError:
                                    print("El valor ingresado no es valido, intentelo de nuevo.")
                                    os.system("pause")
                                else:

                                    if (not 0 <= ob3 <= 100):
                                        print("El valor ingresado no es valido, intentelo de nuevo.")
                                        os.system("pause")
                                    else:
                                        correct = True
    prom = ((ob1 + ob2 + ob3) / 3)
    result = {
        f"{title}1": ob1,
        f"{title}2": ob2,
        f"{title}3": ob3,
        }
    return (prom, result)

# COMPLETO