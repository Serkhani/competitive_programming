class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isZero = 0
        for rowIdx in range(len(matrix)):
            for colIdx in range(len(matrix[0])):
                if not matrix[rowIdx][colIdx]:
                    matrix[0][colIdx] = 0
                    if rowIdx:
                        matrix[rowIdx][0] = 0
                    else: isZero = 1
        print(matrix)
        for rowIdx in range(1,len(matrix)):
            if not matrix[rowIdx][0]:
                colIdx = 1
                while colIdx<len(matrix[0]):
                    matrix[rowIdx][colIdx] = 0
                    colIdx += 1
        for colIdx in range(1,len(matrix[0])):
            if not matrix[0][colIdx]:
                rowIdx = 1
                while rowIdx<len(matrix):
                    matrix[rowIdx][colIdx] = 0
                    rowIdx += 1
        if matrix[0][0]==0:
            for r in range(len(matrix)):
                matrix[r][0]=0
        if isZero:
            for c in range(len(matrix[0])):
                matrix[0][c]=0
                    