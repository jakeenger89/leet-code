class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ''
        while word1 and word2:
            merged += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        merged += word1 + word2
        return merged