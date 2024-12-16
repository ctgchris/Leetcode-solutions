class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        #the solution is to first add to set. then for each num in set check if the current element is a new potential start
        #this is done by checking if n-1 is not in set

        mySet=set(nums)
        longest=0

        for num in mySet:
            if num-1 not in mySet:
                current_num=num
                current_streak=1

                while current_num+1 in mySet:
                    current_num=current_num+1
                    current_streak+=1
                longest=max(current_streak, longest)
        return longest


