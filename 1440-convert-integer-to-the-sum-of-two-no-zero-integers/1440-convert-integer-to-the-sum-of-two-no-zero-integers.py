class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res=[]
        half = n//2
        
        def isZeroInNum(n: int)->bool:
            return '0' in str(n)

        # if n%10==0:
        for i in range(1,n):
            b = n-i
            if not isZeroInNum(i) and not isZeroInNum(b):
                return [i, b]