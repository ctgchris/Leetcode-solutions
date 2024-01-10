class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        maxn = i = j = 0
        for i in range(1, len(s)+1):
            count[s[i-1]] += 1
            maxn = max(maxn, count[s[i-1]])
            if i - j - maxn > k:
                count[s[j]] -= 1
                j += 1
        return i-j
            