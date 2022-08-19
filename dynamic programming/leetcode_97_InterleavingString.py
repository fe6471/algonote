# Interleaving String [Medium]
# https://leetcode.com/problems/interleaving-string/

# Solution1 - DFS
# [idea]
# Say i, j, k are indices of s1, s2, s3 each starting from 0.
# If s1[i] = s3[k], it is down to subproblem(s1[i+1:], s2[j:], s3[k+1:]).
# If s2[j] = s3[k], it is down to subproblem(s1[i:], s2[j+1:], s3[k+1:]).
# If s1[i] = s3[k] and s2[j] = s3[k], there are two branches subproblem(s1[i+1:], s2[j:], s3[k+1:]) and (s1[i:], s2[j+1:], s3[k+1:]).
# Travel all possible states (i,j,k) by using DFS and if i + j = len(s3), it means it reached the end and found interleaving.
# Note: since i + j = k, the state can be denoted as (i,j)

# [code]
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        next_node = [(0,0)]
        visited = set()

        while next_node:
            node = next_node.pop()
            i, j = node
            
            if node in visited:
                continue
            else:
                visited.add(node)

            if i + j == len(s3):
                return True

            if i == len(s1):
                if s2[j] == s3[i + j]:
                    next_node.append((i,j + 1))
            elif j == len(s2):
                if s1[i] == s3[i + j]:
                    next_node.append((i + 1,j))
            else:
                if s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                    next_node.append((i,j + 1))
                    next_node.append((i + 1,j))
                elif s1[i] == s3[i + j]:
                    next_node.append((i + 1,j))
                elif s2[j] == s3[i + j]:
                    next_node.append((i,j + 1))

        return False
      
# time complexity : O(nm)
# space complexity : O(nm)
