class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        track =[]
        
        def backTrack(start,track):
            if len(track)==k and sum(track) == n:
                res.append(track.copy())
                return
            for num in range(start,10):
                track.append(num)
                # copyTrack = track + [num]
                backTrack(num+1, track)
                track.pop()
            
        backTrack(1,track)
        return res
        
            