class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        maxArea = 0
        for i in range(n-2):
            
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]
                    area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
                    maxArea = max(area, maxArea)
            # maxArea = max(currMax, maxArea)
        return maxArea

        
        #logic is correct few issue
        # maxArea = 0
        # for i in range(len(points)-2):
        #     curMax=0
        #     j=i+1
        #     while j<(len(points)-1):
        #         x1,y1 = points[i]
        #         x2,y2 = points[j]
        #         x3,y3 = points[j+1]
        #         area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
        #         currMax = max(area, curMax)
        #         j+=1
        #     maxArea = max(currMax, maxArea)
        # return maxArea
