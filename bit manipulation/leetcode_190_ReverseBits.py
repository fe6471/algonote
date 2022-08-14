# Reverse Bits [Easy]
# https://leetcode.com/problems/reverse-bits/

# Solution1
# [idea]
# Access bit by bit.
# Say n = '000...1010'
# Step 1. Shift i bits to right.        i = 1, n = '000...0101'
# Step 2. & operation with 1.           bit = '000...0101' & '000...0001' = '000...0001' (only the last bit left)
# Step 3. Shift (31 - i) bit to left.   bit = '100...0000'
# Step 4. | operation with 0.           res = '100...0000' | '000...0000' = '100...0000'
# Repeat above steps 32 times from i = 0 to 31.

# [code]
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
      
# time complexity : O(1)
# space complexity : O(1)
