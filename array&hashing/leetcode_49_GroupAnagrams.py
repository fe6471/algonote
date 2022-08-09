# Group Anagrams [Medium]
# https://leetcode.com/problems/group-anagrams/

# Solution1
# [idea]
# A same group of anagrams has same numbers of characters.

# [code]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st in anagrams:
                anagrams[sorted_st].append(st)
            else:
                anagrams[sorted_st] = [st]
                
        return anagrams.values()
        
# time complexity : O(nlogm)
# space complexity : O(n)
