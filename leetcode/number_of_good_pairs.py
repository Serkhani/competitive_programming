from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def factorial(n: int) -> int:
            if n == 0 or n == 1: return 1
            else: return n * factorial(n-1)
        def combination(n:int)-> int:
            return factorial(n)//(2*factorial(n-2))
        
        count = 0
        for i in Counter(nums).values():
            if i > 1:
                count += combination(i)
        return count