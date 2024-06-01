class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        sHash = {}
        
        for c in s:
            if c in sHash:
                sHash[c] +=1
            else:
                sHash[c]=1
                
        for c in t:
            if c in sHash:
                if sHash >0:
                    sHash[c]-=1
                else:
                    return False
            else:
                return False
            
        if all(value == 0 for value in sHash.values()):
            return True
        else:
            return False
            
            
        