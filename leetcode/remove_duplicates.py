class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0,1
        nums_count = len(nums)
        while r<nums_count:
            while r < nums_count and nums[l] == nums[r]:
                r += 1#continue till you reach a point where there is not duplicate
            if r == nums_count:
                break
            nums[l+1] = nums[r]
            l+=1
            r+=1
            
        return l+1