# Longest Common Subsequence [Medium]
# https://leetcode.com/problems/longest-common-subsequence/

# Solution1
# [idea]
# If text1[i] = text2[j], found one common subsequence and the rest is reduced to subproblem of text1[i+1:] and text2[j+1:].
# Otherwise, it is either subproblem of text1[i+1:] and text2[j:] or subproblem of text1[i:] and text2[j+1:].

# [code]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[n][m]
      
# time complexity : O(nm)
# space complexity : O(nm)
