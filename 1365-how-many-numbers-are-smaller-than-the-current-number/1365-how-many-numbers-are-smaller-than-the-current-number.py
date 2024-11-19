class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        #sort it first
        #8, 1, 2, 2, 3
        #1, 2, 2, 3, 8 temp sorted

        #4, 0, 1, 1, 3

        sort=sorted(nums)
        res=[]
        hashMap={}
        # {1:0, 2:1, 3:3, 8:4}
        for i, num in enumerate(sort):
            if num not in hashMap:
                hashMap[num]=i 

        for num in nums:
            res.append(hashMap[num])

        return res
