class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        # print(cnt)
        maxfreq = max(cnts.values())
        res = 0
        for k,v in cnts.items():
            if v == maxfreq:
                res += v 
        
        return res