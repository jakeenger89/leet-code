class Solution(object):
    def lengthOfLongestSubstring(self, s):
        check = ""
        result = 0
        longest = 0
        for letter in s:
            if letter not in check:
                result += 1
                longest = max(longest, result)
                check += letter
            elif letter in check:
                index = check.index(letter)
                check = check[index + 1:] + letter
                result = len(check)
        return longest
                
        