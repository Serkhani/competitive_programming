class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _str = ""
        if not len(strs) or not len(strs[0]):
            return _str
        idx = 1
        shortestStr = len(strs[0])
        while idx < len(strs):
            if len(strs[idx]) < shortestStr:
                shortestStr = len(strs[idx])
            idx+=1
        for idx in range(shortestStr):
            currChar = strs[0][idx]
            for s in strs:
                if currChar != s[idx]:
                    return _str
                currChar = s[idx]                
            _str += s[idx]
        return _str