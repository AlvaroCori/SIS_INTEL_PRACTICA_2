# Sis Inteligentes - Práctica 2
## Nombres:
#### Alvaro Bryan Cori Sanchez
#### Ruyasi Chanove Guzman

### Description of the Problem

The 8 puzzle is a game invented in 1874 by Noyes Palmer Chapmen. It’s based on a table of 3x3 cells of equal size. With 8 pieces and a free space. The objective of the game is moving the pieces in the free space (up, left, right and down) to achieve an arrangement that is previously given. In this case, the numbers are shown on an image.

This problem could have less or greater complexity, usually determined by size which we will name n in this documentation. If we take a table of 2x2 (3-puzzle) or a table of 4x4 (15-puzzle). The quantity of movements that are required increases by a lot. 

### Description of the Solution

This problem can be solved in various ways. But in this practice, we will solve it using Breadth First Search (BFS) and Iterative Deepening (IDDFS).

#### Breadth First Search (BFS)

Is a searching algorithm that traverses by levels which is based in a tree using a structure called Queue. A Queue is a linear structure that contains the elements and places the elements always first, in other words a FIFO structure (First in First Out).

This algorithm works, searching by levels from the first node, then their direct successors and then the successors of these. The expansion of new successors occurs when we compare the objective state with the first of the queue, then we aggregate the successors in the queue, or to say it in other words, we pop the first node and if isn’t the objective state we append their successor and if we don’t get the objective state, we continue expanding/appending new nodes.

#### Iterative Deepening (ID)

The algorithm is based in DLS (Deep Limited Search) and in the DFS (Depth First Search).
The algorithm is like we traverse a tree of variable height with DLS, then the algorithm will travel through the first node and if it does not find the objective state, then will travel to the second level, if it doesn’t find it, it will keeping looking to the next level and expanding itself, if it is not in the level, the way in which it looks for it it’s by depth.
The algorithm has 3 outputs, “success” is when the goal is found, “cutoff” is when the depth limit is reached, and “failure” is when all the tree is traversed, and the goal isn’t found.
The language used for the implementation of the algorithms is Python 3. This is a high-level language with many tools and libraries that we can take advantage of, which is tested by the queue, stack, read text files, use of OOP and other functionalities.

#### Experiments And Results

###### Initial State:

A table with a random order of elements.

###### Goal State:
A table with a sequential order of elements (1,2,3,…,n  * n-1,0)
###### Actions:
Move the pieces to the free space. Minimum of 2 (for the corners). 3 (for the borders). And 4 for the middle squares.
###### Transition Module:
Action => (up,left, right, down)
Transition(actualState, action)
###### Test of the target:
Check that the current state is the target state.
###### Cost of the path:
The quantity of states that the algorithms visited.

 

### EXPERIMENTS
###### Experiments of N=2 (3_puzzle):
For 3-Puzzle, we could take two different paths. Each of them has states that the other one couldn’t achieve. For example in the path of the left, both routes traverse to the objective state. The right one is longer than the left one. Also, it’s notable that the right path couldn’t achieve the objective state even when we expanded every possible state.
For the left path, we got 11 different states, and for the right one we got 13 different states, which gives us the result of 24 different combinations without repetitions that we could achieve on a 3-puzzle with an empty square.

The states that were generated manually demonstrate that the input generates different states in the initial state of 3_puzzle. Both initial states are of 3 pieces, but the first has a degree of 2, and the other one has degree of 1.

On the left example, the possible paths constraints two actions right square and up squares. Moving the piece at the left generates a greater quantity of states than the 4 states that generate the transition of when we move down the piece in the initial state.

On the right path, it doesn’t matter which direction you choose to move a piece, any of the paths could achieve the objective states.

###### Manually search for n = 2.
###### Initial State:
 2 3
 1 0
###### Objective State:
 1 2
 3 0
###### Path from initial state to goal state.
[[2, 3],
 [1, 0]]

[[2, 0],
 [1, 3]]

[[0, 2],
 [1, 3]]

[[1, 2],
 [0, 3]]

[[1, 2],
 [3, 0]]
 
###### Height: 4
Number of total states (BFS): 11
Number of total states (IDDFS): 11
 
##### Initial State:
 1 3
 2 0
##### Objective State:
 1 2
 3 0
There's no path from initial state to final state.

##### Height: 11
Number of total states (BFS): 13
Number of total states (IDDFS): 13
 
 
##### Experiments of N=3 (8-Puzzle)
We are implementing an algorithm to search the total of states of a random sequence of numbers for a table of 3 x 3 pieces. We implemented the DLS (Depth Limited Search) algorithm with a height that is calculated from the number of table pieces.

##### Initial State:
  1 2 3
  7 4 6
  0 5 8

###### Objective State:
  1 2 3
  4 5 6
  7 8 0

##### Number of all different states: 26931 states.
Height: 19
We used a prefixed initial state and traversed through a state space search.  Using DFS and a counter.
Clarify that we didn't reach the theoretical value of 9!/2 possible states. Nor the maximum value of 9!

Experiments of N=4:
We compared the number of states, time of execution and space of execution with the algorithms BFS and ID.
In the worst case scenario, we will go until the last state searching the objective state and while we are searching, we check if we are repeating the same state, from the new state to the last of their ancestors recurring in a n log(n) time complexity.
 
Initial State:
  5   1   3   4
  2 10   6   7
  9   0 12   8
13 14 11 15

Objective State:
  1   2   3   4
  5   6   7   8
  9 10 11 12
13 14 15   0
 
Path from initial state to goal state.
[[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]]
[[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
Height = 11 
BFS
Number of states from initial state to goal state:  8516 states
Time of Execution:
The algorithm executed in 7.93 seconds.
 Space of Execution:
S = O(b^d)
S = 4^11 * (32 * 16) bits
S = 2147483648 bits => S = 2.15 Gigabits
   	N: The quantity of total states.
 
IDDFS
Number of states from initial state to goal state: 1386 states.
Time of Execution:
   	The algorithm executed in 5.28 seconds.
Space of Execution:
S = O(b*d)
S = 4*11 * (32 * 16) bits
S = 22528 bits => S = 122.528 kilobits
Given the initial state of ![initialState.url] and the objectiveState of ![objectiveState]. We compared the time execution which theoretically is O(b^d) where b=branches, and d = depth. This is contrasted by a timer on our program which gives the time: (insert time)
About space complexity we are just getting the Queue.size() for the BFS and the Stack.Size() for the IDDFS.
Log(d) is aggregated on both time complexities, BFS and IDDFS. Because the algorithm searches repeated states until the first state.

 
 
Conclusions
We implemented both algorithms using some Python libraries to simplify the implementation of algorithm structure, as well as some tweaks like reading from text files.

For the first experiment we manually expanded the tree of two different initial cases. One with solution and one without solution. By this way, we managed to get all states in a table of 2x2, the total different states are 24 which prove all the possible theoretical states (4! = 24).

For the second experiment we put a table with a random order in order to get all different states in the algorithm. If we desire get all combinations (factorial of 9) we need to move the pieces in differents initial states.

For the third experiment we compare the quantity of states, the time execution and the space execution. This experiment checks the bigger difference between BFS and IDDFS. While BFS needs a lot of time, the IDDFS only needs a small fraction. 

The BFS algorithm consumes very much space while the IDDFS needs less space. For the difference in quantity of states, the BFS uses too many states while the algorithm searches level for level, while the IDDFS searches in profundity and uses less states. 

To clarify, in a worst case scenario in which both algorithms search for the same goal that is in the last state of the three, both algorithms use the same quantity of states.

Bibliography
Tail of Python: (from collections import deque)
https://docs.hektorprofe.net/python/colecciones-de-datos/colas/
 Copy objects: (import copy)
https://pymotw.com/2/copy/

8-puzzle Solver:
https://deniz.co/8-puzzle-solver/s
 
Obtain the actual path: (import os)
https://www.delftstack.com/es/howto/python/python-get-path/
 
Open input from file txt:
https://decodigo.com/python-leer-un-archivo-de-texto

An example of Iterative Deepening (IDDFS):
    	https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
How python treats the stack:
https://www.geeksforgeeks.org/stack-in-python/
Game-Trees:
https://www.andrew.cmu.edu/course/15-121/lectures/Game%20Trees/Game%20Trees.html
 

