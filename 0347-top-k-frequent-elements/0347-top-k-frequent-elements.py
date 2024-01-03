class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        
        for num in nums:
            c[num] = c.get(num, 0) + 1
        c=sorted(c, key=lambda x: c[x], reverse=True)
        return c[:k]