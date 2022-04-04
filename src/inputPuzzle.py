def inputFile():
    # Masukan file
    print("Masukan nama file: ", end="")
    fileName = input()
    file = open("./tes/"+fileName, "r")
    matrix = []
    for line in file:
        matrix.append(list(line.split()))

    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == '-' or matrix[i][j] == '0'):
                matrix[i][j] = 16
            else:
                matrix[i][j] = int(matrix[i][j])

    return matrix

def randomInput():
    # Masukan random
    import numpy as np
    matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    matrix = matrix.ravel()
    np.random.shuffle(matrix)
    matrix = matrix.reshape(4,4)
    matrix = matrix.tolist()

    return matrix