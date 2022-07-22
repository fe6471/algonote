# Detect Squares [Medium]
# https://leetcode.com/problems/detect-squares/

# Solution1
# [idea]
# Create two hash map X = {x: {y: cnt}}, Y = {y: {x: cnt}} where (x,y) = point.
# Let's say input point = (x1, y1).
# Find point1 that its y = y1 to make aligned square.
# Calculate distance = |x - x1| (skip if distance = 0).
# Find point2 that its x = x1 and is y = y1 + distance or y1 - distance.
# Find point3 = (x, y1 + distance) or (x, y1 - distance)
# Add cnt1 * cnt2 * cnt3 to total count. (cnt[i] = count of point[i])

# [code]
class DetectSquares:

    def __init__(self):
        self.X = {}
        self.Y = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        
        if x not in self.X:
            self.X[x] = {y: 1}
        else:
            self.X[x][y] = 1 + self.X[x].get(y, 0)
            
        if y not in self.Y:
            self.Y[y] = {x: 1}
        else:
            self.Y[y][x] = 1 + self.Y[y].get(x, 0)

    def count(self, point: List[int]) -> int:
        cnt = 0
        x1, y1 = point
        if x1 not in self.X or y1 not in self.Y:
            return cnt
        
        for x2, cnt1 in self.Y[y1].items():
            distance = abs(x2 - x1)
            if distance == 0:
                continue
            
            cnt2 = self.X[x1].get(y1 + distance, 0)
            if cnt2:
                cnt3 = self.X[x2].get(y1 + distance, 0)
                cnt += cnt1 * cnt2 * cnt3
            
            cnt2 = self.X[x1].get(y1 - distance, 0)
            if cnt2:
                cnt3 = self.X[x2].get(y1 - distance, 0)
                cnt += cnt1 * cnt2 * cnt3
        
        return cnt
      
# time complexity : O(n)
# space complexity : O(n)

# Solution2
# [idea]
# easy to understand but slow
# For given point = (x1, y1), find point = (x2, y2) that |x2 - x1| = |y2 - y1|.
# Find point1 = (x2, y1), point2 = (x1, y2).
# Add cnt1 * cnt2 to total count. (cnt[i] = count of point[i])

# [code]
# class DetectSquares:

#     def __init__(self):
#         self.point_cnt = {}
#         self.points = []

#     def add(self, point: List[int]) -> None:
#         self.point_cnt[tuple(point)] = 1 + self.point_cnt.get(tuple(point), 0)
#         self.points.append(point)

#     def count(self, point: List[int]) -> int:
#         cnt = 0
#         x1, y1 = point
        
#         for x2, y2 in self.points:
#             if (abs(x2 - x1) != abs(y2 - y1)) or x1 == x2 or y1 == y2:
#                 continue
            
#             cnt += self.point_cnt.get((x2, y1), 0 ) * self.point_cnt.get((x1, y2), 0)
        
#         return cnt

# time complexity : O(n)
# space complexity : O(n)

# Solution3
# [idea]
# same idea as Solution1 using defaultdict, counter.

# # [code]
# from collections import defaultdict, Counter

# class DetectSquares:

#     def __init__(self):
#         self.x_cord = defaultdict(Counter)

#     def add(self, point: List[int]) -> None:
#         x, y = point
#         self.x_cord[x][y] += 1

#     def count(self, point: List[int]) -> int:
#         cnt = 0
#         x1, y1 = point
        
#         for y2 in self.x_cord[x1]:
#             d = abs(y1 - y2)
#             if d == 0:
#                 continue
            
#             cnt += self.x_cord[x1][y2] * self.x_cord[x1 + d][y1] * self.x_cord[x1 + d][y2]
#             cnt += self.x_cord[x1][y2] * self.x_cord[x1 - d][y1] * self.x_cord[x1 - d][y2]
            
#         return cnt

# time complexity : O(n)
# space complexity : O(n)
