class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums)-1
        while l <= r:
            middle= (l+r)//2
            #4 cases, 
            if nums[middle] < nums[0] and target >= nums[0]:
                #case where out of order and target in left sorted
                r=middle-1
            elif nums[middle] >= nums[0] and target < nums[0]:
                #case where out of order and target in right sorted
                l=middle+1
            elif target < nums[middle]:
                r=middle-1

            elif target > nums[middle]:
                l=middle+1
            else:
                return middle
            
        return -1
                
                