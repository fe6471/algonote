# Letter Combinations of a Phone Number [Medium]
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Solution1
# [idea]
# Add all possible letters of a corresponding digit to path recursively.

# [code]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letter = {'2': ['a','b','c'],
                           '3': ['d','e','f'],
                           '4': ['g','h','i'],
                           '5': ['j','k','l'],
                           '6': ['m','n','o'],
                           '7': ['p','q','r','s'],
                           '8': ['t','u','v'],
                           '9': ['w','x','y','z']}

        letter_combinations = []

        def backtrack(path, i):
            if i == len(digits):
                letter_combinations.append(path)
                return

            digit = digits[i]
            letters = digit_to_letter[digit]
            for letter in letters:
                path += letter
                backtrack(path, i + 1)
                path = path[:-1]

        backtrack('', 0)

        return letter_combinations
      
# time complexity : O(4^n)
# space complexity : O(4^n)
