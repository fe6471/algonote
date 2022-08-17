# Target Sum [Medium]
# https://leetcode.com/problems/target-sum/

# Solution1
# [idea]
# At each num in nums, there are two decisions +num and -num.
# So brute force solution would be O(2^n) time complexity.
# Keep track what index we are at now and current sum so far with parameter (index, current_sum).
# Since there can be multiple branches with same (index, current_sum) pairs,
# we can reduce duplicate search by using cache (backtracking).

# [code]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def backtrack(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            elif (index, current_sum) in dp:
                return dp[(index, current_sum)]
            
            dp[(index, current_sum)] = (backtrack(index + 1, current_sum + nums[index]) 
                                        + backtrack(index + 1, current_sum - nums[index]))
            return dp[(index, current_sum)]
        
        return backtrack(0, 0)
      
# time complexity : O(nt)
# space complexity : O(nt)
