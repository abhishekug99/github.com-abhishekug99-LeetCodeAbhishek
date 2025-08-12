class Solution:
    # def trailingZeroes(self, n: int) -> int:
        #correct opproach, exceeds the limit of 4300 digits
        
        # if n < 4:
        #     return 0
        
        # res = 0
        # fact = 1
        
        # for num in range(1, n + 1):
        #     fact *= num
        
        # fact = str(fact)
        # print(fact)  
        
        # if fact[-1] == '0':
        #     for i in range(len(fact) - 1, -1, -1):
        #         if fact[i] == '0':
        #             res += 1
        #         else:
        #             break
        
        # return res
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            n //= 5
            res += n
        return res

