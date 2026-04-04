class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_curr = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_curr = max(max_curr, count)
                count = 0
            else:
                count += 1
        return max(max_curr, count)