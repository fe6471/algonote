# Hand of Straights [Medium]
# https://leetcode.com/problems/hand-of-straights/

# Solution1
# [idea]
# Find smallest number n.
# Remove n, n+1, n+2, ... , n+groupSize-1 from the array.
# Repeat until the array is empty.

# [code]
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        num_cnt = {}
        for n in hand:
            num_cnt[n] = 1 + num_cnt.get(n, 0)

        nums = list(num_cnt.keys())
        nums.sort()

        while nums:
            smallest = nums[0]
            k = 0

            while k < groupSize:
                n = smallest + k

                if n not in num_cnt:
                    return False
                else:
                    num_cnt[n] -= 1

                if num_cnt[n] == 0:
                    del num_cnt[n]
                    nums.remove(n)
                
                k += 1

        return True
        
# time complexity : O(nlogn)
# space complexity : O(n)
