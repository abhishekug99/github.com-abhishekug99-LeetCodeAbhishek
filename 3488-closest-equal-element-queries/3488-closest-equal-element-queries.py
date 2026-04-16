class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        mapnums = defaultdict(list)
        n = len(nums)

        for i, v in enumerate(nums):
            mapnums[v].append(i)

        res = []

        for q in queries:
            curr = nums[q]
            idxPos = mapnums[curr]

            if len(idxPos) == 1:
                res.append(-1)
                continue

            idx = bisect_left(idxPos, q)

            left = idxPos[idx - 1]  # circular left
            right = idxPos[(idx + 1) % len(idxPos)]  # circular right

            d1 = abs(q - left)
            d2 = abs(q - right)

            dist = min(d1, n - d1, d2, n - d2)
            res.append(dist)

        return res
            
        
        # Correct but TLE 612/614
        # mapnums = defaultdict(list)
        # res = []
        # n=len(nums)
        # if len(nums) == len(set(nums)):
        #     return [-1]*len(queries)

        # for i in range(len(nums)):
        #     mapnums[nums[i]].append(i)

        # # print(mapnums)
        # for q in queries:
        #     curr = nums[q]
        #     # minDist = float('inf')
        #     idxPos = mapnums[curr]
        #     if len(idxPos)==1:
        #         res.append(-1)
        #         continue
        #     for i in range(len(idxPos)):
        #         if mapnums[curr][i] == q:
        #             idx=i
        #     l = mapnums[curr][idx-1]
        #     r = mapnums[curr][(idx+1)%len(idxPos)]
        #     d1 = abs(q-l)
        #     d2 = abs(q-r)
        #     dist = min(d1,n-d1,d2,n-d2)
        #         # dist = (abs(mapnums[curr][idx]-mapnums[curr][idx-1]))%n
        #         # minDist = min(minDist, dist)
        #     res.append(dist)
        # return res
