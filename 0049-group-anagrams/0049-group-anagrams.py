from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return ""
        result = {}
        for i in strs:
            x="".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())