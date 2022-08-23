# Jump Game [Medium]
# https://leetcode.com/problems/jump-game/

# Solution 1
# [idea]
# At ith position it can reach max(max_reach, i+nums[i]).
# If i is bigger than max_reach, it cannot reach the position.

# [code]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i <= max_reach:
                max_reach = max(max_reach, i + num)
            
            if max_reach >= len(nums) - 1:
                return True
        
        return False
        
# time complexity : O(n)
# space complexity : O(1)
