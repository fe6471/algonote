# Two Sum II - Input Array Is Sorted [Medium]
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Solution1
# [idea]
# Starts at idx1 = 0, idx2 = n - 1.
# If numbers[idx1] + numbers[idx2] < target, increase idx1.
# If numbers[idx1] + numbers[idx2] > target, decrease idx2.

# [code]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, len(numbers)-1
        
        while(numbers[idx1] + numbers[idx2] != target):
            if numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            elif numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1
        
        return [idx1 + 1, idx2 + 1]
        
# time complexity : O(n)
# space complexity : O(1)
