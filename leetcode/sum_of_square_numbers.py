import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, math.sqrt(c)//1
        while i<=j:
            if i*i+j*j > c:
                j-=1
            elif i*i+j*j < c:
                i+=1
            else: return True
        return False