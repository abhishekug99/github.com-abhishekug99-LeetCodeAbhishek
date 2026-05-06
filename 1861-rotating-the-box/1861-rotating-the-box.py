class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROW = len(boxGrid)
        COL = len(boxGrid[0])
        res = [['']*ROW for _ in range(COL)]
        for r in range(ROW):
            write = COL - 1
            for c in range(COL - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    write = c - 1
                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][write] = '#'
                    write -= 1

        # Step 2: Rotate 90 degrees clockwise
        for r in range(ROW):
            for c in range(COL):
                res[c][ROW - 1 - r] = boxGrid[r][c]

        return res