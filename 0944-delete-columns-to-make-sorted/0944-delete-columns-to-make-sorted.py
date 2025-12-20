class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        ROW  = len(strs)
        COL = len(strs[0])
        for c in range(COL):
            for r in range(1, ROW):
                if strs[r][c]<strs[r-1][c]:
                    res+=1
                    break
        return res