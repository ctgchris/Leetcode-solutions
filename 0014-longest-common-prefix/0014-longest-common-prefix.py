class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res=""

        short=min(strs, key=len)

        for i, n in enumerate(short): #0 f
            matchChar=True
            for word in strs:
                if n != word[i]:
                     matchChar=False
            if matchChar==False:
                return res
            else:
                res+=n
                continue
                    
        return res
