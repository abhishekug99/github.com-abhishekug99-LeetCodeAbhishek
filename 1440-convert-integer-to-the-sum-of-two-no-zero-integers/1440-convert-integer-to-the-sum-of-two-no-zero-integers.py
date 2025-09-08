class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res=[]
        half = n//2
        
        def isZeroInNum(n: int)->bool:
            return '0' in str(n)

        for i in range(1,n):
            if not isZeroInNum(i) and not isZeroInNum(n-i):
                return [i, n-i]
    
        