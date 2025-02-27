class Solution:
    def removeStars(self, s: str) -> str:
        sList = list(s)
        # sLen = len(sList)
        stack = []

        for i in range(len(sList)):
            if sList[i] != '*':
                stack.append(sList[i])
            if sList[i] == '*' and stack:
                stack.pop()
        
        return ''.join(stack)

        # TLE at case 31/65
        # sList = list(s)
        # sLen = len(sList)
        # # stack = []
        # i=0
        # while '*' in sList and  i < len(sList)-1:
        #     if sList[i+1] == '*':
        #         del sList[i] 
        #         del sList[i]
        #         i = max(0,i-1)
        #     else:
        #         i+=1
        # return ''.join(sList)
        

                


