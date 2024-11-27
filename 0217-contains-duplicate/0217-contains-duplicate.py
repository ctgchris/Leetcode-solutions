class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #want to use a set to store all unique values, while iterating if already in set return false
        mySet=set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        return False