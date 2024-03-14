import random
def adivinar_numero():
    n=random.randint(1,10)
    a=int(input("Trata de Adivinar el número:"))
    if a==n:
        print("Felicidades, adivinaste el número!!")
    else:
        print("No adivinaste el número :c")
    return