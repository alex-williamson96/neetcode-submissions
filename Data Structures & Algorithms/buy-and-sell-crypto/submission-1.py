class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]

        profit = 0

        for num in prices:
            if num > high:
                high = num
                profit = max(profit, high - low)
            if num < low:
                low = num
                high = num
        return profit