class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def minOpsInRange(l,r):
            if l>r:
                return 0
            selections = 0
            maxDepth = 0
            start = 1
            d = 1
            while start<=r:
                end = start*4 -1 
                lo = max(l, start)
                hi = min(r, end)
                if lo<=hi:
                    cnt=hi-lo+1
                    selections += cnt*d
                    maxDepth = d
                d+=1
                start*=4
            return max(maxDepth, (selections+1)//2)
        total =0
        for l,r in queries:
            total+=minOpsInRange(l,r)
        return total