# Counting Bits [Easy]
# https://leetcode.com/problems/counting-bits/

# Solution1
# [idea]
# For number x in binary representation, the number of 1's of 2x is same as x.
# Since doubling up in binary representation is just moving each digits up to next bit.

# [code]
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if i % 2 == 0:
                res[i] = res[i//2]
            else:
                res[i] = res[i//2] + 1
        
        return res
      
# time complexity : O(n)
# space complexity : O(n)
