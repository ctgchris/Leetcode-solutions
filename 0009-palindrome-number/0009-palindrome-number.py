class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # 2 pointer solution
        if x<0:
            return False

        temp=x
        reverse=0

        while temp!=0:
            digit=temp%10
            reverse=reverse*10+digit
            temp=temp//10
        return reverse==x

        