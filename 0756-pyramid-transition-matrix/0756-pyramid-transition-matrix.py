class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # with memoisation
        substrMap  = defaultdict(list)
        for pattern in allowed:
            substrMap[(pattern[0],pattern[1])].append(pattern[2])
        
        memo = {}

        def dfs(curr, i, above):
            if len(curr)==1:
                return True
            
            if i ==0 and curr in memo:
                return memo[curr]
            
            if i==len(curr)-1:
                res = dfs(above,0,'')
                memo[curr] = res
                return res
            pair = (curr[i], curr[i+1])
            if pair not in substrMap:
                return False
            
            for char in substrMap[pair]:
                if dfs(curr, i+1, above+char):
                    return True
            return False
            
        return dfs(bottom,0,"" )


        #Submitted works well
        # substrMap  = defaultdict(list)
        # for pattern in allowed:
        #     substrMap[(pattern[0],pattern[1])].append(pattern[2])
        
        # def dfs(curr, i, above)->bool:
        #     if len(curr)==1:
        #         return True
        #     if i == len(curr)-1:
        #         return dfs(above, 0, "")
            
        #     pair = (curr[i], curr[i+1])
        #     if pair not in  substrMap:
        #         return False
            
        #     for char in substrMap[pair]:
        #         if dfs(curr, i+1, above + char):
        #             return True
        #         # above = above[:-1]
        #     return False
        
        # return dfs(bottom,0,"" )