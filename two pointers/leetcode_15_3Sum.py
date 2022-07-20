# 3Sum [Medium]
# https://leetcode.com/problems/3sum/

# Solution1
# [idea]
# Sort given nums.
# Initiate indices i, j, k (i=0, k=n-1, j in range(1, n-2)).
# While j going through from 1 to n-2, if sum is greater than 0, decrease k or if less than, increase i until i = j or k = j.

# [code]
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
    
        nums.sort()

        for j in range(1, len(nums) - 1):
            i, k = 0, len(nums) - 1
            while(i < j < k):
                _sum = nums[i] + nums[j] + nums[k]

                if _sum == 0:
                    triplets.add((nums[i],nums[j],nums[k]))
                    if i < j:
                        i += 1
                    else:
                        k -= 1
                elif _sum > 0:
                    k -= 1
                elif _sum < 0:
                    i += 1
        
        result = [list(x) for x in triplets]
        
        return result
      
# time complexity : O(n^2)
# space complexity : O(combination(n,3))

# Solution2
# [idea]
# Same idea but skip some indices if a number equals to previous one to avoid duplicates.

# [code]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                
                if _sum < 0:
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                    
        return triplets
      
# time complexity : O(n^2)
# space complexity : O(combination(n,3))
