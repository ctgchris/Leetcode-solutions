class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search. 
        l=0
        r=len(nums)-1
        while l< r:
            mid=(l+r)//2
            if nums[mid] >= nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
        #case when mid > start, start=mid+1

        #case when mid < start, end=mid

    