class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = {}
        common = 0
        res = []
        for i in range(n):

            freq[A[i]] = freq.get(A[i], 0) + 1
            if freq[A[i]] == 2:
                common += 1

            freq[B[i]] = freq.get(B[i], 0) + 1
            if freq[B[i]] == 2:
                common += 1
            res.append(common)
        return res

        #submitted but O(n^2)
        # res = [0]*len(A)
        # adict = defaultdict(list)
        # bdict = defaultdict(list)

        # for i in range(n):
        #     adict[i] = A[:i+1]
        
        # for i in range(n):
        #     bdict[i] = B[:i+1]

        # # print(adict)
        # for i in range(len(A)):
        #     common = list(set(adict[i]) & set(bdict[i]))
        #     res[i] = len(common)
        
        # return res

