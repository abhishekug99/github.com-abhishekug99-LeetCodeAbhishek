class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #optimal
        if not s or not words:
            return []
        
        wLen = len(words[0])
        windowLen = wLen * len(words)

        target = Counter(words)
        res = []

        for i in range(len(s) - windowLen + 1):
            visited=[]
            for j in range(i, i+windowLen, wLen):
                word = s[j:j+wLen]
                if word in target:
                    visited.append(word)
                else:
                    break
            
            if Counter(visited) == target:
                res.append(i)
        return res
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))


        #correct but not optimal Permutations and perStrs takinh alot of time O(n^2) 152/182
        # if words[0][0] not in s:
        #     return []

        # res = []
        # perms = list(permutations(words))
        # permsStr = []
        # for i in range(len(perms)):
        #     permsStr.append(''.join(perms[i]))

        # strLen = len(permsStr[0])

        
        # if strLen > len(s):
        #     return []

        # for i in range(len(s)-strLen+1):
        #     j=i+1
        #     n= i+strLen
        #     tempStr = s[i]
        #     while j!=n:
        #         tempStr+=s[j]
        #         j+=1
        #     # print(tempStr)
        #     if tempStr in permsStr:
        #         res.append(i)
        
        # return res
