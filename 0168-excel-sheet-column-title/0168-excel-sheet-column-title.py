class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            columnNumber //=26
        return result