class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)  # Count frequency of each tile

        def backtrack():
            total = 0
            for tile in count:
                if count[tile] > 0:  # Only use available tiles
                    total += 1
                    count[tile] -= 1  # Use this tile
                    total += backtrack()  # Recursive call
                    count[tile] += 1  # Backtrack (restore)
            return total

        return backtrack()