class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
#Every time a value increases relative to the previous one, you need that many new     operations.
# When it decreases or stays the same, you don’t add new operations.
        res = target[0]
        for i in range(1, len(target)):
            res+= max(0, target[i]-target[i-1])
        return res
        
        # correct approach, TLE
        # res = 0
        # initial = [0]*len(target)
        
        # while initial != target:
        #     i=0
        #     while i<len(target):
        #         if initial[i]<target[i]:
        #             j=i
        #             while j<len(target) and initial[j]<target[j]:
        #                 initial[j]+=1
        #                 j+=1
        #             res+=1
        #             i=j
        #         else:
        #             i+=1
        # return res
        
        