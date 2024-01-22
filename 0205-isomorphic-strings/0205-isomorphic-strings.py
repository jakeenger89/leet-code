class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        stoT = {}
        ttoS = {}
        
        for charS, charT in zip(s, t):
            if charS in stoT:
                if stoT[charS] != charT:
                    return False
            else:
                stoT[charS] = charT
                
            if charT in ttoS:
                if ttoS[charT] != charS:
                    return False
            else:
                ttoS[charT] = charS
            
        return True
        