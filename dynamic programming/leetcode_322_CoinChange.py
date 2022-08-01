# Coin Change [Medium]
# https://leetcode.com/problems/coin-change/

# Solution1
# [idea]
# Bottom-up approach
# Base case: amount = 0, count = 0
# From 1 to amount, if i >= coin, count = dp[i - coin] + 1.

# [code]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[-1] == float('inf'):
            dp[-1] = -1
        return dp[-1]
      
# time complexity : O(n*amount)
# space complexity : O(n)
