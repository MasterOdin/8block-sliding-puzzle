8block-sliding-puzzle
=====================
Written for CSCI4150 (RPI)  

Algorithm to solve 8block-sliding-puzzle using A* algorithm

It utilizes a priority queue structure where each node has the cost to get to that node + it's heuristic cost.

Heuristic currently implemented is Hamiltonian Path.

This was made and tested in Python 2.7.5.

Main program execution is done in __main.py__ with puzzle specific functions (calculating new moves, checking if input is valid, etc.) is all done in __PuzzleFunctions.py__

Way to run program:
python main.py


Potential future considerations:  
1. Clean up code. There are parts that are a bit hacky and could be cleaned up for better readability.  
2. Allow better debug information to be printed out if the user so wanted.  
3. Probably add comments if someone wanted to use this as an example of what to do.  
4. Test on the larger (and more complicated) 15 block sliding puzzle (4x4)  
