class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {'1':'', '2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs','8':'tuv', '9': 'wxyz'}
        nStr = ''
        res = []
        
        if not digits:
            return []
        if len(digits) ==1:
            return list(graph[digits])
        # for num in digits:
        #     nStr += graph[int(num)]
        
        nStrList = list(nStr)
        track = ''
        
        def backTrack(idx,track):
            if len(track) == len(digits):
                res.append(track)
                return 
            
            letters = graph[digits[idx]]
            for l in letters:
                backTrack(idx+1, track+l)
        
        backTrack(0,track)
        return res


        backTrack(nStrList, used, track)
        return res


#lofic for permutation backtracking
        # used = ['' for _ in range(len(nStrList))] for pemutations keep track of repeated, appear only once in given string
        # print(used)
        # res = []
        # track =''
        # def backTrack(nStrList, used, track):
        #     if len(track) == len(digits):
        #         res.append(track)
        #         return
        #     for i in range(len(nStrList)):
        #         if used[i]:
        #             continue
        #         track+=nStrList[i]
        #         used[i] = 1
        #         copyTrack = track
        #         backTrack(nStrList, used, copyTrack)
        #         track = track[:-1]
        #         used[i]=0
        