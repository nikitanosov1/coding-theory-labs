import numpy as np

def swapRows(matrix, i, j):
    currentMatrix = matrix.copy()
    currentMatrix[[i, j]] = currentMatrix[[j, i]]
    return currentMatrix

# Writes the xor result between firstRowIndex and secondRowIndex to the secondRowIndex
def xorRowsInMatrix(matrix, firstRowIndex, secondRowIndex):
    currentMatrix = matrix.copy()
    currentMatrix[secondRowIndex] = np.logical_xor(currentMatrix[firstRowIndex], currentMatrix[secondRowIndex])
    return currentMatrix

def ref(inputMatrix):
    matrix = inputMatrix.copy()
    rows = matrix.shape[0]
    columns = matrix.shape[1]

    # Find and moving lead row
    indexForNextPositionOfLeadRow = 0
    indexColumnOfLeadingElement = -1
    while (True):
        isMoveLeadRow = False
        for i in range(indexColumnOfLeadingElement + 1, columns):
            for j in range(indexForNextPositionOfLeadRow, rows):
                if matrix[j][i]:
                    matrix = swapRows(matrix, indexForNextPositionOfLeadRow, j)
                    indexForNextPositionOfLeadRow += 1
                    indexColumnOfLeadingElement = i
                    isMoveLeadRow = True
                    break
            if (isMoveLeadRow):
                break
        if not isMoveLeadRow:
            return matrix[0: indexForNextPositionOfLeadRow]

        # Making xor with rows
        for j in range(indexForNextPositionOfLeadRow, rows):
            if matrix[j][indexColumnOfLeadingElement]:
                matrix = xorRowsInMatrix(matrix, indexForNextPositionOfLeadRow - 1, j)

if __name__ == '__main__':
    matrix1 = np.array([[False, False, True],
                        [False,  True, True],
                        [False,  True, False],
                        [False,  True, True],
                        ])
    # matrix1 = np.array([[True, False, True, True, False, False, False, True, False, False, True],
    #                     [False, False, False, True, True, True, False, True, False, True, False],
    #                     [False, False, False, False, True, False, False, True, False, False, True],
    #                     [True, False, True, False, True, True, True, False, False, False, False],
    #                     [False, False, False, False, True, False, False, True, True, True, False],
    #                     [True, False, True, True, True, False, False, False, False, False, False]]
    #                     )
    print(ref(matrix1))
    print(matrix1)
