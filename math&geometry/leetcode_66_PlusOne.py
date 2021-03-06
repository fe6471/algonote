# Plus One [Easy]
# https://leetcode.com/problems/plus-one/

# Solution1
# [idea]
# Change the digits into strings, concatenate them, add 1 to it and change it back to digits and insert it into an array.

# [code]
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        
        n = ''
        for digit in digits:
            n += str(digit)
            
        n = str(int(n) + 1)
        for digit in n:
            res.append(int(digit))
        
        return res
        
# time complexity : O(n)
# space complexity : O(n)

# Solution2
# [idea]
# Add 1 to the last number of given array.
# If it exceeds 10, change it into remainder of it divided by 10 and add 1 to next digits.
# Check if next digit exceeds 10 and repeat the same process above.

# [code]
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                digits[i - 1] += 1
        
        if digits[0] >= 10:
            digits[0] = digits[0] % 10
            digits = [1] + digits
        
        return digits
        
# time complexity : O(n)
# space complexity : O(1)
