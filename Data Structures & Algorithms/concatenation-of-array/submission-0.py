class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)

        r = len(nums)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[r] = nums[i]

            r += 1
            
        return ans