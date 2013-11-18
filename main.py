'''
    Name:
        8-Block Solver

    Desc:
        Needs to solve the 8-block sliding puzzle using the A* search algorithm
        using Manhattan Distance as the heuristic function
        https://www.dropbox.com/s/mwpmtfr0t0qckfi/HW1.pdf

    Date Due:
        9-29-2013 @ 11:59pm

    Author:
        Matthew Peveler

    Notes:
        Made and run in Python 2.7.5
'''

import time
import Queue # allows Priority Queue functionality in Python
import PuzzleFunctions as f
from sys import exit # allows use of exit() function

# final state we want to get to
goalState = [['1','2','3'],['4','5','6'],['7','8','0']]

# get input
#print "Enter the initial puzzle state. Use numbers each of 0 to 8. Put three numbers for each input."
#x1 = raw_input("Enter the first line of 3 numbers:\n").replace(" ","")
#x2 = raw_input("Enter the second line of 3 numbers:\n").replace(" ","")
#x3 = raw_input("Enter the third line of 3 numbers:\n").replace(" ","")
x1 = raw_input().replace(" ","")
x2 = raw_input().replace(" ","")
x3 = raw_input().replace(" ","")
#print ""

start = time.time()

# convert three strings to list of lists format we use throughout program
initial = [x1,x2,x3]
initial = [[j for j in i] for i in initial]

# check for valid board configuration
if f.checkInput(initial) == False:
    exit(0)

# check to see we don't have the final state off the bat
state = [initial,0,None]
if initial == goalState:
    finalState = state
else:
    finalState = None

pQueue = Queue.PriorityQueue()
# format for put: [cost,state 3-tuple].
pQueue.put([0,state])
#f.printState(state)
# run till we get to that final board configuration as board is solvable.
prevPuzzles = []
count = 0
currentF = 10000000000
while finalState == None:
    currentState = pQueue.get()
    steps = currentState[1][1]
    puzzle = currentState[1][0]
    lastPuzzle = currentState[1][2]
    prevPuzzles.append([item for sublist in currentState[1][0] for item in sublist])
    #f.printState(currentState[1])
    moves = f.getMoves(puzzle)
    '''
        getMoves gives us a 2-tuple for four different directions:
        0 - next puzzle (None if none exist)
        1 - manhattan distance for that new puzzle state
    '''
    for i in range(4):
        if moves[i][0] != None:
            checkPrev = [item for sublist in moves[i][0] for item in sublist]
            if moves[i][0] == goalState:
                finalState = [moves[i][0], steps+1, currentState[1]]
            elif moves[i][0] != lastPuzzle and checkPrev not in prevPuzzles:
                # priority is steps(to last puzzle state)+1+manhattanDistance
                pQueue.put([(steps+1+moves[i][1]),[moves[i][0],steps+1,currentState[1]]])

moves = []
s = finalState
while True:
    if s[2] != None:
        moves.append(s[2])
        s = s[2]
        #print s
    else:
        break

moves.reverse()
for i in moves:
    f.printState(i)

f.printState(finalState)
#print "Program Execution time:",(time.time()-start),"seconds" 