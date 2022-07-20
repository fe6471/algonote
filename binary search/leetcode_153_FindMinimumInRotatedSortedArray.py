# Find Minimum in Rotated Sorted Array [Medium]
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Solution 1
# [idea]
# Split the array into two blocks, compare each blocks' first or last elements, take smaller one's block and repeat.

# [code]
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]

# time complexity : O(logn)
# space complexity : O(1)

# Solution 2
# [idea]
# same idea, easier to understand

# [code]
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:  # The nums[mid] is the minimum number
                return nums[mid]
            if nums[mid] > nums[right]:  # search on the right side, because smaller elements are in the right side
                left = mid + 1
            else:
                right = mid - 1  # search the minimum in the left side
                
# time complexity : O(logn)
# space complexity : O(1)
