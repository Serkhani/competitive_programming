class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        strCount = s.count(letter)
        return int((strCount/len(s))*100)