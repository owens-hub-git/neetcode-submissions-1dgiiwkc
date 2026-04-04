class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        
        for i in range(1, len(s)):
            this_ord = ord(s[i])
            prev_ord = ord(s[i - 1])
            res = res + abs(this_ord - prev_ord)
        return res