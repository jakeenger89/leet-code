class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expsum = n * (n+1) // 2
        actualsum = sum(nums)
        return expsum - actualsum