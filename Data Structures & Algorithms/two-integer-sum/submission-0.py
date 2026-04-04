class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map = {}

        for i, v in enumerate(nums):
            dif = target - v
            if dif in res_map:
                return [res_map[dif], i]
            else:
                res_map[v] = i