class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in count:
                count[sorted_i].append(i)
            else:
                count[sorted_i].append(i)
        res = []
        for k, v in count.items():
            res.append(v)
        return res