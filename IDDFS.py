from TF_of_n_pieces import *

def DLSRecursive(state,goalState,actions,limit):
        result = "failure"
        if goalTest(state,goalState) : return "success", state
        elif (limit == 0) : return "cutoff", state   
        else:
            global Counter
            Counter+=1
            cutOffOcurred=False
            for a in actions:
                if (evaluateAction(state, a)):
                    successor = TF(state,a)
                    successor.father = state
                    if (evaluateRepeatState(successor)):
                        result, successor = DLSRecursive(successor,goalState,actions,limit-1)
                    if(result == "cutoff"): cutOffOcurred=True
                    elif(result!="failure"): return result, successor
            if(cutOffOcurred):
                return "cutoff", state
            else: 
                return "failure", state

#function
def IDDFS(initialState,goalState,actions):
        result = "failure"
        depth = 0
        counters = []
        while depth < 16:
            global Counter
            Counter = 0
            result, state = DLSRecursive(initialState,goalState,actions,depth)
            counters.append(Counter)
            if (result != "cutoff"):
                return result, state, counters
            depth = depth +1
        return result, None, counters
