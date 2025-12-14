class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        res = 1
        chairCnt =0
        plants = 0
        for c in corridor:
            if c=='S':
                chairCnt+=1
                if chairCnt%2==1 and plants>0:
                    res = (res*(plants+1))%MOD
                    plants=0
            elif chairCnt%2==0 and chairCnt > 0:
                plants+=1
        return res if chairCnt>0 and chairCnt%2==0 else 0



        # if len(corridor)<2:
        #     return 0
        # if 'S' not in corridor:
        #     return 0

        # for i in range(len(corridor)):
        #     if corridor[i]=='S':
        #         chairCnt+=1
        #     if chairCnt==2 and i+1<len(corridor):
        #         j=i+1
        #         # print(j)
        #         # print(i)
        #         while j<len(corridor) and corridor[j]!='S':
        #             if j==len(corridor)-1:
        #                 break
        #             j+=1
        #         res += (j-i-1)
        #         break
        # return res%MOD
     