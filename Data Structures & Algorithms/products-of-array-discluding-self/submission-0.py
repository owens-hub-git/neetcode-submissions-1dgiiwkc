class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = []
        post = [0] * len(nums)

        pre.append(nums[0])
        for i in range(1, len(nums)):
            pre.append(nums[i] * pre[i - 1])

        post[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i] * post[i + 1]

        for i in range(1, len(nums) - 1):
            res[i] = pre[i - 1] * post[i + 1]
        res[0] = post[1]
        res[len(res) - 1] = pre[len(pre) - 2]

        return res