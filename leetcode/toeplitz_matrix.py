class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def check_diagonal(col, row):
            val = matrix[row][col]
            while row<len(matrix) and col<len(matrix[0]):
                if not val == matrix[row][col]:
                    return False
                row += 1
                col += 1
            else: return True
        for r in range(1, len(matrix)):
            if not check_diagonal(0, r):
                return False
                
        for c in range(len(matrix[0])):
            if not check_diagonal(c,0):
                return False

        return True
            