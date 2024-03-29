# Maximum Subarray [Easy]
# https://leetcode.com/problems/maximum-subarray/

# [idea]
# Negative sum has no use to the next value, so break.

# [code]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = float('-inf')
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        
# time complexity : O(n)
# space complexity : O(1)
