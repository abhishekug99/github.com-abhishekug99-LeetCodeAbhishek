class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # O(n)
        # def transform(string):
        #     iMap = {}
        #     result = []
        #     for i, ch in enumerate(string):
        #         if ch not in iMap:
        #             iMap[ch] = i
        #         result.append(iMap[ch])
        #     return result
        # return transform(s) == transform(t)

        # High time O(n^2+m^2)
        # return [s.index(ch) for ch in s] ==  [t.index(ch) for ch in t]
        
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))        
        