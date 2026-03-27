from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        total = 0
        row_sum = [0] * n
        col_sum = [0] * m

        min_row = {}
        max_row = {}
        min_col = {}
        max_col = {}

        # Precompute totals, row sums, col sums, and value boundaries
        for r in range(n):
            for c in range(m):
                val = grid[r][c]
                total += val
                row_sum[r] += val
                col_sum[c] += val

                if val not in min_row:
                    min_row[val] = max_row[val] = r
                    min_col[val] = max_col[val] = c
                else:
                    if r < min_row[val]:
                        min_row[val] = r
                    if r > max_row[val]:
                        max_row[val] = r
                    if c < min_col[val]:
                        min_col[val] = c
                    if c > max_col[val]:
                        max_col[val] = c

        # Horizontal cuts
        top_sum = 0
        for cut in range(n - 1):
            top_sum += row_sum[cut]
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                # remove from top section: rows [0..cut], all columns
                rows = cut + 1
                cols = m

                if rows > 1 and cols > 1:
                    if diff in min_row and min_row[diff] <= cut:
                        return True
                elif rows == 1:
                    # only removable ends in row 0
                    if grid[0][0] == diff or grid[0][m - 1] == diff:
                        return True
                else:  # cols == 1
                    if grid[0][0] == diff or grid[cut][0] == diff:
                        return True
            else:
                # remove from bottom section: rows [cut+1..n-1], all columns
                rows = n - (cut + 1)
                cols = m

                if rows > 1 and cols > 1:
                    if diff in max_row and max_row[diff] >= cut + 1:
                        return True
                elif rows == 1:
                    # only removable ends in last row
                    if grid[n - 1][0] == diff or grid[n - 1][m - 1] == diff:
                        return True
                else:  # cols == 1
                    if grid[cut + 1][0] == diff or grid[n - 1][0] == diff:
                        return True

        # Vertical cuts
        left_sum = 0
        for cut in range(m - 1):
            left_sum += col_sum[cut]
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                # remove from left section: all rows, cols [0..cut]
                rows = n
                cols = cut + 1

                if rows > 1 and cols > 1:
                    if diff in min_col and min_col[diff] <= cut:
                        return True
                elif rows == 1:
                    if grid[0][0] == diff or grid[0][cut] == diff:
                        return True
                else:  # cols == 1
                    if grid[0][0] == diff or grid[n - 1][0] == diff:
                        return True
            else:
                # remove from right section: all rows, cols [cut+1..m-1]
                rows = n
                cols = m - (cut + 1)

                if rows > 1 and cols > 1:
                    if diff in max_col and max_col[diff] >= cut + 1:
                        return True
                elif rows == 1:
                    if grid[0][cut + 1] == diff or grid[0][m - 1] == diff:
                        return True
                else:  # cols == 1
                    if grid[0][m - 1] == diff or grid[n - 1][m - 1] == diff:
                        return True

        return False