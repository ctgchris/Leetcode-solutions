class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        mapS=defaultdict(list)

        for s in strs:
            count=[0] * 26
            for char in s:
                count[ord(char)- ord('a')]+=1

            mapS[tuple(count)].append(s)

        return list(mapS.values())
