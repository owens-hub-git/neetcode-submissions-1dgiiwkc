class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)):
            if i == len(arr) - 1:
                res.append(-1)
                break
            r = i + 1
            curr_max = 0
            while r < len(arr):
                if arr[r] > curr_max:
                    curr_max = arr[r]

                r += 1
            res.append(curr_max)
        return res