class Solution(object):
    def findWinners(self, matches):
        loserCount = {}
        for winner, loser in matches:
            loserCount[loser] = loserCount.get(loser, 0) + 1
            
        winners = [winner for winner, _ in matches]
        uniqueWinners = set(winners)
        lostNone = []
        
        for player in uniqueWinners:
            if player not in loserCount:
                lostNone.append(player)
        
        LostOne = []
        
        for player, losses in loserCount.items():
            if losses == 1:
                LostOne.append(player)
                
        lostNone.sort()
        LostOne.sort()
        
        return [lostNone, LostOne]