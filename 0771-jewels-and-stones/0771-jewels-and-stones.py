class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        result = 0
        for char in stones:
            if char in jewels:
                result += 1
        return result