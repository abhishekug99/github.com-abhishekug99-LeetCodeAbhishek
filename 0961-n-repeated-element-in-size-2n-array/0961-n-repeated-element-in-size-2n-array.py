class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(set(nums))
        # cnts = Counter(nums)
        # # print(cnts)
        # for k,v in cnts.items():
        #     if v==n-1:
        #         return k
        
        cnts1={}
        for v in nums:
            if v not in cnts1:
                cnts1[v]=1
            elif v in cnts1 and cnts1[v]==n-1:
                return v  
            
            cnts1[v]+=1
            


        