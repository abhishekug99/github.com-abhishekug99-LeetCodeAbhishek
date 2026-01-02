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
            cnts1[v] = cnts1.get(v, 0) + 1
            if cnts1[v] == n-1:
                return v
            


        