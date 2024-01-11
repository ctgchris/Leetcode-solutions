class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums)-1
        res=nums[0]
        
        while l<=r:
            if nums[l] < nums[r]:
                return min(nums[l], res)
            middle=(l+r)//2
            res = min(res, nums[middle])

            
            if nums[middle] >= nums[l]:
            # We are in the left sorted portion, move right
                l = middle + 1
            else:
            # We are in the right sorted portion, move left
                r = middle - 1
        return res
                