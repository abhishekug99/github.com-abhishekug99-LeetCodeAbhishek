class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        n, m = len(robot), len(factory)
        n = len(robot)
        INF = 10**30

        # dp_prev[i] = min distance to repair first i robots
        # using factories processed so far
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0

        for pos, cap in factory:
            # prefix[i] = sum of distances of first i robots to this factory
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + abs(robot[i] - pos)

            dp_new = [INF] * (n + 1)

            # option to skip this factory entirely
            for i in range(n + 1):
                dp_new[i] = dp_prev[i]

            dq = deque()

            for i in range(n + 1):
                # candidate k = i enters the deque
                val = dp_prev[i] - prefix[i]

                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((i, val))

                # keep only k in [i - cap, i]
                while dq and dq[0][0] < i - cap:
                    dq.popleft()

                # use this factory for last segment
                dp_new[i] = min(dp_new[i], prefix[i] + dq[0][1])

            dp_prev = dp_new

        return dp_prev[n]
        
        
        
        # Works but tle
        # @lru_cache
        # def dp(i,j,used):
        #     if i==len(robot):
        #         return 0
        #     if j==len(factory):
        #         return float('inf')
        #     pos,cap = factory[j]
            
        #     res=dp(i,j+1,0)
            
        #     if used<cap:
        #         cost = abs(robot[i]-pos)
        #         res= min(res, cost + dp(i+1,j,used+1))
        #     return res
        
        # return dp(0,0,0)
        


        
        # works but greedy logic fails at 32/40
        # factory.sort()
        # robot.sort()
        # res=0
        # factPoaLimit = {}
        # for fact in factory:
        #     factPoaLimit[fact[0]] = fact[1]
        
        
        # for rPos in robot:
        #     if rPos in factPoaLimit and factPoaLimit[rPos]>0:
        #         factPoaLimit[rPos] -= 1
        #         continue
        #     minDist = float('inf')
        #     chosenFactory = None
        #     for pos,cap in factory:
        #         if factPoaLimit[pos]>0:
        #             dist = abs(pos-rPos)
        #             if dist<minDist:
        #                 minDist=dist    
        #                 chosenFactory=pos 
        #     res+=minDist
        #     factPoaLimit[chosenFactory]-=1
        # return res
