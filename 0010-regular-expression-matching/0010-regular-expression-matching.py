class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            matches = i<len(s) and (s[i]==p[j] or p[j]==".")
            if (j+1)<len(p) and p[j+1] == "*":
                cache[(i,j)] = (dfs(i,j+2) or (matches and dfs(i+1, j)))
                return cache[(i,j)]
            if matches:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        return dfs(0,0)

        
        # @lru_cache
        # def dfs(i,j):
        #     if i>= len(s) and j>=len(p):
        #         return True
        #     if j>= len(p):
        #         return False
            
        #     matches = i<len(s) and (s[i]==p[j] or p[j]=='.')
        #     if (j+1)<len(p) and p[j+1]=='*':
        #         return dfs(i,j+2) or (matches and dfs(i+1,j))
        #     if matches:
        #         return dfs(i+1, j+1)

        #     return False

        # return dfs(0,0) 

        
        # i=0
        # j=0
        # if len(s)>len(p):
        #     return False
        # while i<len(s) and j<len(p):
        #     if s[i] == p[j] or p[j]=='.' or p[j] == '*':
        #         i+=1
        #         j+=1
        #     else:
        #         return False
        # return True

            