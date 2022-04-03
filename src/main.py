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
for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()

timeStart = time.time()

# Check if puzzle is solvable
if(isSolveable(matrix)):
    # Solve puzzle
    solve(matrix)
else:
    # Puzzle unsolvable
    print("Puzzle tidak dapat diselesaikan")

timeEnd = time.time()

print("Time: ", timeEnd-timeStart)