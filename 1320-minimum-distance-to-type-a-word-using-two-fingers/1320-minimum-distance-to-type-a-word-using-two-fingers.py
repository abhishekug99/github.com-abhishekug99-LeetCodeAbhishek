class Solution:
    def minimumDistance(self, word: str) -> int:
        n=len(word)
        alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # posMat = [['']*6 for _ in range(5)]
        poscor = {}
        k=0
        for i in range(5):
            for j in range(6):
                if k < len(alphas):
                    poscor[alphas[k]] = (i,j)
                    # posMat[i][j] = alphas[k]
                    k += 1
                else:
                    break
            if k >= len(alphas):
                break
        
        def dist(a,b):
            if a ==-1:
                return 0
            x1,y1 = poscor[a]
            x2,y2 = poscor[b]
            return abs(x1-x2) + abs(y1-y2)
        
        @lru_cache(None)
        def dp(i, f1,f2):
            if i==n:
                return 0
            cur = word[i]
            c1 = dist(f1,cur) + dp(i+1,cur,f2)
            c2 = dist(f2,cur) + dp(i+1, f1, cur)

            return min(c1,c2)

        return dp(0,-1,-1)
