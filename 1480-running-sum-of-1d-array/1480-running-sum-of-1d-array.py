class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #make a new res array. hold a value called sum. iterate through array, add curr to sum then add that sum to res.


        res=[]
        sums=0
        for n in nums:
            sums+=n
            res.append(sums)
        
        return res