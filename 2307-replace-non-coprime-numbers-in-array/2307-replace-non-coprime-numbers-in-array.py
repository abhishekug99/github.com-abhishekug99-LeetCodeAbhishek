class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def getGCD(a,b):
            while b:
                a,b = b, a%b
            return a
        def getLCM(x,y):
            return x * y // getGCD(x, y)

        res = []
        for num in nums:
            res.append(num)
            while len(res)>1:
                g = getGCD(res[-1],res[-2])
                if g==1:
                    break
                lcm = getLCM(res[-1],res[-2])
                res.pop()
                res[-1]=lcm
            
        return res
        