class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n
        while x>=n:
            x+=1
            xMap = {}
            for c in str(x):
                c= int(c)
                xMap[c] = xMap.get(c,0)+1
            if (list(xMap.keys())==list(xMap.values())):
                break
        return x    