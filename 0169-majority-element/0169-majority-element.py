from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        
        mostfrequent = counts.most_common(1)
        return mostfrequent[0][0]
        