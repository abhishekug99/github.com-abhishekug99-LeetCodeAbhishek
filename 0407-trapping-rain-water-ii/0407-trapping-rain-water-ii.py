class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        heap = []
        ROW = len(heightMap)
        COL = len(heightMap[0])
        visited = [[False]*COL for _ in range(ROW)]
        
        for r in range(ROW):
            for c in range(COL):
                if r in [0, ROW-1] or c in [0, COL-1]:
                    heapq.heappush(heap, (heightMap[r][c], r ,c))
                    visited[r][c] = True
        trapped = 0
        maxHeight = 0

        while heap:
            h,r,c = heapq.heappop(heap)
            maxHeight = max(maxHeight, h)
            for dr, dc in dirs:
                nr,nc = dr+r, dc+c
                if 0<=nr<ROW and 0<=nc<COL and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    if nh<maxHeight:
                        trapped+=maxHeight-nh
                    heapq.heappush(heap, (nh,nr,nc))
        return trapped 
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(r,c, visited):
        #     surr = []
        #     nonlocal vol
        #     if min(r,c)<0 or (r,c) in visited or r>=ROW or c>=COL:
        #         return
        #     if min(heightMap[r+1][c], heightMap[r-1][c], heightMap[r][c+1], heightMap[r][c-1])> heightMap[r][c]:
        #         vol = min(heightMap[r+1][c], heightMap[r-1][c], heightMap[r][c+1], heightMap[r][c-1]) -  heightMap[r][c]
        #     dfs(r+1,c, visited)
        #     dfs(r,c+1, visited)
        #     dfs(r-1,c, visited)
        #     dfs(r,c-1, visited)

        #     # visited.pop()

        #     return vol
        # finalVol = 0
        # for r in range(ROW-1):
        #     for c in range(COL-1):
        #         finalVol+=dfs(r,c, visited)
        # return finalVol

