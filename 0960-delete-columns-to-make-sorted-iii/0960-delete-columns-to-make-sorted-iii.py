class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        dp = [1]*len(strs[0])
        for c in range(len(strs[0])):
            for i in range(c):
                valid=True
                for r in range(len(strs)):
                    if strs[r][i]>strs[r][c]:   
                        valid = False
                        break
                if valid:
                    dp[c] = max(dp[c], dp[i]+1)
        return len(strs[0])-max(dp)
         
        # sortdpairs = [False]*(len(strs)-1)        
        # for c in range(len(strs[0])):
        #     rmv = False
        #     for r in range(len(strs)-1):  
        #         if not sortdpairs[r] and strs[r][c]>strs[r+1][c]:
        #             rmv = True
        #             break
        #     if rmv:
        #         res+=1
        #         continue
        #     for r in range(len(strs)-1):
        #         if not sortdpairs[r] and strs[r][c]<strs[r+1][c]:
        #             sortdpairs[r]=True

        # return res