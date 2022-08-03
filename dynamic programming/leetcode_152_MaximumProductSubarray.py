# Maximum Product Subarray [Medium]
# https://leetcode.com/problems/maximum-product-subarray/

# Solution1
# [idea]
# At any index i of the list, there are two choices.
# Product nums[i] to maximum product subarray ending at i - 1 or reset the starting position at i.
# If nums[i] is negative, current max is either nums[i] * previous min or nums[i] itself.
# 

# [code]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max(nums)
        current_max, current_min = 1, 1
        
        for num in nums:
            if num < 0:
                current_max, current_min = current_min, current_max
                
            current_max = max(num * current_max, num)
            current_min = min(num * current_min, num)
            max_product = max(max_product, current_max)
        
        return max_product
      
# time complexity : O(n)
# space complexity : O(1)

# Solution2
# [idea]
# If all numbers in the array are non zeros, the maximum product of subarray should either start at the first or end at the last.
# Let's say there is a subarray nums[i:j] where 0 < i < j < n and the product of all elements inside the array P is positive.
# If nums[i-1] > 0 or nums[j] > 0, then it should be extended as nums[i-1:j] or nums[i:j+1].
# If nums[i-1] < 0 and nums[j] <0, then it should be extended as nums[i-1:j+1]
# Repeating above steps leads to i = 0 or j = n eventually.
# If there is zero in the array, it becomes subproblems with subarrays without zeros.

# [code]
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, max_product = 0, 0, float('-inf')
        
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_product = max(prefix, suffix, max_product)
            
        return max_product
'''
# time complexity : O(n)
# space complexity : O(1)
