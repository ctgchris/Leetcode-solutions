class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        #brute force check each pair (n^3)

        num_dict = {}  # Using a meaningful variable name
        for i, num in enumerate(nums):  # Using enumerate to get both value and index
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], i]  # Returning indices
            else:
                num_dict[num] = i  # Storing value-index pair in the dictionary
        return []  # If no solution is found, you can return an empty list or None
