class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        
        tribo = [0]*(n+1)
        tribo[0] = 0
        tribo[1] = 1
        tribo[2] = 1
        
        
        i=3
        while i<n+1:
            tribo[i] = tribo[i-1]+tribo[i-2]+tribo[i-3]
            i+=1
        return tribo[-1]