class Solution(object):
    def isAcronym(self, words, s):
        #get a list of the letters index 0 from the words
        letters = [word[0].lower() for word in words if word.isalpha()]
        #if the string of letters from words equal our acronym return true
        if ''.join(letters) == s:
            return True
        else:
            return False