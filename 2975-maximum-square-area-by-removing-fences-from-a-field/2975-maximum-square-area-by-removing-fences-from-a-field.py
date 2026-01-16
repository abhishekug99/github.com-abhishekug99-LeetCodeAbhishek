class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9+7
        hFences.sort()
        vFences.sort()

        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        hFences.sort()
        vFences.sort()

        widths = set()
        heights = set()

        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                w =   vFences[j]-vFences[i]
                widths.add(w)
        
        maxSide =0
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                h = hFences[j]-hFences[i]
                if h in widths:
                    maxSide = max(maxSide, h)
        
        return (maxSide**2)%MOD if maxSide else -1
            


