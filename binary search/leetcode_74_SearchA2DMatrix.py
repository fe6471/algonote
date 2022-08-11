# Search a 2D matrix [Medium]
# https://leetcode.com/problems/search-a-2d-matrix/

# Solution 1
# [idea]
# Find a row containing target (binary search) and then find the target inside the row (binary search).

# [code]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high, mid = 0, len(matrix) - 1, 0
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                break

        if not low <= high:
            return False
        row = matrix[(low+high)//2]
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left+right)//2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# time complexity : O(logmn)
# space complexity : O(1)

# Solution 2
# [idea]
# Flatten a two dimensional matrix into a one dimensional matrix. ex) [[1,2,3,4], [5,6,7,8], [9,10,11,12]] -> [1,2,3,4,5,6,7,8,9,10,11,12]
# ith element of second matrix is same as i//m row, i%m column of the first matrix where m is the number of its columns.

# [code]
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        low, high = 0, m*n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid//m][mid%m] > target:
                high = mid - 1
            elif matrix[mid//m][mid%m] < target:
                low = mid + 1
            else:
                return True
        
        return False
'''
# time complexity : O(logmn)
# space complexity : O(1)
