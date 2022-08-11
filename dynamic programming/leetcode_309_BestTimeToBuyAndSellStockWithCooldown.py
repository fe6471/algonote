# Best Time to Buy and Sell Stock with Cooldown [Medium]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Solution1
# [idea]
# There are 3 states at each day buy, sell and cooldown.
# Let's say,
# buy[i] means maximum profit can be made when first i days ends with buy or cooldown. last two sequence (..., cooldown, buy) or (..., buy, cooldown)
# sell[i] means maximum profit can be made when first i days ends with sell or cooldown. last two sequence (..., buy, sell) or (..., sell, cooldown)
# cooldown[i] means maximum profit can be made when first i days ends with cooldown. last two sequence (..., buy, cooldown), (..., sell, cooldown) or (..., cooldown, cooldown)
# Base case
# buy[0] = -prices[0]
# sell[0] = -inf
# cooldown[0] = 0

# [code]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        cooldown = [0] * len(prices)

        buy[0] = -prices[0]
        sell[0] = float('-inf')

        for i in range(1, len(prices)):
            buy[i] = max(cooldown[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            cooldown[i] = max(sell[i - 1], buy[i - 1], cooldown[i - 1])

        return max(sell[-1], cooldown[-1])
      
# time complexity : O(n)
# space complexity : O(n)
