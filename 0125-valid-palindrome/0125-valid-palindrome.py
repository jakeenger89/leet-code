class Solution(object):
    def isPalindrome(self, s):
        #make lowercase 
        s = s.lower()
        #remove spaces 
        s = s.replace(" ", "")
        #remove all non chars
        s = ''.join(char for char in s if char.isalnum())
        
        if s == s[::-1]:
            return True
        else:
            False