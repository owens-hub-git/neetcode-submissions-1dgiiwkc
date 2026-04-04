class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = n / 2

        counted = Counter(nums)

        for k, v in counted.items():
            if v > major:
                return k