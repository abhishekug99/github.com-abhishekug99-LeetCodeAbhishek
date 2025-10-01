class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles == numExchange:
            return numBottles +1
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            newBottles = empty// numExchange
            total+=newBottles
            empty = (empty%numExchange)+newBottles
        return total        