class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        #sort each word, then check if sorted word is in dict, if so append word to the sorted word key 
        dic=defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))].append(word)
        return dic.values()