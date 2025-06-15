class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = len(needle)
        if haystack == needle:
            return 0
        if len(needle)==1 and needle in haystack:
            return haystack.index(needle)
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            print(haystack[i:j])
            if haystack[i:j] == needle and j<=len(haystack):
                return i
            j+=1
            
        return -1



        