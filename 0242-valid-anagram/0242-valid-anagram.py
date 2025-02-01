class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counts=Counter(s)

        for c in t:
            if c not in s_counts:
                return False
            s_counts[c]-=1
            if s_counts[c]==0:
                del s_counts[c]

        return len(s_counts)==0
