class Solution:
    def calculate(self, s: str) -> int:
        #way to optimise O(1) space:
        stack = []
        op = '+' #intial operato ot compare
        num =0
        for char in s.replace(' ','')+'+':
            if char.isdigit():
                num = 10*num+int(char)
            else:
                if op =='+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    stack.append(int(stack.pop()/num))
                num=0
                op=char
            # print(stack)
        return sum(stack)



        # works but takes too much time spac passes all test cases 180 ms
        # sList = list(s)
        # operators = []
        # nums = []
        # def opPriority(op):
        #     if op in ('*','/'):
        #         return 2
        #     if op in ('+','-'):
        #         return 1
        #     return 0
        
        # def operatorToUse(ops,nums):
        #     op = operators.pop()
        #     numLast = nums.pop()
        #     numSLast = nums.pop()
        #     if op =='+':
        #         nums.append(numSLast + numLast)
        #     if op =='-':
        #         nums.append(numSLast - numLast)
        #     if op =='*':
        #         nums.append(numSLast * numLast)
        #     if op =='/':
        #         nums.append(int(numSLast/numLast))
        # i=0
        # n = len(s)
        # while i<n:
        #     if s[i]==' ':
        #         i+=1
        #         continue
        #     if s[i].isdigit():
        #         num = 0
        #         while i<n and s[i].isdigit():
        #             num = num*10+int(s[i])
        #             i+=1
        #         nums.append(num)
        #     else:
        #         while operators and opPriority(operators[-1]) >= opPriority(s[i]):
        #               operatorToUse(operators,nums)
        #         operators.append(s[i])
        #         i+=1
        # while operators:
        #     operatorToUse(operators,nums)
        
        # return nums[0]
            
            

