from numpy import matrix
from inputPuzzle import randomInput, inputFile
from puzzleSolver import *
import time

print("""
--- 15-Puzzle Solver ---
1. Random Input
2. File Input
3. Exit
""")

# Input Puzzle
inputOptions = input("Pilih: ")
while(inputOptions != "1" and inputOptions != "2" and inputOptions != "3"):
    print("Pilihan tidak tersedia")
    inputOptions = input("Pilih: ")
if(inputOptions == "1"):
    matrix = randomInput()
elif(inputOptions == "2"):
    matrix = inputFile()
elif(inputOptions == "3"):
    exit()

print("Matrix :")
printMatrix(matrix)



# Print all Kurang(i)
initialKurang(matrix)
print()

# Check if puzzle is solvable
if(isSolveable(matrix)):
    # Solve puzzle
    print("Puzzle dapat diselesaikan")
    print("Solving...\n")
    timeStart = time.time()
    solution, nodeCount = solve(matrix)
    timeEnd = time.time()

    # Initialize result
    result = []

    # Backtrack to root
    while(solution.parent != None):
        result.append(solution.move)
        solution = solution.parent

    # Reverse result
    result.reverse()

    # Print result
    printSteps(matrix, result)
    print("All Steps:", result)
    print("Total Steps:", len(result))
    print("Node Count:", nodeCount)

    print("Time: ", timeEnd-timeStart)
else:
    # Puzzle unsolvable
    print("Puzzle tidak dapat diselesaikan")