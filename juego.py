import random


def menu():
    nivel_ok = False 
    while nivel_ok == False:
        print("elija un nivel de dificultad entre 1 y 4, siendo el 1 el nivel facil")
        nivel = int(input())
        if nivel < 1 and nivel > 4:
            print("El nivel tiene que estar entre 1 y 4, no hay mas.")
        else:
            nivel_ok = True

    return nivel

def jugar(numero, reintentos):
    print("Introduzca un numero entero.")
    candidato = int(input())
    while candidato != numero and reintentos > 1 :
        if candidato > numero:
            print("Te has pasado.")
        else:
            print("Te has quedado corto.")
        candidato = int(input())
        reintentos = reintentos - 1
    return reintentos

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

print("Inserte su nombre")
nombre_juagdor = str(input())
puntuacion = 0
tabla_resultados = []
tabla_resultados.append(nombre_juagdor)
nivel = menu()
reintentos = calcular_reintentos(nivel)
puntuacion = reintentos
print("Has elegido el nivel " + str(nivel) + ". Tienes " + str(reintentos) + " intentos y tu puntuación máxima es " + str(puntuacion) + ". Cada reintento se resta de la puntuación.")
incognita = generar_numero(nivel)
resultado = jugar(incognita, reintentos)
if resultado > 1:
    print("Has ganado.")
    
else:
    print("Game Over.")
puntuacion = resultado - 1
tabla_resultados.append(puntuacion)
print(tabla_resultados)