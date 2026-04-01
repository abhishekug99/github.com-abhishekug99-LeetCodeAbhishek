class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)], key=lambda x:x[0])
        stack = []
        alive = [True]*n
        currHealth = healths[:]

        for pos,h,d,idx in robots:
            if d=='R':
                stack.append(idx)
            else:
                while stack and alive[idx]:
                    topIdx = stack[-1]

                    if currHealth[topIdx]<currHealth[idx]:
                        alive[topIdx]=False
                        stack.pop()
                        currHealth[idx]-=1
                    elif currHealth[topIdx]>currHealth[idx]:
                        alive[idx]=False
                        currHealth[topIdx]-=1
                        break
                    else:
                        alive[topIdx]=False
                        alive[idx]=False
                        stack.pop()
                        break
        res=[]
        for i in range(n):
            if alive[i]:
                res.append(currHealth[i])
        return res
             
