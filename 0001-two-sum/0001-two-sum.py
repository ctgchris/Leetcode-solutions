class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        #brute force check each pair (n^3)

        hash_map={}
        for ind, num in enumerate(nums):
            diff=target-num
            if diff in hash_map:
                return [hash_map[diff], ind]
            else:
                hash_map[num]=ind
        return []