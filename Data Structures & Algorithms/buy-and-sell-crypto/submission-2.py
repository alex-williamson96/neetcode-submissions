class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]

        profit = 0

        for num in prices:
            if num < low:
                low = num
                high = num
            else:
                profit = max(profit, num - low)
        return profit