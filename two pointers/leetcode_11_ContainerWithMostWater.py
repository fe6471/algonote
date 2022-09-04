# Container With Most Water [Medium]
# https://leetcode.com/problems/container-with-most-water/

# Solution1
# [idea]
# The amount of water contained between height[i] and height[j] is (j - i) * min(height[i], height[j]).
# To possibly increase the amount, move index of minimum height.

# [code]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        i, j = 0, len(height) - 1
        
        while(i < j):
            h = min(height[i], height[j])
            amount = h*(j-i)
            max_amount = max(max_amount, amount)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_amount
      
# time complexity : O(n)
# space complexity : O(1)
