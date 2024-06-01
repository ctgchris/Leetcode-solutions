class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   

        
        myMap= {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in myMap:
                arr=[myMap[diff], i]
                return arr
            else:
                myMap[n]=i 
                