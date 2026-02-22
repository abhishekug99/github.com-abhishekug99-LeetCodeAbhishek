class Solution:
    def binaryGap(self, n: int) -> int:
        bits = bin(n)[2:]
        prev = -1
        res = 0

        for i in range(len(bits)):
            if bits[i] == '1':
                if prev != -1:
                    res = max(res, i - prev)
                prev = i

        return res