import heapq

def solve(matrix):
    # Branch and Bound Algorithm Solver
    
    #Initialize result
    result = []

    # Initialize Queue
    Q = PrioQueue()

    # Initialize visited
    visited = {}

    # Initialize parent
    parent = {}

    # Initialize depth
    depth = {}

    # Initialize cost
    cost = {}

    

    return result

    
def move(matrix, move):
    # Move matrix according to move
    row,col = find(16,matrix)

    if(move == "up"):
        matrix[row][col], matrix[row-1][col] = matrix[row-1][col], matrix[row][col]
    elif(move == "down"):
        matrix[row][col], matrix[row+1][col] = matrix[row+1][col], matrix[row][col]
    elif(move == "left"):
        matrix[row][col], matrix[row][col-1] = matrix[row][col-1], matrix[row][col]
    elif(move == "right"):
        matrix[row][col], matrix[row][col+1] = matrix[row][col+1], matrix[row][col]   

    return matrix


    
def isSolveable(matrix):
    #Check if puzzle is solvable
    totalKurang = 0
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != 16):
                totalKurang += kurang(matrix[i][j],matrix)

    row,col = find(16,matrix)
    if((row+col)%2 == 0):
        X = 0
    else:
        X = 1
    
    if ((totalKurang+X)%2 == 0):
        return True
    else:
        return False
            
def kurang(i,matrix):
    # Menghitung jumlah kurang dari i
    total = 0
    for j in range(4):
        for k in range(4):
            if(matrix[j][k] < i):
                total += 1
    return total

def find(x, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == x):
                return i,j
    return -1,-1

class PrioQueue:
    def __init__(self):
        self.queue = []
        self.index = 0
    
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1
    
    def pop(self):
        return heapq.heappop(self.queue)[-1]
    
    def isEmpty(self):
        return len(self.queue) == 0