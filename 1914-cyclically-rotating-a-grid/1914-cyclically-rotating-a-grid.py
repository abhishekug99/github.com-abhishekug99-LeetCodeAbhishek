class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for l in range(layers):
            top, bottom = l, m - l - 1
            left, right = l, n - l - 1

            ring = []

            # 1) Collect the ring

            # top row
            for c in range(left, right + 1):
                ring.append(grid[top][c])

            # right column
            for r in range(top + 1, bottom):
                ring.append(grid[r][right])

            # bottom row
            for c in range(right, left - 1, -1):
                ring.append(grid[bottom][c])

            # left column
            for r in range(bottom - 1, top, -1):
                ring.append(grid[r][left])

            # 2) Rotate the ring counter-clockwise
            length = len(ring)
            shift = k % length
            ring = ring[shift:] + ring[:shift]

            # 3) Put back into grid in same order
            idx = 0

            # top row
            for c in range(left, right + 1):
                grid[top][c] = ring[idx]
                idx += 1

            # right column
            for r in range(top + 1, bottom):
                grid[r][right] = ring[idx]
                idx += 1

            # bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = ring[idx]
                idx += 1

            # left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = ring[idx]
                idx += 1

        return grid
