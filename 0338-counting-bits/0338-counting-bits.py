class Solution:
    def countBits(self, n: int) -> List[int]:
        #dp
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

        # res=[]
        # for i in range(n+1):
        #     count=0
        #     bi=i
        #     # bi = int(bin(i)[2:])
        #     while bi>0:
        #         bi &= (bi-1)
        #         count+=1
        #     res.append(count)
    
        # return(res)
