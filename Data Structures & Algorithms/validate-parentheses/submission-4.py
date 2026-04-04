class Solution:
    def isValid(self, s: str) -> bool:
        paren = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []
        if len(s) < 2:
            return False

        for char in s:
            if char in paren:
                if stack and stack[-1] == paren[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True