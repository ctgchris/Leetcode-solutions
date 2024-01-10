class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL=0
        mySet=set()
        
        for i in range(len(s)):
            while(s[i] in mySet):
                mySet.remove(s[l])
                l+=1
            mySet.add(s[i])
            maxL=max(maxL, i-l + 1)
        return maxL
            
        