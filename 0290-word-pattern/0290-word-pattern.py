class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern) != len(words):
            return False
        d={}
        seen=set()
        for i, char in enumerate(pattern):
            #when new character
            if char not in d:
                if words[i] in seen:
                    return False
                seen.add(words[i])
                d[char]=words[i]
            #existing character
            else:
                #checking if repeats of words to characters
                if d[char] != words[i]:
                    return False
        
        return True
