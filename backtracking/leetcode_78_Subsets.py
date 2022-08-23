# Subsets [Medium]
# https://leetcode.com/problems/subsets/

# Solution1
# [idea]
# dp[i] means all subsets with size i.
# To make dp[i + 1], add num into subsets of dp[i] when only the num is not in subset.
# Sort the subset before append it to dp[i + 1] to avoid duplicates.
# This is CRAP!

# [code]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [[] for _ in range(n + 1)]
        dp[0].append([])

        i = 0
        while i < n:
            for num in nums:
                for subset in dp[i]:
                    if num not in subset:
                        tmp = subset + [num]
                        tmp.sort()
                        if tmp not in dp[i + 1]:
                            dp[i + 1].append(tmp)

            i += 1

        all_subsets = sum(dp, [])

        return all_subsets
'''
# time complexity : O(n2^n)
# space complexity : O(2^n)

# Solution2
# [idea]
# For each numbers, it can be picked or not.
# If it's picked, add the number in the all existing subsets.
# If not, leave the existing subsets just as they are.
# Say nums = [1,2,3].
# Base case, all_subsets = [[]]
# For 1, if pick - [1], if not [] -> all_subsets = [[],[1]]
# For 2, if pick - [2],[1,2], if not [],[1] -> all_subsets = [[],[1],[2],[1,2]]
# For 3, if pick - [3],[1,3],[2,3],[1,2,3], if not [],[1],[2],[1,2] -> all_subsets = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# [code]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        
        for num in nums:
            all_subsets += [subset + [num] for subset in all_subsets]
        
        return all_subsets
      
# time complexity : O(2^n)
# space complexity : O(2^n)
