class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                h1bits = bin(h).count('1')
                m1bits = bin(m).count('1')
                if h1bits+m1bits == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res