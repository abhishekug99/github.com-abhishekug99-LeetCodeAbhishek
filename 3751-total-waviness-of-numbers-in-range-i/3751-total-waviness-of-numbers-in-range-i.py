class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for n in range(num1, num2+1):
            strn = str(n)
            for i in range(len(strn)-2):
                wv = strn[i:i+3]
                if (wv[1]>wv[0] and wv[1]>wv[2]) or (wv[1]<wv[0] and wv[1]<wv[2]):
                    # print(wv)
                    res+=1
                else:
                    continue
        return res