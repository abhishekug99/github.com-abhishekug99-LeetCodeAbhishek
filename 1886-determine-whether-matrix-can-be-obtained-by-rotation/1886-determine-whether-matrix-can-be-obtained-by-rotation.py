class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rot90(matrix):
            n=len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            for i in range(n):
                matrix[i].reverse()
        r=0
        rotated = mat
        for _ in range(4):
            if rotated == target:
                return True
            rot90(rotated)
    
        return False