class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # abc  cba
        l, r= 0, len(s)-1
        # 
        # while l<r
        #while l<r and s[l] not alnum, shirnk l
        #same for r
        # if s[l].lower != s[r].lower return false
        #shrink l and r
        # add return true

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True