# Pow(x, n) [Medium]
# https://leetcode.com/problems/powx-n/

# Solution1
# [idea]
# Binary Exponentiation

# [code]
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        p = 1
        while n:
            if n % 2:
                p *= x
                n -= 1
                
            x *= x
            n //= 2
        
        return p
      
# time complexity : O(logn)
# space complexity : O(1)
