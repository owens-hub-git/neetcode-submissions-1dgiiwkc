class Solution:
    def isValid(self, s: str) -> bool:
        close_and_open = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for char in s:
            if char in close_and_open:
                if stack and stack[-1] == close_and_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False