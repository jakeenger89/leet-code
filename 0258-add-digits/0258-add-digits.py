class Solution(object):
    def addDigits(self, num):
        #the output will be less than 10 so we have a check for when to stop
        while num >= 10:
            #turn it into a string
            numstr = str(num)
            
            numsum = 0
            #now we can itterate through each char in the string (3 and 8)
            for char in numstr:
                #add them together
                numsum += int(char)
            #if this is 10 or greater we put it bcak in the while else return the num
            num = numsum
        return num