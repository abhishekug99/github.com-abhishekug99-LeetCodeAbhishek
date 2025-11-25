class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        res = 1
        prev = set()
        while curr % k:
            if curr in prev:
                return -1
            prev.add(curr)
            curr = 10*(curr%k)+1
            res+=1
        return res

        #logically correct but getting ot of int Constraints
        # if k == 1:
        #     return 1
        # if k%2==0 or k%5==0:
        #     return -1 
        # res = 1
        # while res%k!=0:  
        #     res*=10
        #     res+=1
        #     if res%k==0:
        #         print(res)
        #         return len(str(res))
        #     # print(res)
        # return -1