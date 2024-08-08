class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP=0
        minP=float('inf')
        for price in prices:
            if price < minP:
                minP=price
            
            profit=price-minP

            if profit > maxP:
                maxP=profit
        return maxP

        



