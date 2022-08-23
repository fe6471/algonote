# Reverse Integer [Medium]
# https://leetcode.com/problems/reverse-integer/

# Solution1
# [idea]
# Access digit by digit starting from right end by using modulo operator.

# [code]
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x:
            digit = x % 10
            res = res * 10 + digit
            x //= 10

        res *= sign
        if res > 2**31 - 1 or res < -2**31:
            return 0
        else:
            return res
          
# time complexity : O(n)
# space complexity : O(1)
