from math import factorial 
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        res = 1
        MOD = 10**9+7

        for i in range(1, len(complexity)):
            if complexity[i]<=complexity[0]:
                return 0
            res= (res*i)%MOD
                
        return res
        
        # unlocked = set()
        # res = 0
        # for j in range(len(complexity)):
        #     if j==0:
        #         unlocked.add(j)
        #     i=j+1
        #     while i<len(complexity):
        #         if i not in unlocked and i-1 in unlocked and complexity[j]<complexity[i]:
        #             unlocked.add(i)
        #         elif not i-1 in unlocked:
        #             break
        #         i+=1
        # # print(unlocked)
        # perms = permutations(list(unlocked)[1:])
        # return len(list(perms)) if len(unlocked)>1 else 0 

                


