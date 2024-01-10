class Solution(object):
    def isPalindrome(self, s):
        #we want to make a copy of the word w/o special chars
        word = ""
        for letter in s:
            #check if letters are letters before adding to word
            if letter.isalnum():
                #set to lower so letters are consistantly the same
                word += letter.lower()
                #if they are the same this will return true
        return word == "".join(reversed(word))