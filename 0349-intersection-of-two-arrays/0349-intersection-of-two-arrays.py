class Solution(object):
    def intersection(self, nums1, nums2):
        one = set(nums1)
        two = set(nums2)
        intercept = one & two
        return list(intercept)
            
        