class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #essentially the minimum moves is the max distance needed to take horizontally or vertically.

        x1, y1= points.pop()
        res=0
        while points:
            x2, y2=points.pop()
            res+=max(abs(x1-x2), abs(y1-y2))
            x1,y1=x2,y2

        return res