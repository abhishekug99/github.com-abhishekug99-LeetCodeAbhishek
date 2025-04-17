class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def BFS(grid):
            path = 0
            ROW, COL = len(grid), len(grid[0])
            er, ec = entrance
            visit = {(er, ec)}
            queue = deque([(er, ec)])
            nbrs = [[0,1],[0,-1],[1,0],[-1,0]]
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    # if grid[r][c] == '.':
                    #     if r==0 or r==ROW-1 or c==0 or c==COL-1:
                    #         return path+1
                    for dr,dc in nbrs:
                        if (min(r+dr,c+dc)<0 or (r+dr,c+dc) in visit or r+dr == ROW or c+dc == COL or grid[r+dr][c+dc] == '+'):
                            continue
                        if r+dr == 0 or r+dr ==ROW-1 or c+dc ==0 or c+dc==COL-1:
                            return path+1
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                path+=1
                
            return -1
        return BFS(maze)

                    

            


         