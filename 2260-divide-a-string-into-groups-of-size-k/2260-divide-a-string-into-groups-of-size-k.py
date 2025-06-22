class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        i = 0
        nStr = ''
        while i<len(s):
            if len(nStr)<k+1:
                nStr+=s[i]
            if len(nStr)<k and  i== len(s)-1:
                nStr = nStr+ (fill*(abs(len(nStr)-k)))                
            if len(nStr)==k:
                res.append(nStr)
                nStr=''
            i+=1
        return res
