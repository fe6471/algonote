# Decode Ways [Medium]
# https://leetcode.com/problems/decode-ways/

# [idea]
# Base case 1: s[0] = 0, cannot decode
# Base case 2: s[0] = 1 and len(s) >= 2, decode single digit and double digits
# Base case 3: s[0] = 2 and len(s) >= 2 and s[1] <= 6, decode single digit and double digits
# Base case 4: s[0] = 2 and len(s) >= 2 and s[1] >= 7, decode single digit and double digits
# Base case 5: s[0] >= 3, decode single digit
# Declare two variables to store last two operations' results. (dp1, dp2)
# While going through from end to start,
# if case 1, current result = 0.
# If case 4, 5, current result = last operation's result.
# If case 2, 3, current result = sum of last two operation's result.

# [code]
class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp2 = 1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                res = 0
            else:
                res = dp1
            
            if (i + 1 < len(s) and
               ((s[i] == '1') or
               (s[i] == '2' and int(s[i + 1]) < 7))):
                res += dp2
            
            dp2 = dp1
            dp1 = res
        
        return dp1
      
# time complexity : O(n)
# space complexity : O(1)
