# Min Cost Climbing Stairs [Easy]
# https://leetcode.com/problems/min-cost-climbing-stairs/

# Solution1
# [idea]
# Let's say dp[i] means minimum cost to get to top from ith position.
# Since it can take either one step or two steps, dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]

# [code]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]
        
        for i in range(len(cost) - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        
        return min(dp[0], dp[1])
      
# time complexity : O(n)
# space complexity : O(n)

# Solution2
# [idea]
# Same idea but don't need extra space.

# [code]
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
'''
# time complexity : O(n)
# space complexity : O(1)
