class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        for tPtr in range(len(t)):
            if sPtr==len(s): break
            if t[tPtr]==s[sPtr]:
                sPtr+=1
        return sPtr==len(s)