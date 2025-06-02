class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) ==1:
            return int(tokens[0])
        validOp = ['+', '-', '*', '/']
        stack = []
        curr = 0
        def op(a,b,sign: str):
            if sign == '+':
                return a+b
            if sign == '*':
                return a*b
            if sign == '/':
                return int(a/b)
            if sign == '-':
                return a-b
        for i in range(len(tokens)):
            if tokens[i] not in validOp:
                stack.append(int(tokens[i]))
                
            if tokens[i] in validOp:
                a =stack.pop()
                b =stack.pop()
                curr = op(b,a,tokens[i])
                stack.append(curr)
                
        return stack[-1]
