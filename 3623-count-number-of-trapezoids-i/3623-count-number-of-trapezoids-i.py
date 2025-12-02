class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        yMap = defaultdict(list)
        for x,y in points:
            yMap[y].append(x)
        
        segs = []
        for y in yMap:
            xs = yMap[y]
            m=len(xs)
            if m>=2:
                segs.append(m*(m-1)//2)
        
        if len(segs)<2:
            return 0
        
        segs.sort()
        res = 0
        total = sum(segs)%MOD
        prefix = 0
        for c in segs:
            res = (res+c*(total-c))%MOD
        
        res = res*pow(2,MOD-2,MOD)%MOD

        return res%MOD
        


        
        
        
        # def getSlope(x1,y1,x2,y2):
        #     if (x2-x1)!=0:
        #         return (y2-y1)/(x2-x1)
        #     else: return -1
        
        # combs = combinations(points, 2)
        # visited = set()
        # for (x1,y1), (x2, y2) in combs:
        #     s1 = getSlope(x1,y1,x2,y2)
        #     if s1==0 and ((x1,y1), (x2, y2)) not in visited:
        #         visited.add(((x1,y1), (x2, y2)))
        #     else:
        #         continue
        # res = len(list(combinations(visited, 2)))%MOD
        # return res
            

        