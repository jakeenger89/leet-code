class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return -1
        
        h, n = len(haystack), len(needle)
        
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1