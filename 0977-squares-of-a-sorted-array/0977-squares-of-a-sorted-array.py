class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[0]*len(nums)
        p1, p2 = 0, len(nums)-1
        insert=len(nums)-1
        while insert >= 0:
            if abs(nums[p2]) > abs(nums[p1]):

                output[insert]=nums[p2]*nums[p2]
                p2-=1
            else:
                output[insert]=nums[p1]*nums[p1]
                p1+=1
            insert-=1
        return output
