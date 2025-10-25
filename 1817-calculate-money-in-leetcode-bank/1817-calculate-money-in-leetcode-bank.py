class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        if n<=7:
            for i in range(1,n+1):
                res+=i
            return res

        niter = n//7
        remain = n - niter*7
        start =1
        end =8
        for i in range(1, niter+1):
            curRes = 0
            for j in range(start, end):
                curRes+=j
            res+=curRes
            start+=1
            end+=1

        for i in range(niter+1,  niter+1+remain):
            res+=i

        return res

