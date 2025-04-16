class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def BFS(grid):
            ROW = len(grid)
            COL = len(grid[0])
            visit = set()
            queue = deque()
            queue.append((0,0))
            visit.add((0,0))
            path = 1
            if grid[0][0]!=0 or grid[ROW-1][COL-1] != 0:
                return -1
            nbrs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if r == ROW-1 and c ==COL-1:
                        return path
                    
                    # for dr,dc in  nbrs:
                    #     if (0 <= r+dr < ROW and 0 <= c+dc < COL and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]==0):
                    #         # continue
                    #         queue.append((r+dr,c+dc))
                    #         visit.add((r+dr,c+dc))
                    for dr,dc in  nbrs:
                        if (min(r+dr,c+dc)<0 or (r+dr,c+dc) in visit or r+dr == ROW or c+dc==COL or grid[r+dr][c+dc]==1):
                            continue
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                path+=1
                print(queue)
            return -1

        return BFS(grid)
        