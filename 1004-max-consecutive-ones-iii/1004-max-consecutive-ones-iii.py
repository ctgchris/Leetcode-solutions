class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start=0
        end=0
        max_ones=0

        while end < len(nums):
            if nums[end]==0:
                k-=1
            
            

            if k < 0:
                if nums[start]==0:
                    k+=1
                start+=1
            max_ones=max(max_ones, end-start+1)
            end+=1
        return max_ones