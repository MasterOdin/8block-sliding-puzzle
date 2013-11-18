'''
    Name:
        PuzzleFunctions
    Desc:
        Implements functions used for an 8-block puzzle
    Author:
        Matthew Peveler
'''
import copy #needed so we can create a "deep copy" of the list for swap

# the final puzzle configuration we want to get to
goalState = [['1','2','3'],['4','5','6'],['7','8','0']]

# flat list of all numbers to check against user input
check = ['0','1','2','3','4','5','6','7','8']

'''
checkInput(puzzle):
puzzle - a list of lists for the puzzle

Checks the puzzle to make sure there are 9 elements,
that none of the elements are repeated and that 0-8 are all used
and that it satisifies the rule for inversions for solvibility:
http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html

retuns False on invalid boards, and True for valid boards
'''
def checkInput(puzzle):
    flatList = [item for sublist in puzzle for item in sublist]
    i = sorted(flatList)
    if len(i) != 9:
        print "You must enter 9 digits (0 to 8) for the input."
        return False
    if check != i:
        print "The input must contain only one of each of the 9 (0 to 8) digits."
        return False
    inversions = 0
    for i in range(len(flatList)):
        for j in range((i+1),len(flatList)):
            if flatList[j] == '0':
                continue
            if flatList[i] > flatList[j] and flatList[j] != '0' and flatList[i] != '0':
                inversions += 1
    if inversions%2 != 0:
        print "This is an invalid board configuration. Please enter a valid one."
        return False
    return True

'''
getMoves(puzzle):
puzzle - a list of lists for the puzzle

Return a 2-tuple for the four different directions (up, down, left, right)
the blank can swap to. If a direction is invalid, return None as the first element
of the tuple, while if valid, return [new_puzzle_configuration,manhattan_distance]
for that particular move.
'''
def getMoves(puzzle):
    blank = getBlank(puzzle)
    up,down,left,right = (None,)*4
    upDist,downDist,leftDist,rightDist = (0,)*4
    if blank[1] > 0:
        up = swap(puzzle,blank,[blank[0],(blank[1]-1)])
        upDist = getManhattanDistance(up)
    if blank[1] < 2:
        down = swap(puzzle,blank,[blank[0],(blank[1]+1)])
        downDist = getManhattanDistance(down)
    if blank[0] > 0:
        left = swap(puzzle,blank,[(blank[0]-1),blank[1]])
        leftDist = getManhattanDistance(left)
    if blank[0] < 2:
        right = swap(puzzle,blank,[(blank[0]+1),blank[1]])
        rightDist = getManhattanDistance(right)
    return [[up,upDist],[down,downDist],[left,leftDist],[right,rightDist]]

'''
swap(puzzle,square1,square2)
puzzle - a list of lists for the puzzle
square1 - 2-tuple of [x,y] coordinates of one square to swap
square2 - 2-tuple of [x,y] coordinates of other square to swap

swap values of square1 and square2 in puzzle
'''
def swap(puzzle,square1,square2):
    new = copy.deepcopy(puzzle)
    temp = new[square1[1]][square1[0]]
    new[square1[1]][square1[0]] = new[square2[1]][square2[0]]
    new[square2[1]][square2[0]] = temp
    return new

'''
getManhattanDistance(puzzle)
puzzle - a list of lists for the puzzle

get sum of the number of tiles a square is from its final position
for all squares in the puzzle
'''
def getManhattanDistance(puzzle):
    distance = 0
    for i in range(len(goalState)):
        for j in range(len(goalState[i])):
            if goalState[i][j] == '0':
                continue
            for k in range(len(puzzle)):
                if goalState[i][j] in puzzle[k]:
                    distance += abs((k-i)) + abs((puzzle[k].index(goalState[i][j])-j))
    return distance

'''
getBlank(puzzle):
puzzle - a list of lists for the puzzle

return 2-tuple of [x,y] coordinates for where '0' is in puzzle
'''
def getBlank(puzzle):
    count = len(puzzle)
    for i in range(count):
        if '0' in puzzle[i]:
            return [puzzle[i].index('0'),i]

'''
printState(state)
state - 3-tuple of [puzzle,steps,lastPuzzleConfiguration]

prints out a given state to console
'''
def printState(state):
    #print state[1],"step so far to get to:"
    printPuzzle(state[0])

'''
printPuzzle(puzzle):
puzzle - a list of lists for the puzzle

prints out a puzzle configuration in human-readable fashion
to console
'''
def printPuzzle(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != '0':
                print puzzle[i][j],
            else:
                print " ",
            if j == 2:
                print
            #else:
                #print "",
        #print ""
    print ""
        