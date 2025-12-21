class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        sortdpairs = [False]*(len(strs)-1)        
        for c in range(len(strs[0])):
            rmv = False
            for r in range(len(strs)-1):  
                if not sortdpairs[r] and strs[r][c]>strs[r+1][c]:
                    rmv = True
                    break
            if rmv:
                res+=1
                continue
            for r in range(len(strs)-1):
                if not sortdpairs[r] and strs[r][c]<strs[r+1][c]:
                    sortdpairs[r]=True

        return res