class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        end=len(s)
        i=0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < end:
            if i+1 < end and d[s[i+1]] > d[s[i]]:
                res+= d[s[i+1]] - d[s[i]]
                i+=2
            else:
                res+=d[s[i]]
                i+=1
        return res  
            






