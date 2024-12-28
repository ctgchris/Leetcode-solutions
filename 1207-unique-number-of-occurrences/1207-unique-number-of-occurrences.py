class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #iterate through, mapping nums to frequencys, afterwrods add frequencies to a set,
        #when adding if a duplicate is found return false

        d={} 
        seen=set() 

        for num in arr:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for freq in d.values():
            if freq in seen:
                return False
            else:
                seen.add(freq)
        
        return True