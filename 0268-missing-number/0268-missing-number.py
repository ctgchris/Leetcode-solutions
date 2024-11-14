class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for k,v in enumerate(nums):
            if k != v:
                return k
            
            if v == len(nums)-1:
                return v+1