'''
function BFS( initialstate, goalstate, actions){
    open = queue(initialstate);   
    while (open.qSize() != 0){
        state =open.dequeue()
        if (goaltest(state,goalstate)){
            return success; state
        }
        //Expandir un estado
        for each (a in actions){
            successor = TF(state, a);
            successor.father = state
            //ver si el succesor es el estado objetivo
            if (goaltest(state,goalstate)){
                return success, successor
            }
            open.enqueue(successor)
        }
    } 
}

'''
#Cola de python
#https://docs.hektorprofe.net/python/colecciones-de-datos/colas/
#copiar clase
#https://pymotw.com/2/copy/
#solver 8 puzzle
#https://deniz.co/8-puzzle-solver/s
import copy
import time
class State:
    def __init__(self, table, father=None):
        self.father = father
        self.table = table

from collections import deque
from os import stat

def goalTest(state, goalState):
    rows = len(goalState.table)
    columns = len(goalState.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] != goalState.table[row][col]):
                return False
    return True
def findSpace(state):
    rows = len(state.table)
    columns = len(state.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] == 0):
                return row, col
    return -1, -1

def swap(state, r1, c1, r2,c2):
    aux = state.table[r1][c1]
    state.table[r1][c1] = state.table[r2][c2]
    state.table[r2][c2] = aux
'''
E -> Esquina
B -> Borde
A -> Adentro
E B B B B E
B A A A A B
B A A A A B
B A A A A B
B A A A A B
E B B B B E
'''
def evaluateAction(state, action):
    row, col = findSpace(state)
    rows = len(state.table) -1 
    columns = len(state.table[0]) -1
    if (row == 0 and col==0):               #si se halla en esquinas
        return action=="r" or action =="d"
    elif (row == 0 and col==columns):
        return action=="l" or action =="d"  
    elif (row == rows and col==0):
        return action=="u" or action =="r" 
    elif (row == rows and col==columns):
        return action=="l" or action =="u"  #fin
    elif (col == 0): #si se halla en bordes
        return action=="u" or action =="r" or action =="d" 
    elif (row == 0):
        return action=="l" or action =="r" or action =="d"
    elif (col == columns):
        return action=="l" or action =="u" or action =="d"
    elif (row == rows):
        return action=="l" or action =="u" or action =="r" #fin
    return True #si se halla adentro de los bordes y esquinas

def TF(state, action):
    newState = copy.deepcopy(state)
    row, col = findSpace(state)
    if (action == "l"):
        swap(newState,row,col,row,col-1)
    elif (action == "u"):
        swap(newState,row,col,row-1,col)
    elif (action == "r"):
        swap(newState,row,col,row,col+1)
    elif (action == "d"):
        swap(newState,row,col,row+1,col)
    return newState
def evaluateRepeatState(state):
    actual = state
    walker = state.father
    while (walker != None):
        if (goalTest(actual,walker)):
            return False
        walker = walker.father
    return True

def BFS(initialState, goalState,actions):
    open = deque([initialState])
    while (len(open) != 0):
        state = open.popleft()
        if (goalTest(state, goalState)):
            return True, state
        for a in actions:
            
            if (evaluateAction(state, a) and evaluateRepeatState(state)):
                #print(state.table)
                #time.sleep(1)
                successor = TF(state, a)
                successor.father = state
                if (goalTest(state, goalState)):
                    return True, state
                open.append(successor)
    return False, None

#initialState= State([[1,2,3],[7,4,6],[0,5,8]]) 
#initialState= State([[1,2,6],[3,0,4],[7,5,8]]) 
#initialState= State([[1,2,6],[3,0,4],[7,5,8]]) 
#finalState = State([[1,2,3],[4,5,6],[7,8,0]])
initialState = State([[5,1,3,4],[2,10,6,7],[9,0,12,8],[13,14,11,15]]) 
finalState = State([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]) 
#650274318
#initialState= State([[2,3],[1,0]])
#finalState = State([[1,2],[3,0]])
result, state = BFS(initialState, finalState,["l","u","r","d"])
print(("no" if result==False else " ") + "se hallo")
print(".....")
while (state != None):
    print(state.table)
    state = state.father
#print(state.father.father.table)