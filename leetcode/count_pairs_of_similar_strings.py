class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for idx, word_x in enumerate(words):
            for word_y in words[idx+1:]:
                if set(word_x)==set(word_y):
                    count += 1
        return count