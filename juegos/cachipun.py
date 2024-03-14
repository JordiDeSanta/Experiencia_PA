import random
def cachipun():
    n=random.randint(1,3)
    a=input("Elige Piedra, Papel o Tijeras?:")
    if n==1:
        e="Piedra"
    elif n==2:
        e="Tijeras"
    else:
        e="Papel"
    print(f"La computadora eligío {e}")
    if e==a:
        print("Empate")
    elif n==1 and a=="Tijeras":
        print("Perdiste")
    elif n==1 and a=="Papel":
        print("Ganaste")
    elif n==2 and a=="Piedra":
        print("Perdiste")
    elif n==2 and a=="Papel":
        print("Ganaste")
    elif n==3 and a=="Tijeras":
        print("Perdiste")
    elif n==3 and a=="Piedra":
        print("Ganaste")