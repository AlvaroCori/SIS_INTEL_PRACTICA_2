'''
Cola de python (from collections import deque)
#https://docs.hektorprofe.net/python/colecciones-de-datos/colas/
copiar clase (importcopy)
https://pymotw.com/2/copy/
solver 8 puzzle
https://deniz.co/8-puzzle-solver/s
Conseguir el path actual: (import os)
https://www.delftstack.com/es/howto/python/python-get-path/
Abrir entrada desde un archivo txt: 
https://decodigo.com/python-leer-un-archivo-de-texto
'''

import os
from State import State
from BFS import BFS
from IDDFS import IDDFS, swap


#Read the input from a file txt
def loadTxt(path, file):
    numbers = []
    lineaNumeros = []
    elements = 0
    #open the file
    with open(f"{path}/{file}","r") as archivo:
        for linea in archivo:
            #erases the jumps ("\n"), split into space and convert in numbers
            lineaNumeros = list(map(lambda n : int(n) , linea.replace("\n","").split(" ")))
            numbers.append(lineaNumeros)
    elements = len(numbers)
    #return initial and final states
    return [numbers[i] for i in range(0,int(elements/2))], [numbers[i] for i in range(int(elements/2),elements)]

#initialState, finalState = loadTxt(os.path.abspath(os.getcwd()), "input.txt")

'''
#initialState= State([[1,2,3],[7,4,6],[0,5,8]]) 
#initialState= State([[1,2,6],[3,0,4],[7,5,8]]) 
#initialState= State([[1,2,6],[3,0,4],[7,5,8]]) 
#finalState = State([[1,2,3],[4,5,6],[7,8,0]])
'''
'''
initialState = State([[5,1,3,4],[2,10,6,7],[9,0,12,8],[13,14,11,15]]) 
finalState = State([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]) 
#650274318

#initialState = State([[2,3],[1,0]])
#finalState = State([[1,2],[3,0]])
result, state,counter = BFS(initialState, finalState,["l","u","r","d"])
print(("no" if result==False else " ") + "se hallo")
print("" if result==False else f"la cantidad de estados es: {counter}")



'''
def results(state):
    resultTables = []
    while (state != None):
        resultTables.append(state.table)
        state = state.father
    print(f"La altura del arbol alcanzo a los {len(resultTables)-1}")
    print("Los pasos son:")
    for table in reversed(resultTables):
        print(table)

actions = ["l","u","r","d"]
nameTxt = "input_n_3.txt"
option = -1
initialTable, goalTable = loadTxt(os.path.abspath(os.getcwd()), nameTxt)
initialState = State(initialTable)
goalState = State(goalTable)
while (option != 0):
    print("ruta objetivo:")
    print(os.path.abspath(os.getcwd())+"\\"+nameTxt)
    print("1. Colocar nombre de archivo de texto.")
    print("2. Cargar objetivo y inicial.")
    print("3. Resolver (BFS).")
    print("4. Resolver (IDDFS).")
    print("0. Salir.")
    option = int(input())
    if (option == 1):
        nameTxt = input()
    elif (option == 2):
        initialTable, goalTable = loadTxt(os.path.abspath(os.getcwd()), nameTxt)
        initialState = State(initialTable)
        goalState = State(goalTable)
    elif (option == 3):
        result, state,counter = BFS(initialState, goalState, actions)
        print(("no" if result==False else " ") + "se hallo")
        print("" if result==False else f"la cantidad de estados es: {counter}")
        results(state)
    elif (option == 4):
        result, state = IDDFS(initialState, goalState, actions)
        results(state)
        

