class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)
        for s in strs:
            key="".join(sorted(list(s)))
            hash[key].append(s)

        return [l for l in hash.values()]