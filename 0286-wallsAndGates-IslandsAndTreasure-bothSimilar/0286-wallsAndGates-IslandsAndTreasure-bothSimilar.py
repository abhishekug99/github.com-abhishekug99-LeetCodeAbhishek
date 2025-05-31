    """Problem descrption
    https://leetcode.com/problems/walls-and-gates/
    You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
    """


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c,dist):
            if r < 0 or c<0 or r>=ROWS or c >= COLS:
                return

            if grid[r][c]<dist:
                return

            grid[r][c] = dist
            dfs(r+1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c-1,dist+1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r,c,0)
        
        # return grid

# examples
"""
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

"""