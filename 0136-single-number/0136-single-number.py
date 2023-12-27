class Solution(object):
    def singleNumber(self, nums):
        counts = Counter(nums)
        
        for num, count in counts.items():
            if count == 1:
                return num
            
        return None