class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        Letters = ''
        maxlength = 0
        start = 0
        
        for end, letter in enumerate(s):
            if letter in Letters[start:end]:
                start = start + Letters[start:end].index(letter) + 1
            Letters += letter
            maxlength = max(maxlength, end - start + 1)
       
        return maxlength