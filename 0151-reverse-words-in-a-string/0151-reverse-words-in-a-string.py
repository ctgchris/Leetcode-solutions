class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        arr=s.split()
        res=arr[::-1]
        return ' '.join(res)