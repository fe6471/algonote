# Climbing Stairs [Easy]
# https://leetcode.com/problems/climbing-stairs/

# Solution1
# [idea]
# If k is the number of 2 steps, it is choosing k places from (n - k) possible candidates.
# Which equals to combination(n - k, k).
# All possible k is from 0 to n//2.

# [code]
class Solution:
    def climbStairs(self, n: int) -> int:
        from math import comb
        
        cnt = 0
        for k in range(n//2 + 1):
            cnt += comb(n-k, k) 
            
        return cnt
      
# time complexity : O(n)
# space complexity : O(1)

# Solution2
# [idea]
# Fibonacci
# The number of ways to get to n is way[n] = way[n - 1] + way[n - 2].
# Because [n - 1] is one step away from [n] and [n - 2] is two steps away from [n].
# The solution covers all possible cases on how the final step is taken.
# It is not redundant since the final steps are different.

# [code]
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        cnt = 0
        n1 = 2
        n2 = 1
        for _ in range(2, n):
            cnt = n1 + n2
            n2 = n1
            n1 = cnt
            
        return cnt
'''
# time complexity : O(n)
# space complexity : O(1)
