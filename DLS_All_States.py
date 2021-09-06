import copy
from State import State
import math
#A class with table and a father

#Compare all elements of 2 tables
def goalTest(state, goalState):
    rows = len(goalState.table)
    columns = len(goalState.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] != goalState.table[row][col]):
                return False
    return True

#Search the element 0 and return the position
def findSpace(state):
    rows = len(state.table)
    columns = len(state.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] == 0):
                return row, col
    return -1, -1

#Swap two elements of a table
def swap(state, r1, c1, r2,c2):
    aux = state.table[r1][c1]
    state.table[r1][c1] = state.table[r2][c2]
    state.table[r2][c2] = aux

'''
C -> Corner
B -> Border
I -> Inside
C B B B B C
B I I I I B
B I I I I B
B I I I I B
B I I I I B
C B B B B C
When a space is empty in some positions the actions are restringid
for example:
_in corners only can move in 2 directions
_in borders only can move in 3 directions
_in inside can move in the 4 directions
'''
def evaluateAction(state, action):
    row, col = findSpace(state)
    rows = len(state.table) -1 
    columns = len(state.table[0]) -1
    #conditions for the 4 corners
    if (row == 0 and col==0):        
        return action=="r" or action =="d"
    elif (row == 0 and col==columns):
        return action=="l" or action =="d"  
    elif (row == rows and col==0):
        return action=="u" or action =="r" 
    elif (row == rows and col==columns):
        return action=="l" or action =="u"  
    #if the empty position don't be a corner, the alghoritm see the borders
    elif (col == 0): 
        return action=="u" or action =="r" or action =="d" 
    elif (row == 0):
        return action=="l" or action =="r" or action =="d"
    elif (col == columns):
        return action=="l" or action =="u" or action =="d"
    elif (row == rows):
        return action=="l" or action =="u" or action =="r" #fin
    #if the position is inside
    return True

#the transiction function change the new state
def TF(state, action):
    #deepcopy copy a new object incluse the lists inside of a object
    newState = State(copy.deepcopy(state.table), state.father)
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

#evaluate if a father have the same state (evit the repeat states).
def evaluateRepeatState(state):
    actual = state
    walker = state.father
    while (walker != None):
        if (goalTest(actual,walker)):
            return False
        walker = walker.father
    return True

#The algorithm search for levels while expand the next level

Counter = 0
def flatten(t):
    return tuple([item for sublist in t for item in sublist])
def DLSRecursiveSearchState(state,states,actions,limit):
        result = "failure"

        if (limit == 0) : return "cutoff", state   
        else:
            if (flatten(state.table) not in states):
                states.add(flatten(state.table))
                global Counter
                Counter+=1
            cutOffOcurred=False
            for a in actions:
                if (evaluateAction(state, a)):
                    successor = TF(state,a)
                    successor.father = state
                    if (evaluateRepeatState(successor)):
                        result, successor = DLSRecursiveSearchState(successor,states,actions,limit-1)
                    if(result == "cutoff"): cutOffOcurred=True
                    elif(result!="failure"): return result, successor
            if(cutOffOcurred):
                return "cutoff", state
            else: 
                return "failure", state
def DLSSearchState(initialState,actions):
    s = set()
    DLSRecursiveSearchState(initialState,s,actions,int(math.log2(math.factorial(len(initialState.table)**2))+1))
    return Counter