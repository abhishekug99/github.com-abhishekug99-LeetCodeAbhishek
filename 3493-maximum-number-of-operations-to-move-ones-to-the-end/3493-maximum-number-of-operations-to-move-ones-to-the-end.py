class Solution:
    def maxOperations(self, s: str) -> int:
        #reverse order way
        zeros = 0
        res=0

        for i in reversed(range(len(s))):
            if s[i] == '0':
                if (i == len(s)-1 or s[i+1] =='1'):
                    zeros+=1
            else:
                res+=zeros
        return res
            
        
        #works O(n)
        # res = 0
        # ones = 0
        # i = 0
        # while i<len(s):
        #     if s[i] =='1':
        #         ones+=1
        #     else:
        #         while i+1<len(s) and s[i+1] == '0':
        #             i+=1
        #         res+=ones    
        #     i+=1
        # return res
                
