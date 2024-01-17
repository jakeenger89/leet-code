class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_string = format(n, '032b')
        reverseN = binary_string[::-1]
        unsignedInt = int(reverseN, 2)
        
        return unsignedInt