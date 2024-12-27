class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d={}
        seen=set()
        # {b-b, a-a, c-a}
        for i, char in enumerate(s):
            if char not in d:
                if t[i] in seen:
                    return False
                d[char]=t[i]
                seen.add(t[i])

            else:
                if d[char] != t[i]:
                    return False
        return True