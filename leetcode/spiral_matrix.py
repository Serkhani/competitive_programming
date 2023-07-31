class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        00 01 02 03 13 23 22 21 20 01 11 12
        
        """
        colNum = len(matrix[0])
        rowNum = len(matrix)
        output = []
        # while colNum:
        col = 0
        row = 0
        while col<colNum and row<rowNum:
            # top
            for i in range(col, colNum):
                output.append(matrix[row][i])
            row+=1
            # right
            for i in range(row, rowNum):
                output.append(matrix[i][colNum-1])
            colNum-=1
            if not (col<colNum and row<rowNum):
                break
            # bottom
            for i in range(colNum-1, col-1, -1):
                output.append(matrix[rowNum-1][i])
            rowNum -=1
            # left
            for i in range(rowNum-1, row-1, -1):
                output.append(matrix[i][col])
            col+=1
        return output