# House Robber II [Medium]
# https://leetcode.com/problems/house-robber-ii/

# Solution1
# [idea]
# If rob house[0] then cannot rob house[n - 1].
# Choose either house[0] or house[n-1] then it becomes 'House Robber I'.

# [code]
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.house_robber_1(nums[:-1]), self.house_robber_1(nums[1:])) # edge case when len(nums) = 1 -> nums[0]
        
    def house_robber_1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2
      
# time complexity : O(n)
# space complexity : O(1)
