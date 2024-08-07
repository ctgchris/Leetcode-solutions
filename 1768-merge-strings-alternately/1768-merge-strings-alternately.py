class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Plan: 
        res=[]
        word1Len=len(word1)
        word2Len=len(word2)
        i=0
        while i < word1Len and i < word2Len:
            res.append(word1[i])
            res.append(word2[i]) 
            i+=1
        if word1Len > word2Len:
            res.append(word1[i:])
        elif word2Len > word1Len:
             res.append(word2[i:]) 
        
        return "".join(res)
        