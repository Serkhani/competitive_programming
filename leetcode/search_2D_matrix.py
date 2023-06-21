class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = [0,0],[len(matrix)-1, len(matrix[0])-1]
        # while l<=r:
        #     m = [l[0]+r[0]]//2,l[0]+r[0]]//2]
        data = []
        for arr in matrix:
            for i in arr:
                data.append(i)
        l,r = 0, len(data)-1
        while l<=r:
            m = (l+r)//2
            if data[m]== target:
                return True
            if data[m]<target:
                l = m+1
                continue
            r = m-1
        return False