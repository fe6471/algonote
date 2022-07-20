# Jump Game II [Medium]
# https://leetcode.com/problems/jump-game-ii/

# Solution1
# [idea]
# If it reached ith position with k jupms, it can reach i+1 to i+nums[i]th position with k+1 jumps.

# [code]
class Solution1:
    def jump(self, nums: List[int]) -> int:
        DP = [0]*len(nums)
        
        i = 0
        while i < len(nums):
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                if DP[j] == 0:
                    DP[j] = DP[i] + 1
            
            i += 1
                
        return DP[-1]
        
# time complexity : O(n^2)
# space complexity : O(n)

# Solution2
# [idea]
# Same idea as solution1. But it can skip positions calculated in the previous iteration.

# [code]
class Solution2:
    def jump(self, nums: List[int]) -> int:        
        l, r = 0, 0
        cnt = 0
        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(max_jump, i + nums[i])
            l = r + 1
            r = max_jump
            cnt += 1
                
        return cnt
        
# time complexity : O(n)
# space complexity : O(1)
