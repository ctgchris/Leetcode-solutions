class Solution:
    def isPalindrome(self, s: str) -> bool:
        #steps
        #l and r pointer (l < r)
        #check if l =r then continue
        new=""
        for a in s:
            if a.isalpha() or a.isdigit():
                new+= a.lower()
        return new == new[::-1]