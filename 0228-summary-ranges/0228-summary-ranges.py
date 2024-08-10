class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        end=0
        res=[]
        i=0
        while i < len(nums):
            curr=i
            end=i+1
            while end < len(nums) and nums[end] == nums[end - 1]+1:
                end+=1
            
            if end - 1 > curr:
                curr_range=f"{nums[i]}->{nums[end - 1]}"
                res.append(curr_range)
            else:
                res.append(f"{nums[i]}")
            i=end
        return res