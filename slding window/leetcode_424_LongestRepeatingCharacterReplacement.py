# Longest Repeating Character Replacement [Medium]
# https://leetcode.com/problems/longest-repeating-character-replacement/

# Solution1
# [idea]
# length = number of most common character + k

# [code]
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        chars = {}
        max_repeat_ch_cnt = 0
        l, r = 0, 0

        while(r < len(s)):
            r_ch = s[r]

            chars[r_ch] = 1 + chars.get(r_ch, 0)

            max_repeat_ch_cnt = max(max_repeat_ch_cnt, chars[r_ch])
            current_length = r - l + 1

            if current_length - max_repeat_ch_cnt > k:
                l_ch = s[l]
                chars[l_ch] -= 1
                l += 1
                current_length -= 1

            max_length = max(max_length, current_length)
            r += 1

        return max_length
      
# time complexity : O(n)
# space complexity : O(n)
