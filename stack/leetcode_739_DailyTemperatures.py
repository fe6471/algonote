# Daily Temperatures [Medium]
# https://leetcode.com/problems/daily-temperatures/

# Solution1
# [idea]
# Store each indices in a stack while going through start to end.
# If current temperature is greater than temperature of top index of stack, backtrack the stack until it becomes bigger than current temperature.

# [code]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        
        for i, temperature in enumerate(temperatures):
            while(stack and temperatures[stack[-1]] < temperature):
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
                
        return answer
      
# time complexity : O(n)
# space complexity : O(n)
