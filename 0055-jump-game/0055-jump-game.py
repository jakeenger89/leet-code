class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        maxjump = 0
        
        for i in range(len(nums)):
            if i > maxjump:
                return False
            maxjump = max(maxjump, i + nums[i])
            
        return True
        