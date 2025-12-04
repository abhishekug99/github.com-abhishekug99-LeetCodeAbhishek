class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        i=0
        j=len(directions)-1
        while i<len(directions) and directions[i]=='L':
            i+=1

        while j>=0 and directions[j]=='R':
            j-=1

        for d in range(i, j+1):
            if directions[d] != 'S':
                res+=1
        
        return res
        