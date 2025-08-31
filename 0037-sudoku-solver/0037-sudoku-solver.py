from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Pre-fill the sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(idx=0):
            if idx == len(empty):  # all cells filled
                return True

            r, c = empty[idx]
            b = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    # place num
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(idx + 1):
                        return True

                    # undo choice
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack()


    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     def isValid(r, c, val):
    #         for i in range(9):
    #             if board[i][c] == val:
    #                 return False
                    
    #         # check row
    #         for j in range(9):
    #             if board[r][j] == val:
    #                 return False
            
    #         rowStart, colStart = (r // 3) * 3, (c // 3) * 3
    #         for i in range(rowStart, rowStart + 3):
    #             for j in range(colStart, colStart + 3):
    #                 if board[i][j] == val:
    #                     return False
    #         return True

    #     def backtrack():
    #         for r in range(9):
    #             for c in range(9):
    #                 if board[r][c] == '.':
    #                     for num in map(str, range(1, 10)):  # 1 through 9
    #                         if isValid(r, c, num):
    #                             board[r][c] = num
    #                             if backtrack():
    #                                 return True
    #                             board[r][c] = '.'  
    #                     return False  
    #         return True  # solved

    #     backtrack()
