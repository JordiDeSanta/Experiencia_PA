import random

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """

    secuencia = ""
    for i in range(9):
        numero =  random.randint(0, 10)
        secuencia += f"{numero}"

    print(secuencia)
    usuario = input("Escribe el patrón: ")

    if usuario == secuencia:
        print("PERFECTO")
    else:
        print("F")


    pass