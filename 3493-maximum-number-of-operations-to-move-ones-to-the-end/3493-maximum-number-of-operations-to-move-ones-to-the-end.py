class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        ones = 0
        i = 0
        while i<len(s):
            if s[i] =='1':
                ones+=1
            else:
                while i+1<len(s) and s[i+1] == '0':
                    i+=1
                res+=ones    
            i+=1
        return res
                
