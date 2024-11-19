class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashMap={}
        for i, num in enumerate(nums):
            diff=target-num

            if diff in dic:
                return [hashMap[diff], i]
            hashMap[num]=i
        