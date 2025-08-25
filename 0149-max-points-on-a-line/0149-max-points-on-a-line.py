class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getSlope(p1: List,p2: List)->float:
            return ((p2[1]-p1[1])/(p2[0]-p1[0]))
        res =1
        for i in range(len(points)):
            p1=points[i]
            cnt = defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = getSlope(p1, p2)
                cnt[slope]+=1
                res = max(res, cnt[slope]+1)

        return res


            






        #     if i == len(points)-1:
        #         inslope = getSlope(points[i], points[0])
        #     else:
        #         inslope = getSlope(points[i], points[i+1])
        #     while j<len(points):
        #         if j!=i:
        #             slope = getSlope(points[i], points[j])
        #             if slope == inslope:
        #                 pt+= 1
        #         else:
        #             continue
        #         j+=1

        #     maxpt=max(maxpt, pt)

        # return maxpt