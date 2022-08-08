# Unique Paths [Medium]
# https://leetcode.com/problems/unique-paths/

# Solution1 - math
# [idea]
# Permutation with repetition.
# Answer = (m + n - 2)!/(m - 1)!(n - 1)!

# [code]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 1
        j = 1
        for i in range(n, m + n - 1):
            paths *= i
            paths //= j
            j += 1

        return paths
      
# time complexity : O(m+n)
# space complexity : O(1)

# Solution2 - dynamic programming
# [idea]
# dp[r][c] is number of paths from (0, 0) to (r, c).
# There are 2 ways to get to (r, c) : Move 1 down from (r - 1, c), move 1 right from (r, c - 1)
# So dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

# [code]
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[-1][-1]
'''
# time complexity : O(m * n)
# space complexity : O(m * n)
