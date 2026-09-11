class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                maxP = max(price, maxP)
            else:
                l = r
            r += 1
        return maxP

# Time: O(n)
# Space: O(1)