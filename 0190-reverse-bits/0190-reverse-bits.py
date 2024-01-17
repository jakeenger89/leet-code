class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #formate to a string
        binary_string = format(n, '032b')
        #reverse teh string
        reverseN = binary_string[::-1]
        #convert string into its unsigned Int
        unsignedInt = int(reverseN, 2)
        
        return unsignedInt