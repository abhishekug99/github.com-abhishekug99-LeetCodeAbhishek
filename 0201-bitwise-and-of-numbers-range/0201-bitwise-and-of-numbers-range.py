class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left>>=1
            right>>=1
            shift+=1
        return left << shift

        
        # return (left & right)
        # b1 = str(bin(left)[2:])
        # b2 = str(bin(right)[2:])
        # i,j = len(b1)-1, len(b2)-1
        # res =''
        # while i>=0 or j>=0:
        #     if b1[i] == '1' and b2[j] == '0':
        #         res+='0'
        #     elif b1[i] == '0' and b2[j] == '1':
        #         res+='0'
        #     elif b1[i] == '0' and b2[j] == '0':
        #         res+='0'
        #     elif b1[i] == '1' and b2[j] == '1':
        #         res+='1'
        #     elif not b1[i] and b2[j]:
        #         res+='0'
        #     elif not b2[j] and b1[i]:
        #         res+='0' 
        #     i-=1
        #     j-=1
        # res = res[::-1]
        # return int(res,2)


             

            
        print(b2)