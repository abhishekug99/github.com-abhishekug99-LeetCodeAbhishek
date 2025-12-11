class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        #nlogn
        xGrp = defaultdict(list)
        yGrp = defaultdict(list)
        res = 0
        for x,y in buildings:
            xGrp[x].append(y)
            yGrp[y].append(x) 
        
        up, down, left, right={}, {}, {}, {}

        for x, ys in xGrp.items():
            ys.sort()
            for i,y in enumerate(ys):
                if i>0:
                    down[(x,y)]=True
                if i<len(ys)-1:
                    up[(x,y)] = True
        
        for y, xs in yGrp.items():
            xs.sort()
            for i,x in enumerate(xs):
                if i>0:
                    left[(x,y)]=True
                if i<len(xs)-1:
                    right[(x,y)] = True
        for x, y in buildings:
            if (x,y) in up and (x,y) in down and (x,y) in left and (x,y) in right:
                res+=1

        return res
    
        
        
        # Correct code but TLE, all edge cases passes O(n^2)
        surrounding = set()
        res=0
        for i in range(len(buildings)):
            l,r,t,b=False, False, False, False
            for j in range(len(buildings)):
                if i!=j:
                    if buildings[i][0] == buildings[j][0] and buildings[i][1]>buildings[j][1] and b==False:
                        surrounding.add((buildings[j][0],buildings[j][1]))
                        b=True
                    if  buildings[i][0] == buildings[j][0] and buildings[i][1]<buildings[j][1] and t == False: 
                        surrounding.add((buildings[j][0],buildings[j][1]))
                        t=True
                    if buildings[i][1] == buildings[j][1] and buildings[i][0]>buildings[j][0] and l == False:
                        surrounding.add((buildings[j][0],buildings[j][1]))
                        l=True
                    if buildings[i][1] == buildings[j][1] and buildings[i][0]<buildings[j][0] and r == False:
                        surrounding.add((buildings[j][0],buildings[j][1]))
                        r=True 
            # print(surrounding)
            if len(surrounding)>=4:
                res+=1
            surrounding.clear()
        return res
            

