# Generate Parentheses [Medium]
# https://leetcode.com/problems/generate-parentheses/

# Solution1
# [idea]
# Base case : n = 1, res = ['()']
# To generate n parentheses, put a complete parenthesis in any places between result of n - 1.
# _ ( _ ) _  possible places are notated as '_' in result of n = 1.

# [code]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = {'()'}
        
        for i in range(1,n):
            tmp = set()
            for r in res:
                for j in range(len(r)//2 + 1):
                    tmp.add(r[:j] + '()' + r[j:])
            res = tmp
        
        return list(res)
      
# time complexity : O(2^2n)
# space complexity : O(n)
