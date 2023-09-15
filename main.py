import numpy as np

def swapRows(matrix, i, j):
    matrix[[i, j]] = matrix[[j, i]]
    return matrix

# Writes the xor result between firstRowIndex and secondRowIndex to the secondRowIndex
def xorRowsInMatrix(matrix, firstRowIndex, secondRowIndex):
    matrix[secondRowIndex] = np.logical_xor(matrix[firstRowIndex], matrix[secondRowIndex])
    return matrix

def ref(inputMatrix):
    rows = inputMatrix.shape[0]
    columns = inputMatrix.shape[1]

    # Find and moving lead row
    indexForNextPositionOfLeadRow = 0
    indexColumnOfLeadingElement = -1
    while (True):
        # print("indexForNextPositionOfLeadRow = ", indexForNextPositionOfLeadRow)
        # print("indexColumnOfLeadingElement = ", indexColumnOfLeadingElement)
        # print("inputMatrix = ", inputMatrix)
        isMoveLeadRow = False
        for i in range(indexColumnOfLeadingElement + 1, columns):
            for j in range(indexForNextPositionOfLeadRow, rows):
                if inputMatrix[j][i]:
                    inputMatrix = swapRows(inputMatrix, indexForNextPositionOfLeadRow, j)
                    indexForNextPositionOfLeadRow += 1
                    indexColumnOfLeadingElement = i
                    isMoveLeadRow = True
                    break
            if (isMoveLeadRow):
                break
        if not isMoveLeadRow:
            return inputMatrix[0:indexForNextPositionOfLeadRow]

        # Making xor with rows
        for j in range(indexForNextPositionOfLeadRow, rows):
            if inputMatrix[j][indexColumnOfLeadingElement]:
                inputMatrix = xorRowsInMatrix(inputMatrix, indexForNextPositionOfLeadRow - 1, j)

if __name__ == '__main__':
    # matrix1 = np.array([[False, False, True],
    #                     [False,  True, True],
    #                     [False,  True, False],
    #                     [False,  True, True],
    #                     ])
    matrix1 = np.array([[True, False, True, True, False, False, False, True, False, False, True],
                        [False, False, False, True, True, True, False, True, False, True, False],
                        [False, False, False, False, True, False, False, True, False, False, True],
                        [True, False, True, False, True, True, True, False, False, False, False],
                        [False, False, False, False, True, False, False, True, True, True, False],
                        [True, False, True, True, True, False, False, False, False, False, False]]
                        )
    print(ref(matrix1))
