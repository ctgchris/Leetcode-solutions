class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        hash=set(nums)

        for n in hash:
            if (n-1) not in hash:
                length=1
                while(n+length) in hash:
                    length+=1
                longest=max(longest, length)
        return longest
