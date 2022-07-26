# Min Stack [Medium]
# https://leetcode.com/problems/min-stack/

# Solution1
# [idea]
# Update and store minimum value whenever push or pop.

# [code]
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val,min(val, self.getMin())))
        else:
            self.stack.append((val,val))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# time complexity : O(1)
# space complexity : O(n)
