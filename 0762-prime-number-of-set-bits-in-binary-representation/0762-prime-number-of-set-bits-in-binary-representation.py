class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            bits = bin(n)[2:]
            ones = bits.count('1')
            if ones == 1:
                return False
            if ones == 2:
                return True
            if ones%2==0:
                return False
            limit = int(sqrt(ones))+1
            for i in range(3,limit,2):
                if ones%i==0:
                    return False
            return True
        res=0
        for n in range(left, right+1):
            if isPrime(n):
                res+=1

        return res



            
        