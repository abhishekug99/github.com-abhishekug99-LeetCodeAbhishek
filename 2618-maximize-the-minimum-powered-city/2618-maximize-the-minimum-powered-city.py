class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        #nlon(n*r)
        n = len(stations)
        diff = [0]*(n+1)
        for i in range(n):
            left = max(i-r, 0)
            right = min(i+r+1, n)
            diff[left] += stations[i]
            diff[right]-=stations[i]

        def canAcheive(targetP):
            currPower = 0
            currK = k
            diffCpy = diff.copy()
            for i in range(n):
                currPower += diffCpy[i]
                if currPower < targetP:
                    additional = targetP - currPower
                    if additional > currK:
                        return False
                    currK -= additional
                    currPower += additional
                    right = min(i + 2*r +1, n)
                    diffCpy[right] -= additional
            return True


        lo, high = min(stations), sum(stations)+k
        res = lo
        # for targetP in reversed(range(lo, high+1)):
        while lo<=high:
            targetP = (lo+high)//2
            if canAcheive(targetP):
                res = targetP
                lo = targetP+1
            else:
                high = targetP-1
        return res

        
        
        
        

