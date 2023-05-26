class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        _str = ""
        shorterStr = len(word1) if len(word1)<len(word2) else len(word2)
        ptr = 0
        while ptr < shorterStr:
            _str += word1[ptr]            
            _str += word2[ptr]            
            ptr+=1
        if len(word1) > len(word2):
            _str += word1[ptr:]
        else:
            _str += word2[ptr:]
        return _str