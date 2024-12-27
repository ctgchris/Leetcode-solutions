class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d={}
        # {b-b, a-a, c-a}
        for i, n in enumerate(s):
            if n in d and d[n] != t[i]:
                return False
            if n not in d and t[i] in d.values():
                return False
            d[n]=t[i]
        return True