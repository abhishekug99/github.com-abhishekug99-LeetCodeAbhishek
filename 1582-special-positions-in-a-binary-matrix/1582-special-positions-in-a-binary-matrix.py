class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
    
        r = [sum(row) for row in mat]
        c = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    res += 1
        
        return res