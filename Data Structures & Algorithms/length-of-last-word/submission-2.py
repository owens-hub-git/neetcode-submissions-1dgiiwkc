class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        if len(s) == 1: return 1

        while s[last] == " ":
            last -= 1
        
        start = last
        print(start)

        while s[start] != " ":
            start -= 1
        
        return last - start