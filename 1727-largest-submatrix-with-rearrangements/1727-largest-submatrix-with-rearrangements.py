class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res= 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]!=0 and r>0:
                    matrix[r][c]+=matrix[r-1][c]
            
            current = sorted(matrix[r], reverse=True)
            for i in range(len(current)):
                res = max(res, current[i]*(i+1))
        return res