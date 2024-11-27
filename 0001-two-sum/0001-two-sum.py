class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #calc difference then check hashmap. hashmap store the num and add to hashmap unless diff found

        mapS={}
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in mapS:
                return [i, mapS[diff]]
            mapS[n]=i