class Solution:
    def totalNQueens(self, n: int) -> int:
        col =set()
        posDiag = set() #r+c
        negDiag = set() #r-c
        res = 0
        def backtrack(r):
            if r == n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0)
        return res
        
        # nbrs =  [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        # ROW = n
        # COL = n
        # dp = [[0]*ROW]*COL
        # # print(dp)
        # def backTrack(r,c):
        #     cnt = 0
        #     for a,b in nbrs:
        #         if dp[r+a][c+b] == 'q':
        #             cnt+=1
        #     if cnt==0:
        #         dp[r][c] == 'q'
        # res = 0
        # for r in range(ROW-1):
        #     for c in range(COL-1):
        #         backTrack(r,c)
        #         if dp[r][c] == 'q':
        #             res+=1
        # return res 
        




            

            