class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        counter = 0
        while a>0 or b>0 or c>0:
            aBi = a & 1
            bBi = b & 1
            cBi = c & 1
            if (aBi|bBi)!=cBi:
                if cBi ==1:
                    counter+=1
                else:
                    counter+=(aBi+bBi)
            a>>=1
            b>>=1
            c>>=1
        return counter
        
        # counter = 0
        # orth = a|b
        # if orth == c:
        #     return 0
        # # while orth!=c:
        # for _ in range(max(a,b)):
        #     if orth<c:
        #         orth=orth|1
        #         counter+=1
        #     if orth >c:
        #         orth= ~orth+1
        #         counter-=1
        
        # return counter

        