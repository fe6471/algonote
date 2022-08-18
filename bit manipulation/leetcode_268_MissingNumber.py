# Missing Number [Easy]
# https://leetcode.com/problems/missing-number/

# Solution1 - math
# [idea]
# sum([0,n]) - sum(nums)

# [code]
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res
      
# time complexity : O(n)
# space complexity : O(1)

# Solution2 - bit manipulation
# [idea]
# n ^ n = 0
# m ^ 0 = m
# Say range is [0, n] and m is missing.
# If perform XOR on [0, n] and nums, every numbers become 0 except missing m.

# [code]
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
'''
# time complexity : O(n)
# space complexity : O(1)
