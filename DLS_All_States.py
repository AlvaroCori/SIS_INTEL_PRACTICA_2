from TF_of_n_pieces import *
Counter = 0
# the function flatten the table and convert in a tuple
def flatten(t):
    return tuple([item for sublist in t for item in sublist])
#search the states using DLS and recursivity
def DLSRecursiveSearchState(state,states,actions,limit):
        result = "failure"

        if (limit == 0) : return "cutoff", state   
        else:
            #We save the different states in a set structure which realize a insert and search of O(1) time complexity 
            if (flatten(state.table) not in states):
                states.add(flatten(state.table))
                global Counter
                Counter+=1
            cutOffOcurred=False
            for a in actions:
                if (evaluateAction(state, a)):
                    successor = TF(state,a)
                    successor.father = state
                    if (flatten(state.table) in states):
                        result, successor = DLSRecursiveSearchState(successor,states,actions,limit-1)
                    if(result == "cutoff"): cutOffOcurred=True
                    elif(result!="failure"): return result, successor
            if(cutOffOcurred):
                return "cutoff", state
            else: 
                return "failure", state
#We search the tree until the 30 level
def DLSSearchState(initialState,actions):
    global Counter
    Counter = 0
    s = set()
    DLSRecursiveSearchState(initialState,s,actions,20)
    return Counter
    