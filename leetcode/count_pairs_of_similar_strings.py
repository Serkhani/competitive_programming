from collections import Counter
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for idx in range(len(words)):
            words[idx] = ''.join(sorted(set(words[idx])))
        counter = Counter(words)
        print(counter)
        return sum((n*(n-1))//2 for n in counter.values())