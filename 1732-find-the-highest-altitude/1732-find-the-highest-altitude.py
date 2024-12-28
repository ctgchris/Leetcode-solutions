class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        #iterate through gain, keep track of current alt, add gain[i] to curr and 
        #check if need to update max alt
       
        maxAlt=currAlt=0
        for change in gain:
            currAlt+=change
            maxAlt=max(currAlt, maxAlt)

        return maxAlt