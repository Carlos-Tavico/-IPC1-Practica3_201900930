# This program prints Hello, world!
from operator import truediv
import random

def juego():
    #variables
    global nomb, carn, fil, col, tablero, indiceJug, dlim, ilim, puntaje, tam
    nomb = input("Ingrese su nombre: ")
    carn = input("Ingrese su carnet: ")
    tam = True
    while tam == True:
        fil = int(input("DIMENSIONES DEL TABLERO\n FILAS: "))
        col = int(input("COLUMNAS: "))
        if fil >= 7 and col >= 0:
            tam = False
        else:
            print("El valor minimo de filas y columnas es de 7")
    tablero = ["[  ]" for x in range(fil*col)]
    
    #items
    global rango1, rango2, rango3
    rango1 = random.randint(8,fil*col//4)
    for o in range(rango1):
        tablero[random.randint(0, len(tablero)-1)] = "[ #]"
    rango2 = random.randint(6,fil*col//5)
    for o in range(rango2):
        tablero[random.randint(0, len(tablero)-1)] = "[ $]"
    rango3 = random.randint(8,fil*col*3//10)
    for o in range(rango3):
        tablero[random.randint(0, len(tablero)-1)] = "[ @]"
    #posicion inicial
    indiceJug = random.randint(0, len(tablero)-1)
    tablero[indiceJug] = "[v:]"

bulean1 = True
bulean2 = True
puntaje = 10
#informacion
while bulean1 == True:
    print("Elija una opcion:\n1. JUGAR\n2. HISTORIAL\n3. SALIR\n")
    op = int(input("Elija una opcion valida: "))
    if op > 3 or op < 1:
        print("Ingrese un numero valido, por favor")
    if op == 3:
        bulean1 = False
    if op == 2:
        print("Historial")
    if op == 1:
        bulean2 = True

        #juego
        juego()
        while bulean2 == True:
            print("-------------------------------------------------------------------\n"+nomb+" - "+carn+" - IPC1 A\n-------------------------------------------------------------------")
            print("Puntaje: ")
            print(puntaje)
            for fila in range(col):
                for columna in range(fil):
                    print(tablero[fila*fil+columna], end = " ")
                print()
            dlim = (indiceJug + 1 ) % col
            ilim = (indiceJug + col) % col
            movimiento = input("Moverse(W,A,S,D)")
            if movimiento == "w":
                tablero[indiceJug] = "[  ]"
                indiceJug = indiceJug - 1*fil   
                if indiceJug < 0:
                    indiceJug = indiceJug + fil*col
            if movimiento == "s":
                tablero[indiceJug] = "[  ]"
                indiceJug = indiceJug + 1*fil
                if indiceJug > fil*col:
                    indiceJug = indiceJug - fil*col
            if movimiento == "d":
                if dlim == 0:
                    tablero[indiceJug] = "[  ]"
                    indiceJug = indiceJug - col + 1
                else:
                    tablero[indiceJug] = "[  ]"
                    indiceJug = indiceJug + 1
            if movimiento == "a":
                if ilim == 0:
                    tablero[indiceJug] = "[  ]"
                    indiceJug = indiceJug + col - 1
                else:
                    tablero[indiceJug] = "[  ]"
                    indiceJug = indiceJug - 1
            if movimiento == "m":
                bulean2 = False
            
            if tablero[indiceJug] == "[ #]":
                puntaje = puntaje -10
            if tablero[indiceJug] == "[ $]":
                puntaje = puntaje +15
            if tablero[indiceJug] == "[ @]":
                puntaje = puntaje +10
            tablero[indiceJug] = "[v:]"
            if puntaje >= 100:
                print("\n"+"¡Has ganado! :D"+"\n")
                bulean2 = False
                puntaje = 10
            if puntaje <= 0:
                print("\n"+"Has perdido D:"+"\n")
                bulean2 = False
                puntaje = 10