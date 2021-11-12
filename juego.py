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