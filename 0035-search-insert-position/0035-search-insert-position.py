class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        #binary search
        #[1,3,5,6] target =2
        # l m   r

        l,r =0, len(nums)
        while l< r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m] > target:
                r=m
            else:
                return m
        return l
        

    