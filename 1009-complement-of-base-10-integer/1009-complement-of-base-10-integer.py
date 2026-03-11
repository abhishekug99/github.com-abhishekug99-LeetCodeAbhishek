class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit = bin(n)[2:]
        res = ['0' if b=='1' else '1' for b in bit]
        return int(''.join(res), 2)