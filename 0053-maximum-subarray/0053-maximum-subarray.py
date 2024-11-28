class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxS=float('-inf')
        currentS=0

        for num in nums:
            currentS=currentS+num

            if currentS > maxS:
                maxS=currentS
            
            if currentS<0:
                currentS=0

        return maxS

