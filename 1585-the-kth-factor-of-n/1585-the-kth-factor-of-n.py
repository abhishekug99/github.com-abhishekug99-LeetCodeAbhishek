class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact = []
        for i in range(1, n+1):
            if n%i==0:                
                fact.append(i)
        # print(fact)
        if len(fact)>=k:
            return fact[k-1]
        return -1
        