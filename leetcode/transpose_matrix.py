class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transposed = []
        for columnIdx in range(len(matrix[0])):
            rows = [matrix[row][columnIdx] for row in range(len(matrix))]
            transposed.append(rows)
        return transposed