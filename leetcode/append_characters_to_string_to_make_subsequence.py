class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPtr, tPtr = 0,0
        while sPtr<len(s) and tPtr<len(t):
            # while sPtr<len(s) and tPtr<len(t) and s[sPtr]==t[tPtr]:
            if s[sPtr]==t[tPtr]:
                 tPtr += 1
            sPtr+=1
        return len(t)-tPtr