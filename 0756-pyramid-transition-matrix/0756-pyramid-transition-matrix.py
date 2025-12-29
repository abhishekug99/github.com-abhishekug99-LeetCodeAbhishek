class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        substrMap  = defaultdict(list)
        for pattern in allowed:
            substrMap[(pattern[0],pattern[1])].append(pattern[2])

        def dfs(curr, i, above)->bool:
            if len(curr)==1:
                return True
            if i == len(curr)-1:
                return dfs(above, 0, "")
            
            pair = (curr[i], curr[i+1])
            if pair not in  substrMap:
                return False
            
            for char in substrMap[pair]:
                if dfs(curr, i+1, above + char):
                    return True
                # above = above[:-1]
            return False
        
        return dfs(bottom,0,"" )