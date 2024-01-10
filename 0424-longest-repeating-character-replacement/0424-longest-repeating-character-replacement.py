class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        i, j, ans = 0, 0, 0
        while j < len(s):
            h[s[j]] = h.get(s[j],0) + 1
            while j-i+1-max(h.values()) > k:
                h[s[i]] -= 1
                i += 1
            ans = max(ans,j-i+1)
            j += 1
        return ans
            