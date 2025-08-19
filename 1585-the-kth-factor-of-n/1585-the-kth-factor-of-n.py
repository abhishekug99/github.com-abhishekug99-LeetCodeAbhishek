class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # without extra space
        cnt = 1
        i =1
        while i <= n:
            if cnt == k:
                return i
            i+=1
            if n%i==0:
                cnt+=1
        return -1

        #most common but takes extra space O(n) 
        # fact = []
        # for i in range(1, n+1):
        #     if n%i==0:                
        #         fact.append(i)
        # # print(fact)
        # if len(fact)>=k:
        #     return fact[k-1]
        # return -1
        