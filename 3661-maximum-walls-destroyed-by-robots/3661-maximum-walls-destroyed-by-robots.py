class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robotsNDist = sorted(zip(robots, distance))
        walls.sort()
        n=len(robotsNDist)

        @cache
        def dfs(i, nxtDir):
            if i<0:
                return 0
            p,d = robotsNDist[i]
            
            leftend = p-d
            if i>0:
                leftend = max(leftend, robotsNDist[i-1][0]+1)
            l=bisect_left(walls, leftend)
            r=bisect_left(walls, p+1)
            ans = dfs(i-1,0) + (r-l)

            rightend = p+d
            if i+1<n:
                nextpos, nextdist = robotsNDist[i+1]
                if nxtDir ==0:
                    rightend = min(rightend, nextpos-nextdist-1)
                else:
                    rightend = min(rightend, nextpos-1)
            l=bisect_left(walls, p)
            r=bisect_left(walls, rightend+1)
            ans = max(ans, dfs(i-1,1) + (r-l))

            return ans
        
        return dfs(n-1,1)

        #works but not well
        # wallsHit = set()
        
        # for i in range(len(robots)):
        #     for r in range(robots[i], robots[i]+distance[i]+1):
        #         if r in robots and r!=robots[i]:
        #             break
        #         if r not in wallsHit and r in walls:
        #             wallsHit.add(r)
                
        #     for l in range(robots[i], (robots[i]-distance[i]-1), -1):
        #         if l in robots and l!=robots[i]:
        #             break
        #         if l not in wallsHit and l in walls:
        #             wallsHit.add(l)
                
        # return len(wallsHit)

