class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #this solution creates two dictionarys, and makes characters the index and value the count. 
        #check if hashmaps equal to see if they are anagrams meaning they have same number of certaincharacters
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):

            countS[s[i]]= 1 + countS.get(s[i], 0)
            countT[t[i]]= 1 + countT.get(t[i], 0)

        return countS == countT