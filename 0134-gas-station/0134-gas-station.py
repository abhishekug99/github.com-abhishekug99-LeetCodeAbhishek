class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fuel = price = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            fuel+=gas[i]
            price+=cost[i]
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank = 0
        if fuel<price:
            return -1
        return start