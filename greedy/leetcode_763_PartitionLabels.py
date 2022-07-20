# Partition Labels [Medium]
# https://leetcode.com/problems/partition-labels/

# Solution1
# [idea]
# Find first character and its last position. -> one partition
# Check all characters' last positions in the partition.
# If it's greater than current last position, update it until it reaches end of the partition.
# Repeat above steps starts from next character of the partition.

# [code]
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        chars = {}
        
        for i, ch in enumerate(s):
            if ch not in chars:
                chars[ch] = {'first':i, 'last':i}
            else:
                chars[ch]['last'] = i
                
        l = 0
        while l < len(s):
            first = chars[s[l]]['first']
            r = chars[s[l]]['last']
            
            while l < r:
                l += 1
                if chars[s[l]]['last'] > r:
                    r = chars[s[l]]['last']
                    
            res.append(r - first + 1)
            l = r + 1
            
        return res
        
# time complexity : O(n)
# space complexity : O(n)
