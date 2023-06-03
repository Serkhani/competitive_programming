class Solution:
    def interpret(self, command: str) -> str:
        d = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        string = ""
        l,r = 0,1
        while r<len(command):
            data = d.get(command[l:r], None)
            if data:
                string += data
                l = r 
                # r+=1
            r+=1
        string += d.get(command[l:r], None) if d.get(command[l:r], None) else ""
        return string