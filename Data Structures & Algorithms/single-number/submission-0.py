class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)

        for k, v in counted.items():
            if v != 2:
                return k