class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start,path,total):
            if total ==target:
                res.append(path[:]) #in backtracing always add the copy
            if total>target:
                return
            for i in range(start,(len(candidates))):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res
        
        # for num in candidates:
        #     if num%target==0:
        #         tmp=[num]*(target//num)
        #         res.append(tmp)
                
        #     tmp = []
        #     i=0
        #     while i<len(candidates):
        #         if sum(tmp)+candidates[i] <= target:
        #             tmp.append(candidates[i])
        #         if sum(tmp)>=target:
        #             tmp.pop()
        #         if sum(tmp) == target and tmp not in res:
        #             res.append(tmp)
        #             break
        #         i+=1
        # return res
