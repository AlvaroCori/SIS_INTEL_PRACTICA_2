import os
from State import State
from BFS import BFS
from IDDFS import IDDFS
from DLS_All_States import DLSSearchState
import time


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

def results(state):
    resultTables = []
    while (state != None):
        resultTables.append(state.table)
        state = state.father
    print(f"La altura del arbol alcanzo a los {len(resultTables)-1}")
    print("Los pasos son:")
    for table in reversed(resultTables):
        for line in table:
            print(line)
        print("----------------")

actions = ["l","u","r","d"]
nameTxt = "input_n_4.txt"
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
    print("5. Buscar todos los estados (DLS).")
    print("0. Salir.")
    option = int(input())
    if (option == 1):
        nameTxt = input()
    elif (option == 2):
        initialTable, goalTable = loadTxt(os.path.abspath(os.getcwd()), nameTxt)
        initialState = State(initialTable)
        goalState = State(goalTable)

    elif (option == 3):
        init = time.time()
        result, state,counter = BFS(initialState, goalState, actions)
        end = time.time()
        print(("no" if result==False else "") + "se hallo el estado objetivo.")
        if (result):  
            results(state)
            print("" if result==False else f"la cantidad de estados es: {counter}")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")

    elif (option == 4):
        init = time.time()
        result, state, counters = IDDFS(initialState, goalState, actions)
        end = time.time()
        if (result == "success"):
            print("Se hallo el estado objetivo.")
            results(state)
            print(f"La cantidad de estados por niveles son {counters}")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        if (result == "cutoff"):
            print("No se hallo el estado objetivo, se necesita mas profundidad.")
        if (result == "failure"):  
            print("No se hallo el estado objetivo, no hay coincidencias en todos los estados expandidos.")
    elif (option == 5):
            counter = DLSSearchState(initialState,actions)
            print("la cantidad de estados diferentes para el estado inicial:")
            results(initialState)
            print(f"es {counter} estados.")

