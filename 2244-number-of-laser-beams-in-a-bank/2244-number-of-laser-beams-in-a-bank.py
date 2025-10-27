class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        n = len(bank)

        for i in range(n-1):
            if '1' in bank[i]:
                cnti = Counter(bank[i])
                for j in range(i+1, n):
                    if '1' not in bank[j]:
                        continue
                    else:
                        cntj = Counter(bank[j])
                        # print(cntj)
                        res += cntj['1']*cnti['1']
                        break
        return res
