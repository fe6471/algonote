# Koko Eating Bananas [Medium]
# https://leetcode.com/problems/koko-eating-bananas/

# Solution 1
# [idea]
# Finding minimum k such that summation of ceil(pile/k) equals h or less.
# In brute force, k starts from 1 all the way to the max(piles).
# Apply binary search finding k within the range 1 to max(piles).

# [code]
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        low, high = 1, max(piles)
        while low < high:
            k = (low + high) // 2
            
            if sum([math.ceil(pile/k) for pile in piles]) <= h:
                high = k
            else:
                low = k + 1
            
        return low
        
# time complexity : O(nlogmax(piles))
# space complexity : O(1)
