class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor) 
        return max(min(res, 2**31 - 1), -2**31)
        
        # res = dividend/divisor
        # print(res)
        # if res ==0:
        #     return 0
        # if divisor == -1:
        #     return int(res) if dividend<0 else int(res) 
        # if res<0:
        #     res = str(res)
        #     res = res[1:]
        #     res = res.split('.')
        #     return -int(res[0])
        # else:
        #     res = str(res)
        #     res = res.split('.')
        #     return int(res[0])
        
