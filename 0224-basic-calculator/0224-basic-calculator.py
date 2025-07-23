class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                num = num*10+int(ch)
            elif ch =='+':
                res+=sign * num
                sign = 1
                num = 0
            elif ch == '-':
                res += sign * num
                sign = -1
                num = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res+=sign*num
                res*=stack.pop()
                res+=stack.pop()
                num = 0
        res +=sign*num
        return res





        # stack =  deque()
        # intChar = ['0','1','2','3','4','5','6','7','8','9']
        # for char in s:
        #     if char!=' ':
        #         stack.append(char)
        # print(stack.popleft())
        # res = 0
        # noBraces = 0
        # for i in range(len(stack)):
        #     if stack[i] == '(':
        #         j = i+1
        #         while stack[i] != '(' or stack[i] !=')':
        #             if stack[i] == '+':
        #                 res = stack[i-1]+stack[i-1]
        #             elif

            


        