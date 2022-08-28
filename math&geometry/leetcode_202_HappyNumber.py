# Happy Number [Easy]
# https://leetcode.com/problems/happy-number/

# Solution1
# [idea]
# A number either goes to 1 or infinite loop while going thorugh given process.
# If the number becomes one of the numbers already seen, it is going into infinite loop.

# [code]
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n > 1:
            tmp = 0
            while n:
                tmp += (n%10)**2
                n //= 10
            n = tmp
            if n in seen:
                return False
            else:
                seen.add(n)
        return True
        
# time complexity : O(logn)
# space complexity : O(logn)
