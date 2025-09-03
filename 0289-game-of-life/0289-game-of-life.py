class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0), (1,0), (0,1), (0,-1), (-1,1), (1,-1), (1,1), (-1,-1)]
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        
        def traverse(r,c):    
            cnt = 0
            for dr,dc in directions:
                if min(r+dr,c+dc)< 0 or r+dr >= ROW or c+dc >= COL:
                    continue
                elif board[r+dr][c+dc]==1:
                    cnt+=1
            return cnt
        
        futureStage = [[board[r][c] for c in range(COL)] for r in range(ROW)]

        for r in range(ROW):
            for c in range(COL):
                surr1 = traverse(r,c)
                # print(surr1)
                if board[r][c]==1:
                    if surr1<2:
                        futureStage[r][c]=0
                    elif surr1==2 or surr1==3:
                        futureStage[r][c]=1
                    elif surr1>3:
                        futureStage[r][c]=0
                else:
                    if surr1 == 3:
                        futureStage[r][c]=1
        
        for r in range(ROW):
            for c in range(COL):
                board[r][c] = futureStage[r][c]


