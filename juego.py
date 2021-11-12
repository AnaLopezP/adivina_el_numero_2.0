import random

def menu():
    nivel_ok = False 
    while nivel_ok == False:
        print("elija un nivel de dificultad entre 1 y 4, siendo el 1 el nivel fácil")
        nivel = int(input())
        if nivel < 1 and nivel > 4:
            print("El nivel tiene que estar entre 1 y 4, no hay más.")
        else:
            nivel_ok = True

    return nivel


def jugar(numero, reintentos):
    print("Intente con un número entero.")
    candidato = int(input())
    while candidato != numero and reintentos != 0:
        if candidato > numero:
            print("Te has pasado.")
        else:
            print("Te has quedado corto.")
        candidato = int(input())

    if candidato == numero:
        return True
    else:
        return False


def generar_numero(nivel):
    numero = 0
    if nivel == 1:
      numero = random.randint(0,100)
    elif nivel == 2:
        numero = random.randint(0,1000)
    elif nivel == 3:
        numero = random.randint(0,10000)
    elif nivel == 4:
        numero = random.randint(0,100000)
    return numero

def calcular_reintentos(nivel):
    reintentos = 0
    if nivel == 1:
      reintentos = 10
    elif nivel == 2:
        reintentos = 50
    elif nivel == 3:
        reintentos = 100
    elif nivel == 4:
        reintentos = 150
    return reintentos

nivel = menu()
reintentos = calcular_reintentos(nivel)
print("Has elegido el nivel " + str(nivel) + ". Tienes " + str(reintentos) + "intentos.")
incognita = generar_numero(nivel)
exito = jugar(incognita, reintentos)
if exito == True:
    print("Has ganado.")
else:
    print("Game Over.")