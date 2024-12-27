class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #2 sets
        set1=set(nums1)
        set2=set(nums2)
        ans1=[]
        for num in set1:
            if num not in set2:
                ans1.append(num)
            else:
                set2.remove(num)
        return [ans1, list(set2)]
