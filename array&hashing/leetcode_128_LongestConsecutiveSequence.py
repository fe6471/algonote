# Longest Consecutive Sequence [medium]
# https://leetcode.com/problems/longest-consecutive-sequence/

# Solution1
# [idea]
# If a (num - 1) not in the array, the num is a start point of one consecutive sequence.
# Find the longest sequence starts at every starting points.

# [code]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = []
        
        for num in nums:
            if num - 1 not in nums:
                starts.append(num)
        
        longest = 0
        for num in starts:
            length = 1
            n = num + 1
            
            while(n in nums):
                length += 1
                n += 1
            
            if length > longest:
                longest = length
        
        return longest
        
# time complexity : O(n)
# space complexity : O(n)
