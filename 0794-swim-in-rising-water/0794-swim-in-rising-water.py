import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        nbrs = defaultdict(list)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        res = 0
        heap = [(grid[0][0],0,0)]

        while heap:
            height, r,c = heapq.heappop(heap)
            res = max(res, height)
            if r == ROW-1 and c == COL-1:
                return res
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr, dc in dirs:
                nr = dr+r
                nc = dc+c
                if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in visited:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc)) 

        
        # for r in range(ROW):
        #     for c in range(COL):
        #         for dr,dc in dirs:
        #             nr = dr+r
        #             nc = dc+c
        #             if 0<=nr<ROW and 0<=nc<COL:
        #                 heapq.heappush(nbrs[(r,c)], grid[nr][nc])
        # print(nbrs)
        # res = set()
        # waitT = 0
        # for k, v in nbrs.items():
        #     minT = heapq.heappop(v)
        #     res.add(minT)
        #     # waitT = max(minT, waitT)
        # print(res)
        # res= list(res)
        # return res[-1]

