# Set Matrix Zeroes [Medium]
# https://leetcode.com/problems/set-matrix-zeroes/

# Solution1 - brute force
# [idea]
# Copy the given matrix.
# If matrix[i][j] is 0, change the every elements of i th row and j th colum of copied matrix into 0.

# time complexity : O(mn)
# space complexity : O(mn)

# Solution2 - more optimized O(m+n) space
# [idea]
# Store rows and columns indices of zero elements.
# Change the elements of stored rows and columns into 0.

# [code]
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        columns = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for row in rows:
            matrix[row] = [0]*len(matrix[0])

        for column in columns:
            for i in range(len(matrix)):
                matrix[i][column] = 0
                
# time complexity : O(mn)
# space complexity : O(m + n)

# Solution3 - most optimized O(1) space
# [idea]
# Store flags in the first row and column of the matrix itself.
# Since matrix[0][0] is overlapped when storing first row's and column's flag, need extra space of O(1).

# [code]
class Solution3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        first_row_zero = False
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first_row_zero = True
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                matrix[i] = [0]*columns
        
        for j in range(columns):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        
        if first_row_zero:
            matrix[0] = [0]*columns
            
# time complexity : O(mn)
# space complexity : O(1)
