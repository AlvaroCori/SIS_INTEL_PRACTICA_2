from TF_of_n_pieces import *
#The algorithm search for levels while expand the next level
def BFS(initialState,goalState,actions):


    open = deque([initialState])
    counter = 0
    while (len(open) != 0):
        state = open.popleft()
        counter += 1
        if (goalTest(state, goalState)):
            return True, state,counter
        for a in actions:
            
            if (evaluateAction(state, a)):
                #print(state.table)
                #time.sleep(1)
                successor = TF(state, a)
                successor.father = state
                if (evaluateRepeatState(successor)):
                    if (goalTest(state, goalState)):
                        return True, state,counter
                    open.append(successor)
    return False, None,counter