class Solution:
    def longestPalindrome(self, s: str) -> str:
        tStr = ''
        tStrLen= 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] ==s[r]:
                if (r-l+1)>tStrLen:
                    tStr = s[l:r+1]
                    tStrLen = r-l+1
                l-=1
                r+=1
            #for even lengths
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] ==s[r]:
                if (r-l+1)>tStrLen:
                    tStr = s[l:r+1]
                    tStrLen = r-l+1
                l-=1
                r+=1
        return tStr
            


        
    
        
        
        #works but as bruteforce, give time exceed
        # maxLen = 0
        # longestPal = ''
        # l = 0
        # def isPalindrome(s: str) -> bool:
        #     if s==s[::-1]:
        #         return True
        #     else: False
        
        # while l<len(s):
        #     for r in range(len(s)):
        #         if isPalindrome(s[l:r+1]):
        #             currPal = s[l:r+1]
        #             longestPal = max((currPal, longestPal), key  = len)
        #     l+=1

        # return longestPal 

                

        
        