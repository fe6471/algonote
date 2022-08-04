# Longest Increasing Subsequence [Medium]
# https://leetcode.com/problems/longest-increasing-subsequence/

# Solution1 - dynamic programming
# [idea]
# Let's say length of the longest increasing subsequence starting at i th index is LIS[i].
# For index j from i + 1 to n - 1, if nums[i] is less than nums[j], i and increaing subsequence starting at j can form longer subsequence.
# So, LIS[i] = max(1, 1 + LIS[j]) all j where i < j < n and nums[i] < nums[j].

# [code]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
    
        for i in range(len(nums) - 2, -1, -1):
            lengths = [1]
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lengths.append(1 + LIS[j])
            LIS[i] = max(lengths)

        return max(LIS)
      
# time complexity : O(n^2)
# space complexity : O(n)

# Solution2 - binanry search (patience sort)
# [idea]
# Stpe 1 : Put first num into pile1(array).
# Step 2 : If num is greater than last pile's smallest num, put it into next pile.
#          If not, among the smallest nums of each piles, find the smallest num which is greater than or equal to the target num and put it into the pile.
# Step 3 : Return the number of piles as result.

# Let's apply above steps to nums = [10, 11, 2, 5, 3, 7, 101, 18].
# pile1 = [10]
# pile1 = [10], pile2 = [11]
# pile1 = [10, 2], pile2 = [11]
# pile1 = [10, 2], pile2 = [11, 5]
# pile1 = [10, 2], pile2 = [11, 5, 3]
# pile1 = [10, 2], pile2 = [11, 5, 3], pile3 = [7]
# pile1 = [10, 2], pile2 = [11, 5, 3], pile3 = [7], pile4 = [101]
# pile1 = [10, 2], pile2 = [11, 5, 3], pile3 = [7], pile4 = [101, 18]
# It is guaranteed that each numbers of any piles can have path to previous adjacent pile in ascending order.

# We only need the number of piles for LIS so we don't actually need to store all numbers in piles.
# Keep the smallest numbers of each piles and update it and return the number of piles.

# [code]
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = [nums[0]]

        for num in nums[1:]:
            if piles[-1] < num:
                piles.append(num)
            else:
                i = self.binarySearch(piles, num)
                piles[i] = num

        return len(piles)
    
    def binarySearch(self, array: List[int], target: int) -> int:
        l, r = 0, len(array) - 1

        res = -1
        while l <= r:
            m = (l + r) // 2

            if array[m] < target:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res
'''
# time complexity : O(nlogn)
# space complexity : O(n)
