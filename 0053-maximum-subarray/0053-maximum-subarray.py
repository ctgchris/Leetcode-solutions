class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #if prefixsum is negative skip over it
        #two pointer
        currSum=0
        maxS=nums[0]
        for i in range(len(nums)):
            if (currSum) < 0:
                currSum=0
            
            currSum+=nums[i]
            maxS=max(currSum, maxS)
        #works for negative numbers array because maxS starts as first index then consistantly compares maxS with following negative numbers (currSum since 0+negative number)
            
        return maxS