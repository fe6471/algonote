# Merge Triplets to Form Target Triplet [Medium]
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# Solution1
# [idea]
# If any value of a triplet is greater than each corresponding values of target, it has no use, so skip it.
# And then check if remaining triplets contain target values.

# [code]
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        X, Y, Z = False, False, False

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0]:
                X = True
            if y == target[1]:
                Y = True
            if z == target[2]:
                Z = True

        if not X or not Y or not Z:
            return False
        else:
            return True
            
# time complexity : O(n)
# space complexity : O(1)
