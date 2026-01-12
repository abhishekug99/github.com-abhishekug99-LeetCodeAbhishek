class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0 #time
        for i in range(1, len(points)):
            x1,y1 = points[i-1]
            x2,y2 = points[i]
            res+= max(abs(x2-x1), abs(y2-y1))
        return res
        
        