class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x:x[1])
        arrow = 1
        end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0]>end:
                arrow+=1
                end = points[i][1]
        

        return arrow


        #     j=0
        #     while j<len(points):
        #         if (j != i) and (points[i][0]<points[j][1] and points[i][1]>=points[j][1]):
        #             cnt+=1
        #         j+=1
        # return cnt