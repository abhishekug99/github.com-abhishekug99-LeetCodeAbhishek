class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = []
        def dfs(r,c, direction):
            if r < 0 or c<0 or r>=ROWS or c >= COLS or (r,c) in visited:
                return
            res.append(matrix[r][c])
            visited.add((r,c))

            if direction  == 'right':
                if c+1 < COLS and (r,c+1) not in visited:
                    dfs(r,c+1,'right')
                else:
                    dfs(r+1,c, 'down')

            elif direction == 'down':
                if r+1 < ROWS and (r+1,c) not in visited:
                    dfs(r+1,c, 'down')
                else:
                    dfs(r,c-1, 'left')

            elif direction == 'left':     
                if c-1 >= 0 and (r,c-1) not in visited:
                    dfs(r,c-1, 'left')
                else:
                    dfs(r-1,c, 'up')
            
            elif direction == 'up':  #imp Case
                if r-1>=0 and (r-1,c) not in visited:
                    dfs(r-1,c, 'up')
                else:
                    dfs(r,c+1, 'right')

            # print(visited)
        dfs(0,0,'right')

        return res
