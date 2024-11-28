class Solution:
    def romanToInt(self, s: str) -> int:
        
        #iterate through and if encounter a I,X,C check next index if its a respective instance
        #then subtract 1st number from 2nd number. move index 2 spaces if case is hit.

        res=0
        mapS={'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500,'M':1000}
        i=0
        while i<len(s):
            if i<len(s)-1:

                if s[i] not in ['I', 'X', 'C']:
                    res+=mapS[s[i]]
                    i+=1
                else:
                    
                    if s[i] == 'I':    
                        if s[i+1] in ['V', 'X']:
                            res+=mapS[s[i+1]]-mapS[s[i]]
                            i+=2
                        else:
                            res+=mapS[s[i]]
                            i+=1

                    elif s[i] == 'X':
                        if s[i+1] in ['L', 'C']:
                            res+=mapS[s[i+1]]-mapS[s[i]]
                            i+=2
                        else:
                            res+=mapS[s[i]]
                            i+=1

                    
                    else:
                        if s[i+1] in ['D', 'M']:
                            res+=mapS[s[i+1]]-mapS[s[i]]
                            i+=2
                        else:
                            res+=mapS[s[i]]
                            i+=1
            else:
                res+=mapS[s[i]]
                i+=1
        return res