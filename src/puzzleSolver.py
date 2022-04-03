import copy
from solverLibrary import PrioQueue, StateNode
import numpy as np

def solve(matrix):
    # Branch and Bound Algorithm Solver

    # Initialize NodeCount as 1 (root)
    NodeCount = 1

    # Initialize Queue
    PQ = PrioQueue(lambda x,y: x.cost < y.cost)

    # Initialize solutionNode as None
    solutionNode = None

    # Initialize visited
    visited = {}

    # Initialize goalMatrix
    goalMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    # Initialize root
    root = StateNode()
    root.matrix = matrix
    root.cost = calculateCost(matrix)

    # Add root to queue
    PQ.enqueue(root)

    # While queue is not empty
    while(not PQ.is_empty()):
        # Dequeue
        node = PQ.dequeue()

        # Check if node is goal
        if(node.matrix == goalMatrix):
            # Add node to result
            solutionNode = node
            break

        # Add node to visited
        visited[str(node.matrix)] = True

        # Get all possible moves
        moves = getMoves(node.matrix)

        # For each move
        for move in moves:

            # Move matrix
            moveMatrix = movePuzzle(node.matrix, move)

            # Check if moveMatrix is in visited
            if(str(moveMatrix) not in visited):
                # Create new node
                newNode = StateNode()
                newNode.matrix = moveMatrix
                newNode.parent = node
                newNode.depth = node.depth + 1
                newNode.cost = calculateCost(moveMatrix) + newNode.depth
                newNode.move = move

                # Add new node to queue
                PQ.enqueue(newNode)
                NodeCount += 1

    return solutionNode, NodeCount

def getMoves(matrix):
    # Get all possible moves from a state matrix
    moves = []
    row,col = find(16,matrix)
    if(row > 0):
        moves.append("up")
    if(row < 3):
        moves.append("down")
    if(col > 0):
        moves.append("left")
    if(col < 3):
        moves.append("right")
        
    return moves

def calculateCost(matrix):
    # Calculate cost of a state matrix
    cost = 0
    reshaped = np.reshape(matrix,(16,))
    for i in range(16):
        if(reshaped[i] != i+1):
            cost += 1
    return cost
    
def movePuzzle(matrix, move):
    # Move matrix according to move
    row,col = find(16,matrix)

    movedMatrix = copy.deepcopy(matrix)
    if(move == "up"):
        movedMatrix[row][col], movedMatrix[row-1][col] = movedMatrix[row-1][col], movedMatrix[row][col]
    elif(move == "down"):
        movedMatrix[row][col], movedMatrix[row+1][col] = movedMatrix[row+1][col], movedMatrix[row][col]
    elif(move == "left"):
        movedMatrix[row][col], movedMatrix[row][col-1] = movedMatrix[row][col-1], movedMatrix[row][col]
    elif(move == "right"):
        movedMatrix[row][col], movedMatrix[row][col+1] = movedMatrix[row][col+1], movedMatrix[row][col]   

    return movedMatrix


    
def isSolveable(matrix):
    #Check if puzzle is solvable

    row,col = find(16,matrix)
    if((row+col)%2 == 0):
        X = 0
    else:
        X = 1
    
    KurangX = kurang(matrix) + X
    print("sum Kurang(i) + X: ", KurangX)

    if ((KurangX)%2 == 0):
        return True
    else:
        return False
            
def kurang(matrix):
    # Menghitung total kurang dari sebuah matrix
    total = 0
    reshaped = np.reshape(matrix,(16,))
    for i in range(16):
        for j in range(i,16):
            if(reshaped[i] > reshaped[j]):
                total += 1
        
    return total

def initialKurang(matrix):
    # Mencetak setiap kurang dari sebuah matrix
    reshaped = np.reshape(matrix,(16,))
    dict = {}
    for i in range(16):
        kurangi = 0
        for j in range(i,16):
            if(reshaped[i] > reshaped[j]):
                kurangi += 1
        dict[reshaped[i]] = kurangi
    
    for i in range(16):
        print("Kurang("+ str(i+1) +") = ", dict[i+1])


def find(x, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == x):
                return i,j
    return -1,-1

def printMatrix(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 16):
                print("-", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()

def printSteps(matrix, result):
    # Print steps to solve the puzzle
    curMatrix = copy.deepcopy(matrix)
    print("Steps to solve the puzzle: \n")
    for i in range(len(result)):
        print("Step " + str(i+1) + ": " + result[i])
        curMatrix = movePuzzle(curMatrix, result[i])
        printMatrix(curMatrix)
        print()