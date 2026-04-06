class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=0
        y=0
        direct = [[0,1],[1,0],[0,-1],[-1,0]] #posible direction N,E,S,W

        d = 0
        res = 0
        obstacles = {tuple(o) for o in obstacles} #set comprehension
        # print(obstacles)
        for c in commands:
            if c==-1:
                d = (d+1)%4 #used mod for not to go outof bound from direction index
            elif c==-2:
                d=(d-1)%4
            else: 
                dx,dy = direct[d] # till here we were tracking the directions
                for _ in range(c): 
                    if (x+dx, y+dy) in obstacles:
                        break
                    x,y = x+dx, y+dy #gives the magnitude
            
            res = max(res,x**2+y**2)



        return res