class Solution(object):
    def sortPeople(self, names, heights):
        ziplist = list(zip(names, heights))
        ziplist.sort(key=lambda x: x[1], reverse=True)
        sortedN = [name for name, height in ziplist]
        return sortedN
            