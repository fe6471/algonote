# Combination Sum II [Medium]
# https://leetcode.com/problems/combination-sum-ii/

# Solution1
# [idea]
# Each elements can be included or not (2^n).
# This can be implemented in recursive way.
# To avoid duplicates, skip if current element is same as previous one.
# If current sum is greater than target, no need to further search.

# [code]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def dfs(idx, subset, subset_sum):
            if subset_sum == target:
                combinations.append(subset)
                return
            if subset_sum > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, subset + [candidates[i]], subset_sum + candidates[i])

        dfs(0, [], 0)

        return combinations
      
# time complexity : O(2^n)
# space complexity : O(2^n)
