# Spiral Matrix [Medium]
# https://leetcode.com/problems/spiral-matrix/

# Solution1
# [idea]
# Append top row elements from left to right.
# Append right column elements from top to bottom.
# Append bottom row elements from right to left.
# Append left column elements from bottom to top.
# Increase top and left, decrease bottom and right by 1.
# Repeat above steps until top equals bottom or left equals right.
# If the number of rows or columns is odd, there will be remaining matrix (either mx1 or 1xn).
# Append remaining elements through linear scan.

# [code]
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elements = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while (top < bottom) and (left < right):
            for j in range(left, right):
                elements.append(matrix[top][j])

            for i in range(top, bottom):
                elements.append(matrix[i][right])

            for j in range(right, left, -1):
                elements.append(matrix[bottom][j])

            for i in range(bottom, top, -1):
                elements.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if len(elements) < len(matrix) * len(matrix[0]):
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    elements.append(matrix[i][j])
        return elements

# time complexity : O(mn)
# space complexity : O(mn)

# Solution2
# [idea]
# Pop the first row of matrix.
# Rotate the remaining matrix anticlockwise.
# Repeat until the matrix is empty.

# [code]
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elements = []
        while matrix:
            elements += matrix.pop(0)
            
            matrix = list(zip(*matrix))[::-1]
        
        return elements
        
# time complexity : O(mn)
# space complexity : O(mn)
