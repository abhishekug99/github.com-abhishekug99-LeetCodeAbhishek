class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cnts = defaultdict(list)
        res = []
        for i in range(len(arr)):
            if arr[i]==0:
                cnts[0].append(0)
            bits = bin(arr[i])[2:]
            ones = bits.count('1')
            if ones:
                cnts[ones].append(arr[i])
        
        for ones in sorted(cnts.keys()):
            cnts[ones].sort()
            res.extend(cnts[ones])

        return res