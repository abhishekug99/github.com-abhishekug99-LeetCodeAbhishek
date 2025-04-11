class Solution:
    def countBits(self, n: int) -> List[int]:
        # print(bin(n)[2:])
        res=[]
        
        for i in range(n+1):
            count=0
            bi=i
            # bi = int(bin(i)[2:])
            while bi>0:
                bi &= (bi-1)
                count+=1
            res.append(count)
    
        return(res)
