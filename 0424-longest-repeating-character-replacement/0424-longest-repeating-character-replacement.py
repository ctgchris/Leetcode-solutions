class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxSlidingWindow = 0 
        
        # left pointer 
        l = 0 
        for r in range(len(s)): 
            # right pointer is moving forward
            
           
            
            # add 1 to the count of the character we are trying to add to the sliding window
            # i.e [ABC] A --> [ABCA]
            count[s[r]] = 1 + count.get(s[r],0)
            
            # is the sliding window invalid if we add the new character?
            if ( (r-l+ 1) - max( count.values()) ) > k:
                
                # if it is reduce the frequency of the character from the count 
                count[s[l]] -= 1
                
                # and we move the window from the left and
                l += 1
                 
            # update the max of the sliding window
            maxSlidingWindow = max(maxSlidingWindow,(r - l + 1))
            
        return maxSlidingWindow
            