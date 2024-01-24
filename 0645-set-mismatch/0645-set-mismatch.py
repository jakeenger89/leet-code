class Solution:
    def findErrorNums(self, nums):
        duplicate = -1
        missing = -1

        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1

        return [duplicate, missing]