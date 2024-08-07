class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        end=len(s)
        i=0
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < end:
            if s[i] == 'I':
                
                if i+1 < end and s[i+1] == 'V':
                    res+=4
                    i+=2
                    
                elif i+1 < end and s[i+1] == 'X':
                    res+=9
                    i+=2
                    
                else:
                    res+=1
                    i+=1
                    
            elif s[i] == 'X':
                
                if i+1 < end and s[i+1] == 'L':
                    res+=40
                    i+=2
                    
                elif i+1 < end and s[i+1] == 'C':
                    res+=90
                    i+=2
                else:
                    res+=10
                    i+=1
                        
            elif s[i] == 'C':
                if i+1 < end and s[i+1] == 'D':
                    res+=400
                    i+=2
                elif i+1 < end and s[i+1] == 'M':
                    res+=900
                    i+=2
                else:
                    res+=100
                    i+=1
            else:
                res+=map[s[i]]
                i+=1
        return res  
            






