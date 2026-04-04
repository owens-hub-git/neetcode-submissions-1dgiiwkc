class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            int_prof = prices[r] - prices[l]
            profit = max(profit, int_prof)
        if profit <= 0:
            return 0
        return profit