class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counts=Counter(s)

        for c in t:
            if s_counts[c] ==0 or c not in s_counts:
                return False
            s_counts[c]-=1

        return all(count==0 for count in s_counts.values())
