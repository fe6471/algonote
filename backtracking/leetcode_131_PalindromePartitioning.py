# Palindrome Partitioning [Medium]
# https://leetcode.com/problems/palindrome-partitioning/

# Solution1
# [idea]
# Find all possible partitions and save palindrome ones only.

# [code]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []
    
        def backtrack(substring, i):
            if i == len(s):
                for string in substring:
                    if string != string[::-1]:
                        return
                substrings.append(substring)
                return

            backtrack(substring + [s[i]], i + 1)
            backtrack(substring[:-1] + [substring[-1] + s[i]], i + 1)

        backtrack([s[0]], 1)
        return substrings

# time complexity : O(n2^n)
# space complexity : O(n2^n)

# Solution2
# [idea]
# Find all possible partitions in prefix.
# If it is not palindrome, break.
# Repeat in suffix till it reaches the end.

# [code]
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []
    
        def backtrack(substring, i):
            if i == len(s):
                substrings.append(substring)
                return

            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    backtrack(substring + [s[i:j + 1]], j + 1)

        backtrack([], 0)
        return substrings
'''
# time complexity : O(n2^n)
# space complexity : O(n2^n)
