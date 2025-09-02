class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        zeros = set()
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0 and (r,c) not in zeros:
                    zeros.add((r,c))

        for a,b in zeros:
            for i in range (ROW):
                matrix[i][b]=0
            for j in range(COL):
                matrix[a][j]=0
        
                
