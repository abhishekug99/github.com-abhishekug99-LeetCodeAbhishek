class Solution:
    def longestBalanced(self, s: str) -> int:
        # cnts = Counter(s)
        # print(cnts)
        res = 0
        for i in range(len(s)):
            freq = [0]*26
            maxFreq = 0
            distinct= 0        
            for j in range(i,len(s)):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx]+=1
                maxFreq = max(maxFreq, freq[idx])
                lenght = j-i+1

                if lenght == distinct*maxFreq:
                    res = max(res, lenght)
        return res
        # cnts = {}
        # for i in range(len(s)):
        #     curr =0
        #     for j in range(i, len(s)):
        #         if len(set(Counter(s[i:j+1]).values()))==1:
        #             curr  = (j - i + 1)
        #     res = max(res, curr)
        # return res

        

            