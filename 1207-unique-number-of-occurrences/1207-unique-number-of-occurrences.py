from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        #create a counter for how many times the number shows up
        counted = Counter(arr)
        occurance = set()
        #now for loop over the counted num values, if any are duplicates return false otherwise add them to
        #occurance to check for duplcates
        for count in counted.values():
            if count in occurance:
                return False
            occurance.add(count)
        
        return True
        