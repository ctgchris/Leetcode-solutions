class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) #to handle [-2, 0, -1] edge case
        currMin, currMax= 1, 1
        for n in nums:
            if n == 0:
                currMin, currMax= 1, 1
                continue
            tmp=n*currMax
            currMax=max(n*currMax, n*currMin, n) #having n removes the need for if statement above
            currMin=min(tmp, n*currMin, n)
            res=max(res, currMax)

        return res


