class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverseInt(i: int) -> int:
            div = 10
            while i // (div * 10):
                div *= 10
            rem = 0
            while i // 10:
                rem += i % 10
                print(rem)
                rem *= 10
                print(rem)
                div //= 10
                i //= 10
            rem += i
            return rem

        numSet = set()
        for i in nums:
            numSet.add(i)
            if i < 10:
                continue
            numSet.add(reverseInt(i))
        return len(numSet)
# Time Complexity
# O(m*n)
# m: number len of nums
# n: number of digits of nums[i]
# Space Complexity
# O(n)
