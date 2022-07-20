# Top K Frequent Elements [Medium]
# https://leetcode.com/problems/top-k-frequent-elements/

# Solution1
# [idea]
# Calculate frequencies and sort.

# [code]
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequency = {}
        
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
            
        sorted_frequency = sorted(frequency.items(), key = lambda item : item[1], reverse=True)
        for i in range(k):
            res.append(sorted_frequency[i][0])
            
        return res
        
# time complexity : O(nlogn)
# space complexity : O(n)

# Solution2
# [idea]
# Similar idea, but don't need to sort the actual frequncy list of which time complexity is O(nlogn).
# Just make extra space to store number by frequency in corresponding index of the array while searching frequency list which takes O(n) time.

# [code]
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequency = {}
        
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
            
        sorted_frequency = [[] for i in range(len(nums) + 1)]
        for num, freq in frequency.items():
            sorted_frequency[freq].append(num)
        
        for n in sorted_frequency[::-1]:
            res += n
            if len(res) == k:
                return res
                
# time complexity : O(n)
# space complexity : O(n)
