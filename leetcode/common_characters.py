class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        checker = list(words[0])
        for word in words[1:]:
            curr = list(word)
            temp = []
            for c in checker:
                if c in curr:
                    temp.append(c)
                    curr.remove(c)
            checker = temp

        return checker