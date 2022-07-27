# Longest Palindromic Substring [Medium]
# https://leetcode.com/problems/longest-palindromic-substring/

# Solution1
# [idea]
# If a substring is palindromic and its left char and right char are same, 'left char + substring + right char' is also palindromic.

# [code]
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        
        for i in range(len(s)):
            # odd length
            substring = s[i]
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    substring = s[l] + substring + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            
            if len(substring) > len(longest):
                longest = substring
         
            # even length
            substring = ''
            l, r = i - 1, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    substring = s[l] + substring + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            
            if len(substring) > len(longest):
                longest = substring
                
        return longest
      
# time complexity : O(n^2)
# space complexity : O(n)
