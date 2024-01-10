class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count=[0] * 26
        res=0
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('A')]+=1
            while (i - l + 1) - max(count) > k:
                count[ord(s[l]) - ord('A')]-=1
                l+=1
            res=max(res, i - l + 1)
        return res
            