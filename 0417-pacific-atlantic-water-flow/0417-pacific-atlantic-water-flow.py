class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 1 and len(heights[0]) == 1:
            return [[0,0]]
        dirs = [(1,0),(-1,0),(0,-1), (0,1)]
        ROW = len(heights)
        COL = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c, visited):
            # if (r,c) in visited:
            #     return 

            visited.add((r,c))
            for dr,dc in dirs:
                nr =dr+r
                nc =dc+c
                if (0<=nr<ROW and 0<=nc<COL and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]) :
                    dfs(nr,nc, visited)
            
        
        
        for c in range(COL):
            dfs(0,c,pacific)
            dfs(ROW-1,c,atlantic)
        for r in range(ROW):
            dfs(r,0,pacific)
            dfs(r,COL-1, atlantic)
        
        res = list(pacific & atlantic)
        return res        
        
        
        
        # for r in range(len(heights)):
        #     for c in range(len(heights[0])):
        #         tmp=[]

        
        