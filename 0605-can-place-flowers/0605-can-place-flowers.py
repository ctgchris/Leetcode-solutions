class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #need to check n-1 and n+1 if its n, instantiate a left and right. however make left true if n=0 and right true
        # if n=len(n-1). if both left and right and n == 0. add a 1  to flowerbed positon and n-=1
        if n==0:
            return True 
        for i in range(len(flowerbed)):
            left=(i==0) or (flowerbed[i-1] == 0)
            right=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)

            if left and right and flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return Falsde