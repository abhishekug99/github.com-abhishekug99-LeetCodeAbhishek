class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        lenght = len(board)
        board.reverse()#vimp
        def posToRC(squareNum):
            r = (squareNum-1)// lenght
            c = (squareNum-1) % lenght
            if r%2:
                c = lenght - 1 - c
            return [r,c]
        
        queue = deque()
        queue.append([1,0]) #[squareNum, moves]
        visited = set()
        while queue:
            squareNum, moves = queue.popleft()
            
            for i in range(1,7): #max on doce
                nextSquareNum = i+squareNum
                r,c = posToRC(nextSquareNum)
                if board[r][c] != -1:
                    nextSquareNum = board[r][c]
                if nextSquareNum == lenght*lenght:
                    return moves+1
                if nextSquareNum not in visited:
                    visited.add(nextSquareNum)
                    queue.append([nextSquareNum, moves+1])
        return -1

    
        