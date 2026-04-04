class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights) - 1
        max_water = 0

        while s < e:
            between = e - s
            if heights[s] < heights[e]:
                max_water = max(max_water, heights[s] * between)
                s += 1
            else:
                max_water = max(max_water, heights[e] * between)
                e -= 1

        return max_water