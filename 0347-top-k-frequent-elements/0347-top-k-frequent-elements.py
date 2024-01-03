class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        
        # Count occurrences manually
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        c=sorted(c, key=lambda x: c[x], reverse=True)
        return c[:k]