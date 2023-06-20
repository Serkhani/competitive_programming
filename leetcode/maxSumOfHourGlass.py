class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rowLen = len(grid[0])
        columnLen = len(grid)
        hourGlassSums = []
        for col in range(columnLen-2):
            for row in range(rowLen-2):
                hourglassSum = sum(grid[col][row:row+3]) +grid[col+1][row+1] +sum(grid[col+2][row:row+3])
                hourGlassSums.append(hourglassSum)

        return max(hourGlassSums)