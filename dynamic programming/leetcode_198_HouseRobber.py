# House Robber [Medium]
# https://leetcode.com/problems/house-robber/

# Solution1
# [idea]
# For ith house, it can be choosed either nums[i] + rob[0:i - 2] or rob[0:i - 1].

# [code]
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2
      
# time complexity : O(n)
# space complexity : O(1)
