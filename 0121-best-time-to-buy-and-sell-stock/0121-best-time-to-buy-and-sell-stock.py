class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        end=1
        maxP=0

        while end < len(prices):
            if prices[start] < prices[end]:
                maxP=max(maxP, prices[end] - prices[start])
            else:
                start=end
                end=start+1
                continue
            end+=1
        
        return maxP
        



