class Solution:
    def average(self, salary: List[int]) -> float:
        _min, runningSum, _max = float('inf'), 0, float('-inf')
        for sal in salary:
            _min = min(sal, _min)
            runningSum += sal
            _max = max(sal, _max)
        runningSum -= (_min+ _max)
        return runningSum/(len(salary)-2)