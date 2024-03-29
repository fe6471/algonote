# Valid Parenthesis String [Medium]
# https://leetcode.com/problems/valid-parenthesis-string/

# Solution1
# [idea]
# Count the number of left parenthesis and decrease it if it encounters right parenthesis.
# The number of left parenthesis shouldn't be negative while going through left to right.
# Since * can be (, ) and _ so come up with min left and max left.
# If it encounters *, increase max left by 1 considering it as ( and decrease min left by 1 considering it as ).
# If max left goes negative, it means there's no possible way to be valid.
# If min left goes negative, consider one of passed *s is not ) but _ so reset the min left to 0.

# [code]
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0, 0
        for ch in s:
            if ch == '(':
                min_left += 1
                max_left += 1
            elif ch == ')':
                min_left -= 1
                max_left -= 1
            else:
                max_left += 1
                min_left -= 1
            
            if max_left < 0:
                return False
            if min_left < 0:
                min_left = 0
        
        return min_left == 0
        
# time complexity : O(n)
# space complexity : O(1)

# Solution2
# [idea]
# First, count the number of left parenthesis treating * as ( while going through from left to right.
# Second, count the number of right parenthesis treating * as ) while going through from right to left.
# If the counters didn't go neagtive in both operations, return True

# [code]
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        for ch in s:
            if ch == '(' or ch == '*':
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        
        right = 0
        for ch in s[::-1]:
            if ch == ')' or ch == '*':
                right += 1
            else:
                right -= 1
            if right < 0:
                return False
            
        return True
'''
# time complexity : O(n)
# space complexity : O(1)
