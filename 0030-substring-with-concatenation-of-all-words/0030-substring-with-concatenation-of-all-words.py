class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words[0][0] not in s:
            return []
            
        res = []
        perms = list(permutations(words))
        permsStr = []
        for i in range(len(perms)):
            permsStr.append(''.join(perms[i]))

        strLen = len(permsStr[0])

        
        if strLen > len(s):
            return []

        for i in range(len(s)-strLen+1):
            j=i+1
            n= i+strLen
            tempStr = s[i]
            while j!=n:
                tempStr+=s[j]
                j+=1
            # print(tempStr)
            if tempStr in permsStr:
                res.append(i)
        
        return res
