class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
        # if len(s) == 1 and s[0] =='1':
        #     return True

        # if s[0] == '1' and '1' not in s[1:]:
        #     return True 
        # if all(b for b in s) == 1:
        #     return True

        # f = False
        # for i in range(1, len(s)-1):
        #     if (s[i]=='1' and s[i-1]=='1') and s[i+1]!='1' :
        #         f = True
        #     else:
        #         f=False

        # return f 