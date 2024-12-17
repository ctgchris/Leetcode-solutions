class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #uses a monotonic decreasing stack. 
        res=[0] * len(temperatures)
        stack=[] #pair of [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append(i)
        
        return res
