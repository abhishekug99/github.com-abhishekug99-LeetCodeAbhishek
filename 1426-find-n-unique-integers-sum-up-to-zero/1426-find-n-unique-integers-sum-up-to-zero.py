class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        res = []
        
        i=1
        # if i%2==0:
        while i <= n//2:
            res.append(-i)
            res.append(+i)
            i+=1
       
        if n%2==1:
            res.append(0)
        
        return res

        


        