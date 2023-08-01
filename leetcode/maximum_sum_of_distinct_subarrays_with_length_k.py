class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter(nums[:k])
        size = len(counter)
        runningSum = sum(nums[:k])
        maxSum = runningSum if size == k else 0
        for i in range(k, len(nums)):
            out, _in = nums[i-k], nums[i]
            counter[out] -= 1
            if not counter[out]:
                counter.pop(out)
                size -= 1
            if _in not in counter:
                size += 1
            counter[_in] += 1
            runningSum = runningSum + _in - out
            print(runningSum, size)
            if size == k:
                maxSum = max(runningSum, maxSum)
        return maxSum