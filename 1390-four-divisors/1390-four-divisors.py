class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def isPrime(n):
            if n<2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        
        res =0
        for n in nums:
            for d in range(2, int(n**0.5) + 1):
                if n % d == 0:
                    other = n // d
                    if (d != other and isPrime(d) and isPrime(other)) or (other==d*d and isPrime(d)) :
                        res += 1 + d + other + n
                        break
                    # if other==d*d and isPrime(d):
                    #     res += 1 + d + other + n
                    #     break
        return res

        
        #bruteforce TLE
        # numDiv = 0
        # sumDiv = 0
        # res = 0
        # for n in nums:
        #     numDiv = 0
        #     sumDiv = 0
        #     for digi in range(1, n+1):
        #         if n%digi==0:
        #             numDiv+=1   
        #             sumDiv+=digi
        #             if numDiv>4:
        #                 break
        #     if numDiv==4:
        #         res+=sumDiv
        # return res
