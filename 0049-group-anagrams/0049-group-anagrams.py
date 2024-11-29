class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #get the ASCII values of each word and check if exists in hashmap, if yes append: key: ASCII, value: strings
        #after iteration, then get all hash.values and add to res

        mapS={}

        for s in strs:
            sorted_s=''.join(sorted(s))
            if sorted_s in mapS:
                mapS[sorted_s].append(s)
            else:
                mapS[sorted_s]=[s]

        return list(mapS.values())

