class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []
        for word in words:
            lowerword = word.lower()
            if lowerword[0] in row1:
                currentrow = row1
            elif lowerword[0] in row2:
                currentrow = row2
            else:
                currentrow = row3
            
            if all(letter in currentrow for letter in lowerword):
                result.append(word)
        return result