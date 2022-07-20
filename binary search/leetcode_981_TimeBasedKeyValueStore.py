# Time Based Key-Value Store [Medium]
# https://leetcode.com/problems/time-based-key-value-store/

# Solution 1
# [idea]
# Do binary search. If there is no target, check last searched element and return element less than target.

# [code]
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        if timestamp < self.map[key][0][1]:
            return ""
        
        low, high = 0, len(self.map[key]) - 1
        while low <= high:
            mid = (low + high) // 2

            if timestamp < self.map[key][mid][1]:
                high = mid - 1
            elif timestamp > self.map[key][mid][1]:
                low = mid + 1
            else:
                return self.map[key][mid][0]
            
        if self.map[key][mid][1] < timestamp:
            return self.map[key][mid][0]
        else:
            return self.map[key][mid - 1][0]
            
# time complexity : O(logn)
# space complexity: O(n)
