class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        nxtZero = [N]*N
        for i in range(N-2,-1,-1):
            if s[i+1] =="0":
                nxtZero[i] = i+1
            else: 
                nxtZero[i] = nxtZero[i+1]
        res = 0
        for l in range(N):
            zeros = 1 if s[l] =="0" else 0
            r=l
            while zeros*zeros<=N:
                nxtZ = nxtZero[r]
                ones = (nxtZ -l) - zeros
                if ones>=zeros*zeros:
                    res+=min(nxtZ-r, ones - zeros*zeros+1)
                r = nxtZ
                zeros+=1
                if r==N:
                    break
        return res
