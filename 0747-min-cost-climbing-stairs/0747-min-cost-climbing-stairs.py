class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        


        # write approach , TLE at 284/285 test case
        if len(cost)==2:
            return min(cost)
        sums = [-1]*(len(cost)+1)
        def dfs(i):
            if i>= len(cost):
                return 0
            if sums[i]!=-1:
                return sums[i]
            sums[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return sums[i]

        return min(dfs(0),dfs(1))



