class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i in range(len(points)):
            d = points[i][0]**2 + points[i][1]**2
            dist.append((d,i))
        dist.sort()
        result = []
        for i in range(k):
            index = dist[i][1]
            result.append(points[index])
        
        return result