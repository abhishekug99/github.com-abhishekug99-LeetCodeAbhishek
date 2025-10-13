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
        