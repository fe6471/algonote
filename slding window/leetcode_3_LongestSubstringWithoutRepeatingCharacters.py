# Longest Substring Without Repeating Characters [Medium]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Solution1
# [idea]
# If a character is not in substring, append it.
# Or slide the window of substring starting next to the character.

# [code]
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        substring = ''
        
        for ch in s:
            if ch not in substring:
                substring += ch
            else:
                substring = substring[substring.find(ch)+1:] + ch
            
            if len(substring) > answer:
                answer = len(substring)

        return answer
      
# time complexity : O(n^2)
# space complexity : O(n)

# Solution2
# [idea]
# While going through from start to end of given string, store characters and indices in hash map as key and value each.
# Keep a start pointer which is start point of substring.
# If a character is already in the hash map and its index is greater than start point, update the start pointer.

# [code]
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        chars = {}
        
        start = 0
        for i, ch in enumerate(s):
            if ch in chars and chars[ch] >= start:
                start = chars[ch] + 1
                
            length = i - start + 1
            max_length = max(max_length, length)
            chars[ch] = i
            
        return max_length
      

# time complexity : O(n)
# space complexity : O(n)
