# Permutations [Medium]
# https://leetcode.com/problems/permutations/

# Solution1 - DFS
# [idea]
# Start with nums and an empty array permutation = [] which on going permutation numbers will be stored in.
# For every num in nums, append num into permutation array and pass (nums - num, permutation) to next iteration.
# If nums becomes empty, add permutation into result array.

# [code]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
    
        def dfs(_nums, permutation):
            if not _nums:
                permutations.append(permutation)
                return
            else:
                for i, num in enumerate(_nums):
                    dfs(_nums[:i] + _nums[i + 1:], permutation + [num])

        dfs(nums, [])

        return permutations
      
# time complexity : O(n!)
# space complexity : O(n!)
