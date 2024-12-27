class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #2 sets
        ans=[[] for i in range(2)]
        set1=set(nums1)
        set2=set(nums2)

        for num in set1:
            if num not in set2:
                ans[0].append(num)
        for num in set2:
            if num not in set1:
                ans[1].append(num)
        return ans
