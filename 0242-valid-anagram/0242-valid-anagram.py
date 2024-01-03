class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #add to dict using s, then remove using t, check dict at end if empty or not
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]]= 1 + countS.get(s[i], 0)
            countT[t[i]]= 1 + countT.get(t[i], 0)

        return countS == countT