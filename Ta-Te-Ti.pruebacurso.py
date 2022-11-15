# -*- coding: utf-8 -*-
#Autor: Bryan Barbie


import random
ganador = None
#defino tablero
tablero =[
    "_","_","_",
    "_","_","_",
    "_","_","_",
    ]

#funcion para mostrar en pantalla el tablero
def ver_tablero():
    print("""\nTABLERO        POSICIONES\n""")
    print("\n")
    print(" | "  + tablero[0] + " | " + tablero[1] + " | " + tablero[2] + " | "+"      1 | 2 |3")
    print(" | "  + tablero[3] + " | " + tablero[4] + " | " + tablero[5] + " | "+"      4 | 5 |6")
    print(" | "  + tablero[6] + " | " + tablero[7] + " | " + tablero[8] + " | "+"      7 | 8 |9")
    print("\n")

#funcion para presentar el juego en pantalla
def jugar_inicio():
    print("Bienvenido al juego de Ta-Te-Ti")
    nombre=input("Como es tu nombre?: ")
    print(f"\nHola {nombre}, estas son las Instrucciones.\n")
    print("""Intrucciones:
    -Es un juego 1vs1, en este caso jugaras vs IO(maquina)
    -Es un juego por turnos, se juega en tablero de 3x3
    -Se permiten el uso de 2 simbolos('X', 'O'), uno para cada jugador, la  'X'  comienza el juego
    -El jugador que logre combinar su simboloc 3 veces en vertical, horizontal o diagonal es el ganador
    -Si el tablero esta lleno y ninguno de los jugadores combinÃƒÂ³ su simbolo 3 veces, se declararÃƒÂ¡ empate y volverÃƒÂ¡ a comenzar el juego""")

    ver_tablero()

#funcion para identificar ganador del juego
def hay_ganador():
    global ganador
    chequeo_horizontal()
    chequeo_vertical()
    chequeo_diagonal()

#acople de funcion hay_ganador()
def chequeo_horizontal():
    global ganador
    if tablero[0] == tablero[1] == tablero[2] !="_":
        ganador = tablero[0]
    elif tablero[3] == tablero[4] == tablero[5] !="_":
        ganador = tablero[3]
    elif tablero[6] == tablero[7] == tablero[8] !="_":
        ganador = tablero[6]

#acople de funcion hay_ganador()
def chequeo_vertical():
    global ganador
    if tablero[0] == tablero[3] == tablero[6] !="_":
        ganador = tablero[0]
    elif tablero[1] == tablero[4] == tablero[7] !="_":
        ganador = tablero[1]
    elif tablero[2] == tablero[5] == tablero[8] !="_":
        ganador = tablero[2]

#acople de funcion hay_ganador()
def chequeo_diagonal():
    global ganador
    if tablero[0] == tablero[4] == tablero[8] !="_":
        ganador = tablero[0]
    elif tablero[2] == tablero[4] == tablero[6] !="_":
        ganador = tablero[2]

#funcion de peticion de jugada
def jugada_propia(ficha):
    chequeo = False
    while chequeo == False:
        posicion =int(input("Elegi una posicion del 1 al 9 para colocar tu ficha: "))
        posicion = posicion-1
        
        if tablero[posicion] == "_":
            chequeo = True
            tablero[posicion] = ficha
            ver_tablero()
        else:
            print("La posicion seleccionada ya esta ocupada, vuelve a intentar.")

#funcion de jugada aleatoria para la maquina
def jugada_aleatoria(ficha):
    chequeo= False
    while chequeo == False:
        posicion=random.randint(0,8)
        if tablero[posicion] == "_":
            chequeo = True
            tablero[posicion] = ficha
            ver_tablero()
        else:
            chequeo=False

#funcion para definir juego en caso de que jugador escoga X
def jugarX():
    global ganador
    print("\nComienza el juego")
    ver_tablero()

    for x in range(5):
        ficha= "X"
        jugada_propia(ficha)
        hay_ganador()
        if ganador != "X" and x<4:
            for y in range(3):
                ficha= "O"
                print("posicion donde coloca O la maquina: ")
                jugada_aleatoria(ficha)
                hay_ganador()
                if ganador == "O":
                    print("Ha ganado la maquina (jugador 2)")
                break
        elif ganador == "X":
            print("Felicitaciones. Has ganado el juego (jugador 1)")
            break
        else:
            print("Empataron el juego")

#funcion para definir juego en caso de que jugador escoga O
def jugarO():
    global ganador
    print("\nComienza el juego")
    ver_tablero()

    for x in range(5):
        print("Turno de la maquina.\n")
        ficha= "X"

        jugada_aleatoria(ficha)
        hay_ganador()
        if ganador != "X" and x<4:
            for y in range(3):
                print("Tu turno, elige la posicion de tu ficha")
                ficha= "O"
                jugada_propia(ficha)
                hay_ganador()
                if ganador == "O":
                    print("Felicitaciones, has ganado el juego!")
                break
        elif ganador == "X":
            print("Ha ganado el juego la maquina.")
            break
        else:
            print("Empataron el juego")
                         

#ESTRUCTURA PRINCIPAL DEL JUEGO


print(jugar_inicio())

ficha= False
while ficha == False:
    print("""\ncon que ficha te gustaria jugar?: \n
Presiona 1 para elegir "X"
Presiona 2 para elegir "O" \n""")
    ficha=int(input("X/O: "))
    if ficha ==1:
        ficha= True
        jugarX()
    
    elif ficha ==2:
        ficha=True
        jugarO()

    elif ganador==None:
        ficha=False

    else:
        print("el valor ingresado no es valido.")
        ficha =False