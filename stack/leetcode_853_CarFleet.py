# Car Fleet [Medium]
# https://leetcode.com/problems/car-fleet/

# Solution1
# [idea]
# Sort the given arrays by position reversed.
# The arrival time of a car is (target - position) / speed.
# If a car's arrival time is less than the one's ahead of it, they become a same fleet eventually.
# If a car's arrival time is greater than the one's behind of it, they never meet each other.

# [code]
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        arrival_time = float('-inf')
        for p, s in sorted(zip(position, speed), reverse=True):
            at = ((target-p)/s)
            if at > arrival_time:
                fleets += 1
                arrival_time = at
            
        return fleets
      
# time complexity : O(nlogn)
# space complexity : O(1)
