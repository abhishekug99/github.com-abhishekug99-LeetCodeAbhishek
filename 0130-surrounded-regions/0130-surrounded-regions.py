class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        ROW = len(board)
        COL = len(board[0])

        def dfs(r,c):
            if r<0 or c<0 or r>= ROW or c>=COL or board[r][c]!='O':
                return
            board[r][c] = 'S' #as in spot is safe
            for dr,dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(ROW):
            if board[r][0] =='O':
                dfs(r,0)
            if board[r][COL-1] == 'O':
                dfs(r,COL-1)
        
        for c in range(COL):
            if board[0][c] =='O':
                dfs(0,c)
            if board[ROW-1][c] == 'O':
                dfs(ROW-1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


        # correct but lot of mising test cases
        # region = set()
        # def checkRegion(r,c)-> bool:
        #     res = set()
        #     for dr,dc in directions:
        #         if board[dr+r][dc+c] == 'O':
        #             res.add((dr+r,dc+c))
        #     if len(res)<4:
        #         return True
        #     if len(res) == 4:
        #         return False
        #     return False

        
        # for r in range(1, ROW-1):
        #     for c in range(1, COL-1):
        #         # print((r,c))
        #         if r < ROW-1 and c < COL-1 and board[r][c] == 'O' and checkRegion(r,c):
        #             region.add((r,c))
        # # print(region)
        # for r,c in region:
        #     # print(r,c)
        #     board[r][c] = 'X'
          
        """
        Do not return anything, modify board in-place instead.
        """
        