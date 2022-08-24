# Combination Sum [Medium]
# https://leetcode.com/problems/combination-sum/

# Solution1 - DP
# [idea]
# To make combinations[i], add num to all combinations in combinations[i - num].

# [code]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        import bisect
        
        combinations = [[] for _ in range(target + 1)]

        for num in candidates:
            if num <= target:
                combinations[num].append([num])

        for i in range(1, target + 1):
            for num in candidates:
                if i >= num and combinations[i - num]:
                    for comb in combinations[i - num]:
                        idx = bisect.bisect(comb, num)
                        new_comb = comb[:idx] + [num] + comb[idx:]
                        if new_comb not in combinations[i]:
                            combinations[i].append(new_comb)

        return combinations[-1]
      
# time complexity : O(?)
# space complexity : O(?)

# Solution2 - DP (faster)
# [idea]
# Same idea as Solution1 but don't need to sort the new combs.

# [code]
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = [[] for _ in range(target + 1)]

        for num in candidates:
            for i in range(num, target + 1):
                if i == num:
                    combinations[i].append([num])
                for comb in combinations[i - num]:
                    combinations[i].append(comb + [num])

        return combinations[-1]
'''
# time complexity : O(?)
# space complexity : O(?)
