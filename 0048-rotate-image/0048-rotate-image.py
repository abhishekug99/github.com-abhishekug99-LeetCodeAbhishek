class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        l , r = 0, len(matrix)-1
        while l<r:
            for i in range(r-l):
                top, bottom = l,r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l] # move bottom left to top left
                matrix[bottom-i][l] =  matrix[bottom][r-i] #bottom right to bottom left
                matrix[bottom][r-i] = matrix[top+i][r] #top right to bottom right
                matrix[top+i][r] = topLeft
            r-=1
            l+=1
        




        