class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
       res = []
    #    def backtrack(o,c,s):
    #     if len(s) == 2*n:
    #         return res.append(s)
    #         return
       def backtrack(o,c,s):
        if len(s) == 2*n:
            res.append(s[:])
            return
        if len(s)> 2*n:
            return
        
        if o<n:
            backtrack(o+1,c,s+'(')
        if c<o:
            backtrack(o,c+1,s+')')
       backtrack(0,0,'')
       return res     
    