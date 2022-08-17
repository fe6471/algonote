# Palindromic Substrings [Medium]
# https://leetcode.com/problems/palindromic-substrings/

# Solution1
# [idea]
# If a substring is palindromic and its left char and right char are same, 'left char + substring + right char' is also palindromic.

# [code]
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            l, r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt
      
# time complexity : O(n^2)
# space complexity : O(1)
