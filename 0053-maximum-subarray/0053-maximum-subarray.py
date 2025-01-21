class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum=nums[0]
        currSum=0

        for num in nums:
            currSum=max(currSum+num, num)
            maxSum=max(currSum, maxSum)
        return maxSum