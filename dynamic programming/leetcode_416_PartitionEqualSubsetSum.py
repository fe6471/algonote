# Partition Equal Subset Sum [Medium]
# https://leetcode.com/problems/partition-equal-subset-sum/

# Solution1
# [idea]
# While going through from start to end, add a new number to previous sub sums and store it.
# Check if any sub sum eqauls to the half of total sum.

# [code]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        sub_sum = {0}

        for num in nums:
            tmp_sum = set()
            for _sum in sub_sum:
                if _sum + num == target:
                    return True
                else:
                    tmp_sum.add(_sum + num)

            sub_sum.update(tmp_sum)

        return False
      
# time complexity : O(n*sum)
# space complexity : O(sum)
