# Rotate Image [Medium]
# https://leetcode.com/problems/rotate-image/

# Solution1
# [idea]
# Change the first row elements with first column elements while storing the row elements in temp array.
# While rotating clockwise the outer circle, store current element in the temp array and change it to first popped element of the array. (first in first out)
# Repeat above steps in next inner circle.

# [code]
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i, j, k = 0, 0, 0

        while n > 1:
            tmp = []
            while j < n - 1:
                tmp.append(matrix[i][j])
                matrix[i][j] = matrix[n - 1 - j + k][i]
                j += 1
            while i < n - 1:
                tmp.append(matrix[i][j])
                matrix[i][j] = tmp.pop(0)
                i += 1
            while j > k:
                tmp.append(matrix[i][j])
                matrix[i][j] = tmp.pop(0)
                j -= 1
            while i > k:
                tmp.append(matrix[i][j])
                matrix[i][j] = tmp.pop(0)
                i -= 1

            n -= 1
            i += 1
            j += 1
            k += 1
            
# time complexity : O(n^2)
# space complexity : O(n)

# Solution2
# [idea]
# Reverse the matrix up and down.
# Transpose the matrix.

# [code]
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
# time complexity : O(n^2)
# space complexity : O(1)
