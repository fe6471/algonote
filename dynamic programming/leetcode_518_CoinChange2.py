# Coin Change 2 [Medium]
# https://leetcode.com/problems/coin-change-2/

# Solution1
# [idea]
# Let's start with coins = [1], amount = 1,2,3,4,5
# Then the number of combinations makes up to each amount = [1,1,1,1,1]
# Say coins = [1,2]
# amount = 1, number of combinations = 1, [(1)]
# amount = 2, number of combinations = 2, [(1+1), (2)]
# amount = 3, number of combinations = 2, [(1+1+1), (1+2)]
# amount = 4, number of combinations = 3, [(1+1+1+1), (1+1+2), (2+2)]
# amount = 5, number of combinations = 3, [(1+1+1+1+1), (1+1+1+2), (1+2+2)]
# the number of combinations makes up to amount j with i coins = (comb makes up to j without ith coin) + (comb makes up to j - ith coin)
# So, dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]] where j >= coins[i - 1]

# [code]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for base in dp:
            base[0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                dp[i][j] += dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[-1][-1]
      
# time complexity : O(nm)
# space complexity : O(nm)

# Solution2
# [idea]
# Since dp[i][j] only rely on dp[i - 1][j], it can be optimized the space by only using 1 dimensional array.

# [code]
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]

        return dp[-1]
'''
# time complexity : O(nm)
# space complexity : O(m)
