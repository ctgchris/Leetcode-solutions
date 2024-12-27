class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        #s a d
        #s a d

        start=2
        start_n=2
        for i in range(len(haystack)-len(needle)+1):
            start=i
            start_n=0
            
            while start_n < len(needle) and haystack[start] == needle[start_n]:    
                start+=1
                start_n+=1
            if start_n >= len(needle):
                    return i



        return -1

