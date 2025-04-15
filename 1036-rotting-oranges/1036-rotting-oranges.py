class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0

        def bfs(grid):
            ROW, COL = len(grid), len(grid[0])
            visit = set()
            queue = deque()

            # Add all initially rotten oranges to queue
            for r in range(ROW):
                for c in range(COL):
                    if grid[r][c] == 2:
                        queue.append((r, c))
                        visit.add((r, c))

            nonlocal time
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    nbrs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in nbrs:
                        nr, nc = r + dr, c + dc
                        if ( 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visit and grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            visit.add((nr, nc))
                if queue:
                    time += 1

        bfs(grid)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return time  