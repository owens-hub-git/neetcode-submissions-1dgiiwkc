class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s, t_s = sorted(s), sorted(t)
        return s_s == t_s