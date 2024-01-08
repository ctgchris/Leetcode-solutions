class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # loop through 
        # if same length, 1 longer, 2 longer 
        # 
        size=0
        res = ""
        if (len(word1) > len(word2)):
            size=len(word2)
        else:
            size=len(word1)
        for i in range(size):
      
                res += word1[i]
          
                res += word2[i]
        
        if  ((size==len(word1)) and (len(res) != (len(word1) + len(word2)))):
            for j in range(size, len(word2)):
                 res += word2[j]
        elif ((size==len(word2)) and (len(res) != (len(word1) + len(word2)))):
            for j in range(size, len(word1)):
                res += word1[j]

        return res

