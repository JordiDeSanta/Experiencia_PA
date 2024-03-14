import random
def juego_del_dado():
    c=True
    d=False
    pert=0
    comt=0
    while c:
        input("Presiona enter para tirar un dado:")
        per=random.randint(1,6)
        pert+=per
        print(f"Lanzaste un {per}, tu puntaje es de {pert}")
        if pert>=30:
            c=False
        if c:
            com=random.randint(1,6)
            comt+=com
            print(f"La computadora lanzó un {com}, su puntaje es de {comt}")
            if comt >=30:
                c=False
                d=True
    if d:
        print("Gana la computadora")
    else:
        print("Ganas tú")
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    pass