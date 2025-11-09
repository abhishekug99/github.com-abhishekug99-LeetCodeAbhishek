class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # O(max(num1,num2))
        # res = 0
        # if num1==0 or num2==0:
        #     return 0
        # if num1 == num2:
        #     return 1
        # while num1 != 0 and num2 !=0:
        #     if num1>num2:
        #         num1 -= num2
        #         res+=1
        #     else:
        #         num2 -= num1
        #         res+=1
        # return res
        
        # O(log(max(num1,num2)))
        res = 0
        if num1 ==0 or num2 ==0:
            return 0
        while num1 and num2:
            res+=num1//num2
            num1%=num2
            num1,num2 = num2, num1
        return res


        