class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        l,r = 0, len(s)-1
        s=list(s)
        while l < r:
            if s[l] not in vowels:
                l+=1
            elif s[r] not in vowels:
                r-=1
            else:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1

        return ''.join(s)