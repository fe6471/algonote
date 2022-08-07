# Valid Sudoku [Medium]
# https://leetcode.com/problems/valid-sudoku/

# Solution1
# [idea]
# Create hash maps for columns and boxes.
# While searching a row, if a number (i, j) is in current row[i] or column[j] or box[i//3][j//3], return False.

# [code]
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        columns = [set() for i in range(9)]
        boxes = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                else:
                    continue

                if num in row or num in columns[j] or num in boxes[i//3][j//3]:
                    return False
                else:
                    row.add(num)
                    columns[j].add(num)
                    boxes[i//3][j//3].add(num)
        
        return True
   
# time complexity : O(n)
# space complexity : O(n)
