class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        runningSum = 0
        n = len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (i==j):
                    runningSum += mat[i][j]
                elif(i+j == n-1):
                    runningSum += mat[i][j]
        return runningSum