class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        char_count={}
        for c in s:
            char_count[c]=char_count.get(c, 0) + 1
        
        for c in t:
            if c not in char_count or char_count[c]==0:
                return False
            
            else:
                char_count[c]-=1
        
        return all(count==0 for count in char_count.values())

