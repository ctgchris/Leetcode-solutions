class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # 2 pointer solution

        l=0
        string=str(x)
        r=len(string)-1
        while l<r:
            if string[l]!=string[r]:
                return False
            l+=1
            r-=1
        return True