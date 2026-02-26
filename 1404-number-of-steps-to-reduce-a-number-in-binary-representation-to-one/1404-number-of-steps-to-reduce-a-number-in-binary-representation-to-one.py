class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s,2)
        res=0
        if s =="1":
            return 0
        while num!=1:
            if num%2==0:
                num = (num//2) 
                res+=1
            else:
                num+=1
                res+=1
        return res

