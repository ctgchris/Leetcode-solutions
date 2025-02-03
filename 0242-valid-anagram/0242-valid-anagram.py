class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count_s={}
        for c in s:
            count_s[c]=count_s.get(c,0)+1
        
        for c in t:
            if c not in count_s or count_s[c]==0:
                return False
            else:
                count_s[c]-=1
        
        return all(count==0 for count in count_s.values())