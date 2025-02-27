class Solution:
    def decodeString(self, s: str) -> str:
        sList = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                nStr = ''
                while stack[-1] != '[':
                    nStr = stack.pop()+nStr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * nStr)
        
        return ''.join(stack)

