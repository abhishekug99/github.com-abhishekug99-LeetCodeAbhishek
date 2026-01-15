class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxConsecutiveH = 1
        maxConsecutiveV = 1

        currH = 1 
        for i in range(1, len(hBars)):
            if hBars[i]-hBars[i-1]  == 1:
                currH+=1
            else:
                currH =1
            maxConsecutiveH = max(maxConsecutiveH, currH)

        currV = 1 
        for i in range(1, len(vBars)):
            if vBars[i]-vBars[i-1]  == 1:
                currV+=1
            else:
                currV =1
            maxConsecutiveV = max(maxConsecutiveV, currV)

        side = min(maxConsecutiveV, maxConsecutiveH) +1
        return side*side