# Number of Islands [Medium]
# https://leetcode.com/problems/number-of-islands/

# Solution1
# [idea]
# first trial, super slow, pretty bad...
# Create a graph by checking all possible edges(up, down, left, right) for each elements.
# Create disjoint sets by traveling nodes in graph.

# [code]
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0

        graph = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue

                node = (i, j)
                edges = []
                if i > 0 and grid[i - 1][j] == '1':
                    edges.append((i - 1, j))
                if i < m - 1 and grid[i + 1][j] == '1':
                    edges.append((i + 1, j))
                if j > 0 and grid[i][j - 1] == '1':
                    edges.append((i, j - 1))
                if j < n - 1 and grid[i][j + 1] == '1':
                    edges.append((i, j + 1))
                graph[node] = edges

        while graph:
            start_node = list(graph.keys())[0]
            to_visit = graph.pop(start_node)
            disjoint_set = {start_node}

            while to_visit:
                node = to_visit.pop()
                if node in disjoint_set:
                    continue

                disjoint_set.add(node)
                edges = graph.pop(node)
                to_visit = list(set(to_visit + [e for e in edges if e not in disjoint_set]))

            cnt += 1

        return cnt
'''
# time complexity : O(mn)
# space complexity : O(mn)

# Solution2
# [idea]
# Find an island while searching through each cell.
# Do bfs for all adjacent islands.
# Increase counter by 1.
# Skip if a cell is already visited.

# [code]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        visited = set()

        def bfs(i, j):
            visited.add((i, j))
            q = [(i, j)]
            while q:
                row, col = q.pop(0)
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(m) and
                        c in range(n) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    cnt += 1
                    bfs(i, j)

        return cnt
      
# time complexity : O(mn)
# space complexity : O(mn)
