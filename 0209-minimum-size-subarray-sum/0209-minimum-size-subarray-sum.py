class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)+1
        start=end=0
        curr_sum=0
        for end in range(len(nums)):
            curr_sum+=nums[end]
            
            while curr_sum >= target:
                size=min(end-start+1, size)
                curr_sum-=nums[start]
                start+=1
            
        return size if size !=len(nums)+1 else 0
                
