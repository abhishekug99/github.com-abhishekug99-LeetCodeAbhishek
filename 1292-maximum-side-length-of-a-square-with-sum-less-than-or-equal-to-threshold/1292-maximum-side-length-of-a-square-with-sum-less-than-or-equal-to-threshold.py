class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                prefix[i][j] = (mat[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]) 
        
        def isValidSquare(k):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    total  = (prefix[i+k][j+k]-prefix[i][j+k]-prefix[i+k][j]+prefix[i][j])
                    if total<=threshold:
                        return True
            return False
        
        l,r = 1, min(m,n)
        res = 0
        while l<=r:
            mid = (l+r)//2
            if isValidSquare(mid):
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res
