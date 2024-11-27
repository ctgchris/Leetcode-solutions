class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #could compare the sorted of the two
        #iterate through and add to hashmap, if hashmap equal then return true

        if len(s) !=len(t):
            return False
        mapS=dict()
        mapT=dict()
        for i in range(len(s)):
            mapS[s[i]]=mapS.get(s[i], 0) + 1
            mapT[t[i]]=mapT.get(t[i], 0 )+ 1
        return mapS==mapT
