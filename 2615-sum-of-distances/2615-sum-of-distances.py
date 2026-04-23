class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        if nums == set(nums):
            return [0]*len(nums)
        res= [0]*len(nums)
        mapidx  = defaultdict(list)
        
        for i in range(len(nums)):
            mapidx[nums[i]].append(i)
        
        for  idxs in mapidx.values():
            n=len(idxs)
            if n==1:
                continue
            prefix = [0]*n
            prefix[0] = idxs[0]
            for i in range(1,n):
                prefix[i] = prefix[i-1] + idxs[i]
            total = prefix[-1]
            for t,p in enumerate(idxs):
                lsum = prefix[t-1] if t>0 else 0
                rsum = total-prefix[t]
                l = t*p - lsum
                r = rsum-(n-t-1)*p
                res[p] = l+r
        return res

        
        # O(n^2)
        # for simidx in mapidx.values():
        #     if  len(simidx)==1:
        #         continue
        #     for i in range(len(simidx)):
        #         curr = 0
        #         for j in range(len(simidx)):
        #             if i!=j:
        #                 curr+= abs(simidx[i]-simidx[j])
        #         res[simidx[i]] = curr
        # return res 
