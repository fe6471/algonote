# Word Search [Medium]
# https://leetcode.com/problems/word-search/

# Solution1
# [idea]
# Find starting points where board[i][j] = word[0].
# Travel 4 possible directions starting from each starting points by dfs.
# If the direction is out of bound or its character is not same as word[idx], terminate the loop.
# If it is a right direction, add the point to path and pass it to the next iteration.

# [code]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        starts = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append((i, j))

        def backtrack(position, path, idx):
            if idx == len(word):
                return True

            i, j = position
            if i + 1 < m and (i + 1, j) not in path and board[i + 1][j] == word[idx]:
                new_path = path.copy()
                new_path.add((i + 1, j))
                found = backtrack((i + 1, j), new_path, idx + 1)
                if found:
                    return True
            if i - 1 >= 0 and (i - 1, j) not in path and board[i - 1][j] == word[idx]:
                new_path = path.copy()
                new_path.add((i - 1, j))
                found = backtrack((i - 1, j), new_path, idx + 1)
                if found:
                    return True
            if j + 1 < n and (i, j + 1) not in path and board[i][j + 1] == word[idx]:
                new_path = path.copy()
                new_path.add((i, j + 1))
                found = backtrack((i, j + 1), new_path, idx + 1)
                if found:
                    return True
            if j - 1 >= 0 and (i, j - 1) not in path and board[i][j - 1] == word[idx]:
                new_path = path.copy()
                new_path.add((i, j - 1))
                found = backtrack((i, j - 1), new_path, idx + 1)
                if found:
                    return True
            if (not (i + 1 < m and (i + 1, j) not in path and board[i + 1][j] == word[idx]) and
               not (i - 1 >= 0 and (i - 1, j) not in path and board[i - 1][j] == word[idx]) and
               not (j + 1 < n and (i, j + 1) not in path and board[i][j + 1] == word[idx]) and
               not (j - 1 >= 0 and (i, j - 1) not in path and board[i][j - 1] == word[idx])):
                return

        while starts:
            start = starts.pop()
            path = {start}
            idx = 1
            found = backtrack(start, path, idx)
            if found:
                return True

        return False
      
# time complexity : O(m*n*4^len(word))
# space complexity : O(m*n*4^len(word))

# Solution2
# [idea]
# same idea, cleaner code.

# [code]
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in path or
                board[r][c] != word[i]):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False
'''
# time complexity : O(m*n*4^len(word))
# space complexity : O(m*n*4^len(word))
