# Sum of Two Integers [Medium]
# https://leetcode.com/problems/sum-of-two-integers/

# Solution1
# [idea]
# Basic concept
# Let's think about adding up 1 digit binary numbers.
# 0 + 0 = 0, 1 + 0 = 1, 0 + 1 = 1, 1 + 1 = 10
# When there is only one 1, 1 is remained on the same place of value.
# When there are all zeroes or ones, 0 is remained on the same place of value.
# This can be done by XOR operation.
# But when operate 1 + 1, 1 should be carried up to the next digit.
# This can be done by AND operation + left shift operation.
# Repeat adding the result of XOR operation and Carry operation until carry becomes 0.

# Python specific
# In Java, integers have fixed lenght of 32 bits, so carry will eventually be moved out of boundary and go to 0.
# But in Python, it can get into infinite loop since Python allows unlimited legth of integers.
# So it is needed to manually bound the inegers with mask.
# mask = 0xFFFFFFFF and & operation will only keep the last 32 bits.
# Masking works fine when the inputs are only positive numbers.
# But if it is a negative number, masking will lose information.
# Let's say adding -9 and -11.
# The above process will produce 0xFFFFFFEC which is -20 in 32 bits integer.
# But Python believes this is a large positive integer 4294967276, because all the bits to the far left are 0.
# So 0xFFFFFFEC should be converted into 0x...FFFFFFFFFFFEC with infinite number of F to the far left.
# It can be done by fliping all bits except the last 32 bits which is same as ~x ^ mask.

# [code]
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        if (a>>31) & 1:
            a = ~(a ^ mask) 
        return a
      
# time complexity : O(1) (small fixed range)
# space complexity : O(1)
