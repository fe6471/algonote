# Permutation in String [Medium]
# https://leetcode.com/problems/permutation-in-string/

# Solution1
# [idea]
# If each number of characters of string A is equal to string B's, A is permutation of B.

# [code]
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0]*26
        for ch in s1:
            l1[ord(ch) - ord('a')] += 1
        
        l2 = [0]*26
        for i in range(len(s2)):
            l2[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                l2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if l1 == l2:
                return True
            
        return False
        
# time complexity : O(n)
# space complexity : O(1)
