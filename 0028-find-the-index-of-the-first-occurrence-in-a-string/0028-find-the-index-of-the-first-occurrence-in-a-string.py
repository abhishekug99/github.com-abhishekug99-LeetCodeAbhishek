class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or len(needle)>len(haystack):
            return -1
        if needle==haystack :
            return 0

        lps = [0]*len(needle)
        prev = 0
        i=1
        while i < len(needle):
            if needle[i] == needle[prev]:
                prev+=1
                lps[i] = prev
                i+=1
            else:
                if prev!=0:
                    prev = lps[prev-1]
                else:
                    lps[i]=0
                    i+=1
        i=j=0
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j!=0:
                    j = lps[j-1] #fallback
                else:
                    i+=1
            if j == len(needle):
                return i-j
        return -1
                