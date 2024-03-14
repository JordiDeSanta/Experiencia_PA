import random

def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """


    numero_aleatorio = random.randint(0, 100)

    usuario = input("¿El número es par o impar? (P / I): ")

    print(f"El número es: {numero_aleatorio}")

    if numero_aleatorio % 2 == 0:
        if usuario == "P":
            print("Correcto, es par")
        else:
            print("Incorrecto, era par")

    elif numero_aleatorio % 2 != 0:
        if usuario == "I":
            print("Correcto, es impar")
        else:
            print("Incorrecto, era impar")
    pass