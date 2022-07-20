# Multiply Strings [Medium]
# https://leetcode.com/problems/multiply-strings/

# Solution1
# [idea]
# If reverse given num1 and num2, each indices represent their place values.
# So result of multiplying reversed num1[i], num2[j] can be stored in res[i + j]
# If the digit exceeds 10, res[i + j], res[i + j + 1] take remainder and quotinent dividend by 10 each.

# [code]
class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0]*(len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                x = ord(num1[-(i + 1)]) - ord('0')
                y = ord(num2[-(j + 1)]) - ord('0')
                res[-(i + j + 1)] += x*y
                res[-(i + j + 2)] += res[-(i + j + 1)] // 10
                res[-(i + j + 1)] = res[-(i + j + 1)] % 10
        
        z = 0
        for i, num in enumerate(res):
            if num != 0:
                z = i
                break
                
        return ''.join(map(str, res[z:]))
      
# time complexity : O(nm)
# space complexity : O(n + m)
