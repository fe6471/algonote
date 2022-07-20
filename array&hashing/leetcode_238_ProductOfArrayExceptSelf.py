# Product of Array Except Self [Medium]
# https://leetcode.com/problems/product-of-array-except-self/

# Solution1
# [idea]
# Make a result array filled with ones. res = [1, 1, ..., 1]
# Product every elements in nums going through 0 to (i - 1) and product it res[i].
# Then res[i] contains product of nums[0] to nums[i - 1].
# Repeat above step backward again, then res[i] contains also product of nums[i + 1] to nums[n - 1].

# [code]
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        n = 1
        for i, num in enumerate(nums):
            res[i] *= n
            n *= num
        
        n = 1
        for i, num in enumerate(nums[::-1]):
            res[-(i+1)] *= n
            n *= num
        
        return res
        
# time complexity : O(n)
# space complexity : O(n)
