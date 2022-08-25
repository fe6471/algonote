# Subsets II [Medium]
# https://leetcode.com/problems/subsets-ii/

# Solution1
# [idea]
# Each number can be either included or not in subsets. (total number of subsets : 2^n)
# If a number is not included in an ongoing subset, the subset should skip all the same duplicate numbers in next iterations.
# Otherwise it will produce duplicate subsets.
# For example, nums = [1,2,2]
# i = 0
# [] -> [1], []
# i = 1
# [1] -> [1,2], [1]
# [] -> [2], []
# i = 2
# [1,2] -> [1,2,2], [1,2]
# [1] -> [1,2], [1]       # duplicate
# [2] -> [2,2], [2]
# [] -> [2], []           # duplicate

# there are 2^n subsets and each subsets' time complexity is its length n at most, so the time complexity is O(n2^n).

# [code]
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                all_subsets.append(subset)
                return
            dfs(i + 1, subset + [nums[i]])
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return all_subsets
      
# time complexity : O(n2^n)
# space complexity : O(n2^n)
