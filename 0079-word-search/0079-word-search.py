class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def dfsBacktrack(r,c,i):
            if i == len(word):
                return True

            if min(r,c)<0 or r == ROW or c == COL or (r,c) in visited or board[r][c] != word[i]:
                return False
            
    
            visited.add((r,c))
            res = (dfsBacktrack(r+1,c,i+1) or
                dfsBacktrack(r-1,c,i+1) or
                dfsBacktrack(r,c+1,i+1) or
                dfsBacktrack(r,c-1,i+1) )

            visited.remove((r,c))
            return res

        for r in range(ROW):
            for c in range(COL):
                if dfsBacktrack(r,c,0):
                    return True
        return False

        # #dp not yet completed
        # res=['']*len(word)
        # # print(res)
        # i=0
        # for r in range(ROW):
        #     for c in range(COL):
        #         if i<=len(res) and word[i] == board[r][c]:
        #             res[i] =  board[r][c]
        #             i+=1
        # if ''.join(res) == word:
        #     return True
        # else:
        #     return False