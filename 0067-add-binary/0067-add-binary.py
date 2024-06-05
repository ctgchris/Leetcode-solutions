class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res=""
        carry= 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digA=int(a[i]) if i < len(a) else 0 #1
            digB=int(b[i]) if i < len(b) else 0#1

            total=digA + digB + carry
            char= str(total % 2)
            carry=total//2
            res=char + res
        
        if carry:
            res= "1" + res

        return res



        