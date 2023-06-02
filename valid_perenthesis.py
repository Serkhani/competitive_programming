class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            '{' : '}',
            '}' : '{',
            '[' : ']',
            ']' : '[',
            '(' : ')',
            ')' : '('
        }
        car = {'}', ']',')'}
        stack = []
        for i in s:
            if stack and data[stack[-1]] == i:
                stack.pop()
            else: 
                if i not in car:
                    stack.append(i)
                else: return False
        return not stack
            