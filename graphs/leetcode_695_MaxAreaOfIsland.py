# Max Area of Island [Medium]
# https://leetcode.com/problems/max-area-of-island/

# Solution1
# [idea]
# Find an island while searching through each cell.
# Do bfs for all adjacent islands.
# Increase area counter by 1 for all adjacent islands.
# Skip if a cell is already visited.
# Update max area whenever a bfs is done.

# [code]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            area = 1
            q = [(r, c)]
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                r, c = q.pop(0)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(m) and
                        col in range(n) and
                        grid[row][col] == 1 and
                        (row, col) not in visited):
                        visited.add((row, col))
                        q.append((row, col))
                        area += 1
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    max_area = max(max_area, area)

        return max_area
      
# time complexity : O(mn)
# space complexity: O(mn)
