# Search in Rotated Sorted Array [Medium]
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Solution 1
# [idea]
# Find k (index of minimum value) using binary search.
# Move elements in the array k times and then find target using binary search.

# [code]
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        # finding k
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            
            if low == mid or high == mid:
                break
            
            if nums[high] < nums[mid]:
                low = mid
            else:
                high = mid
                
        if nums[low] > nums[high]:
            k = high
        else:
            k = low

        # finding target
        n = nums[k:] + nums[:k]
        l, h = 0, len(n) - 1
        while l <= h:
            m = (l + h) // 2
            
            if n[m] < target:
                l = m + 1
            elif n[m] > target:
                h = m - 1
            else:
                return (m + k) % len(n)
        
        return -1
        
# time complexity = O(logn)
# space complexity = O(n)

# Solution 2
# [idea]
# Don't actually need to find k.
# Let's say target is 7 with given array n = [5,6,7,8,9,10,0,1,2,3,4].
# We don't have to search in [0,1,2,3,4], so we can adjust the array like this [5,6,7,8,9,10,inf,inf,inf,inf,inf].
# Or if target is 3 We don't have to search in [5,6,7,8,9,10], so we can adjust the array like this [-inf,-inf,-inf,-inf,-inf,-inf,0,1,2,3,4]
# Note! No need to change the actual array. Just adjust the range while doing binary search.

# [code]
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            
            if target < nums[0] < nums[mid]: # -inf
                low = mid + 1
            elif target >= nums[0] > nums[mid]: # inf
                high = mid
            elif nums[mid] < target :
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        
        return -1
        
# time complexity = O(logn)
# space complexity = O(1)
