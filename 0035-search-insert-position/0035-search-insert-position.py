class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        l=0
        r=len(nums)
        while l < r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            if target > nums[m]:
                l=m+1
            else:
                r=m
        return l
