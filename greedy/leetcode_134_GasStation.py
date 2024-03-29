# Gas Station [Medium]
# https://leetcode.com/problems/gas-station/

# Solution1
# [idea]
# gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Let's say it starts at i = 0 and tank[i] is sum of g[0] - c[0] to g[i] - c[i].
# Then tank[i] = [-2, -4, -6, -3, 0] in given example.
# If it starts at point x = 1, the graph can be moved like tank[i - x] = [-2, -4, -1, 2, 0].
# To complete the circuit, all tank[i - x] should be above or equal to zero.
# So that it should start at the next position where tank[i] is minimum.

# [code]
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        min_tank = 0
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < min_tank:
                min_tank = tank
                start = (i+1) % len(gas)
        
        if tank >= 0:
            return start
        else:
            return -1
           
# time complexity : O(n)
# space complexity : O(1)

# Solution2
# [idea]
# If sum of gas is less than sum of cost, there is no way to get through all positions.
# Otherwise there is one unique solution.
# If tank goes negative while it going from A to B, from any position between A and B cannot reach B. So we restart at the next position.

# [code]
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank, start = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            
            if tank < 0:
                tank = 0
                start = i + 1
                
        return start
'''
# time complexity : O(n)
# space complexity : O(1)
