class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return None
        nonZeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonZeroIdx] = nums[nonZeroIdx], nums[i]
                nonZeroIdx += 1
        return nums