class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minIdx = i
            for j in range(i, len(nums)):
                if nums[minIdx]>nums[j]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]