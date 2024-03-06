class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        topNums = sorted(counts, key=lambda x: counts[x], reverse= True)
        return topNums[:k]