class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diffgrid = [[0]*(n+1) for _ in range(n+1)]
        for r1,c1,r2,c2 in queries:
            diffgrid[r1][c1]+=1
            diffgrid[r1][c2+1]-=1
            diffgrid[r2+1][c1]-=1
            diffgrid[r2+1][c2+1]+=1
        
        res = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                top=0 if r == 0 else res[r-1][c]
                left = 0 if c == 0 else res[r][c-1]
                topleft = 0 if r==0 or c==0 else res[r-1][c-1]
                res[r][c] = diffgrid[r][c]+top+left-topleft
        
        return res
        
        # Works great TLE O(q*n^2)
        # grid = [[0]*n for _ in range(n)]
        # def dfs(r, c, r2, c2, visited):
        #     if r > r2 or c > c2:
        #         return
        #     if (r, c) in visited:
        #         return

        #     visited.add((r, c))
        #     grid[r][c] += 1

        #     dfs(r, c + 1, r2, c2, visited)
        #     dfs(r + 1, c, r2, c2, visited)

        # for r1, c1, r2, c2 in queries:
        #     visited = set()
        #     dfs(r1, c1, r2, c2, visited)

        # return grid