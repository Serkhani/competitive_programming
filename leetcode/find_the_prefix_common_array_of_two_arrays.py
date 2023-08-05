class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        commons = set()
        count = 0
        ptr = 0
        arr = []
        while ptr<len(A):
            if A[ptr]==B[ptr]:
                count+=1
                commons.add(A[ptr])
            else:
                if A[ptr] in commons:
                    count+=1
                else: commons.add(A[ptr])
                if B[ptr] in commons:
                    count+=1
                else:commons.add(B[ptr])
            
            arr.append(count)
            ptr+=1
        return arr
