class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        #two pointers sliding window
        #algo: keep track two variables have and need
        # have < need keep going
        #have and need are sets 
        # loop through t and put into set
        l= 0
        
        #gets the letter count of string t
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        have, need = 0, len(countT)
        res, resLen=[-1, -1], float('infinity')
        for r in range(len(s)):
            c=s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

                while have == need:
                    if (r - l + 1) < resLen:
                        res = [l, r]
                        resLen = (r - l + 1)
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ''
                                                
            
        #if not have all t, grow right
        #if has all t, shrink from left if possible
        # # of unique variables from t in current window
        # # of unique varaibles needed from t
        
        # while have != need
        # if r in range
        # add r to have hashmap
        # 
        # after while, if have == need:
        # incrementally shrink left
        # if shrink l 
        #