from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        for ch in s:
            t_counter[ch] = t_counter[ch] - 1
        for k,v in t_counter.items():
            if v:
                return k
