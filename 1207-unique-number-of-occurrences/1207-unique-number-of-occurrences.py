from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        counted = Counter(arr)
        occurance = set()
        
        for count in counted.values():
            if count in occurance:
                return False
            occurance.add(count)
        
        return True
        