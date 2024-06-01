class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   

        
        myMap= {}
        
        for i in range(len(nums)):
            diff = target - nums[i] 
            if nums[i] in myMap:
                arr=[myMap[nums[i]], i]
                return arr
            else:
                myMap[diff]=i 
                