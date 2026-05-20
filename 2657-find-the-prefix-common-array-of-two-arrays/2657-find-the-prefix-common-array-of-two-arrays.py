class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0]*len(A)
        n = len(A)
        adict = defaultdict(list)
        bdict = defaultdict(list)

        for i in range(n):
            adict[i] = A[:i+1]
        
        for i in range(n):
            bdict[i] = B[:i+1]

        # print(adict)
        for i in range(len(A)):
            common = list(set(adict[i]) & set(bdict[i]))
            res[i] = len(common)
        
        return res

