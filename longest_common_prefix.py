# def longestCommonPrefix(strs: list[str]) -> str:
#         index = 0
#         _str = ""
#         while index<len(strs[0]):#it will be the least if all is present
#             currChar = ""
#             for s in strs:
#                 if currChar and currChar != s[index]:
#                     return _str
#                 currChar = s[index]                
#             _str += s
#             index+=1
#             print(_str)

def longestCommonPrefix(strs: list[str]) -> str:
        index = 0
        _str = ""
        while index<len(strs[0]):#it will be the least if all is present
            currChar = strs[0][0]
            for s in strs:
                if currChar != s[index]:
                    return _str
                print(currChar)
                currChar = s[index]                
            _str += s[index]
            index+=1


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))