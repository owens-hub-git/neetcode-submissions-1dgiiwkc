class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s, t_s = Counter(s), Counter(t)
        return s_s == t_s