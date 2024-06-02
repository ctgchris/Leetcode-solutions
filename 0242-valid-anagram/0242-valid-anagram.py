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
        tHash= {}
        for i in range(len(s)):
            sHash[s[i]]= 1 + sHash.get(s[i], 1)
            tHash[t[i]]= 1 + tHash.get(t[i], 1)
            
        return sHash==tHash

            
            
        