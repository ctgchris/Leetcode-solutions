class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #hash solution with key as value, value as index
        #return array but increase the index by 1 for each
        i =0
        j = len(numbers)-1
        
        while numbers[i]+numbers[j]!=target:
            s=numbers[i]+numbers[j]
            if s > target:
                j-=1
            else:
                i+=1
        return [i+1,j+1]