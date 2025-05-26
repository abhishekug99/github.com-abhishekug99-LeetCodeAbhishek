class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(ch) for ch in s] ==  [t.index(ch) for ch in t]
        # def transform(string):
        #     iMap = {}
        #     result = []
        #     for i, ch in enumerate(string):
        #         if ch not in iMap:
        #             iMap[ch] = i
        #         result.append(iMap[ch])
        #     return result

        # return transform(s) == transform(t)
        
        
        