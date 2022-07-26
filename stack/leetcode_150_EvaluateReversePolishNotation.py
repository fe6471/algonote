# Evaluate Reverse Polish Notation [Medium]
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Solution1
# [idea]
# If a token is an operator, pop two values from stack, calculate the operation and put the result back in the stack.
# Otherwise just push into a stack.

# [code]
class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operator:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    stack.append(val1+val2)
                elif token == '-':
                    stack.append(val1-val2)
                elif token == '*':
                    stack.append(val1*val2)
                else:
                    stack.append(int(val1/val2))
            else:
                stack.append(int(token))
        
        return stack[0]
      
# time complexity : O(n)
# space complexity : O(n)
