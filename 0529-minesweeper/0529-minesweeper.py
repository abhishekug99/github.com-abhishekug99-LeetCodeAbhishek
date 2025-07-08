class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0),(-1,0), (1,1), (1,-1),(0,1),(0,-1),(-1,-1),(-1,1)]
        ROW = len(board)
        COL = len(board[0])
        r,c  = click

        def nbrMines(r,c):
            cnt = 0
            for dr, dc in directions:
                if 0<=r+dr<ROW and 0<= c+dc< COL:
                    if board[r+dr][c+dc] == 'M':
                        cnt+=1
            return cnt

        def dfs(r,c):
            if not  (0 <= r < ROW and 0 <= c < COL) or board[r][c]!='E':
                return
            mines = nbrMines(r,c)
            if mines>0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r+dr,c+dc)
        
        if board[r][c] =='M':
            board[r][c] = 'X'
        else:
            dfs(r,c)
        
        return board



        # for r in range(ROW):
        #     for c in range(COL):
                
        #         if board[click[0]][click[1]] == 'M':
        #             board[click[0]][click[1]] = 'X'
                
        #         if board[click[0]][click[1]] == 'E':
        #             board[click[0]][click[1]] = 'B'
                

        #             for dr,dc in directions:
        #                 if 0 <= r + dr < ROW and 0 <= c + dc < COL:
        #                     if (board[r+dr][c+dc] == 'M' or board[r+dr][c+dc] == 'X'):
        #                         board[r][c] = '1'

        #                     elif board[r+dr][c+dc] == 'E':
        #                         board[r][c] = 'B'

        #                 # if (board[r+1][c+0] == 'M' or board[r+1][c+0] == 'X'):
        #                 #     board[r+1][c+0] == 'E'
        # return board


