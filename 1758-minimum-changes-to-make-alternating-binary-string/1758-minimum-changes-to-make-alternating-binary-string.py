class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = 0  
        alt2 = 0  

        for i in range(len(s)):
            if s[i] != str(i % 2):
                alt1 += 1
            if s[i] != str((i + 1) % 2):
                alt2 += 1

        return min(alt1, alt2)
        
        # if len(s) == 2 and len(set(s)) == 2:
        #     return 0
        # else:
        #     return 1
        
        # res = 0
        # if s[0] == '1':
        #     for i in range(1, len(s),2):
        #         if s[i]!='1' or (s[i]=='1' and s[i-1]=='1'):
        #             res+=1
        # if s[0] == '0':
        #     for i in range(1, len(s),2):
        #         if s[i]!='0' or (s[i]=='0' and s[i-1]=='0'):
        #             res+=1
        # return res
        

