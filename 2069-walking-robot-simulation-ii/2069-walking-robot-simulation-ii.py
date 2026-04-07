class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.moved = False
        self.idx = 0
        self.state = []  
        for x in range(width):
            self.state.append([x, 0, 'E'])
        for y in range(1, height):
            self.state.append([width - 1, y, 'N'])
        for x in range(width - 2, -1, -1):
            self.state.append([x, height - 1, 'W'])
        for y in range(height - 2, 0, -1):
            self.state.append([0, y, 'S'])

        self.state[0][2] = 'S'

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.state)

    def getPos(self) -> List[int]:
        x, y, _ = self.state[self.idx]
        return [x, y]

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        _, _, d = self.state[self.idx]
        if d == 'E':   return "East"
        elif d == 'N': return "North"
        elif d == 'W': return "West"
        else:          return "South"

    # Works well but TLE
    # def __init__(self, width: int, height: int):
    #     self.width = width
    #     self.height = height
    #     self.postdir = [[0,0,'E']]
    #     self.movements = [[1,0],[0,1],[-1,0],[0,-1]]

    # def step(self, num: int) -> None:
    #     # x,y, nxtDir = self.postdir[-1]
    #     for _ in range(num):
    #         x,y, nxtDir = self.postdir[-1]
    #         if nxtDir == 'E':
    #             if x>=0 and y>=0 and y+1<self.width:
    #                 # self.postdir.append([x,y+1,'E'])
    #                 self.postdir[0][0] = x
    #                 self.postdir[0][1] = y+1
    #                 self.postdir[0][2] = 'E'
    #             elif x>=0 and y>=0 and y+1>=self.width and x+1<self.height:
    #                 # self.postdir.append([x+1,y,'N'])
    #                 self.postdir[0][0] = x+1
    #                 self.postdir[0][1] = y
    #                 self.postdir[0][2] = 'N'
    #         elif nxtDir == 'N':
    #             if x>=0 and y>=0 and x+1<self.height:
    #                 # self.postdir.append([x+1,y,'N'])
    #                 self.postdir[0][0] = x+1
    #                 self.postdir[0][1] = y
    #                 self.postdir[0][2] = 'N'
    #             elif x>=0 and y>=0 and x+1>=self.height and y-1>=0:
    #                 # self.postdir.append([x,y-1,'W'])
    #                 self.postdir[0][0] = x
    #                 self.postdir[0][1] = y-1
    #                 self.postdir[0][2] = 'W'
    #         elif nxtDir == 'W':
    #             if x>=0 and y>=0 and y-1>=0:
    #                 # self.postdir.append([x,y-1,'W'])
    #                 self.postdir[0][0] = x
    #                 self.postdir[0][1] = y-1
    #                 self.postdir[0][2] = 'W'
    #             elif x>=0 and y>=0 and y==0 and x-1>=0:
    #                 # self.postdir.append([x-1,y,'S'])
    #                 self.postdir[0][0] = x-1
    #                 self.postdir[0][1] = y
    #                 self.postdir[0][2] = 'S'
    #         elif nxtDir == 'S':
    #             if x>=0 and y>=0 and x-1>=0:
    #                 # self.postdir.append([x-1,y,'S'])
    #                 self.postdir[0][0] = x-1
    #                 self.postdir[0][1] = y
    #                 self.postdir[0][2] = 'S'
    #             elif x>=0 and y>=0 and x==0 and y+1<self.width:
    #                 # self.postdir.append([x,y+1,'E'])
    #                 self.postdir[0][0] = x
    #                 self.postdir[0][1] = y+1
    #                 self.postdir[0][2] = 'E'

    # def getPos(self) -> List[int]:
    #     x, y, pos = self.postdir[-1]
    #     return [y,x]

    # def getDir(self) -> str:
    #     x, y, pos = self.postdir[-1]
    #     if pos == 'E':
    #         return "East"
    #     elif pos =='W':
    #         return "West"
    #     elif pos == 'S':
    #         return "South"
    #     else:
    #         return "North"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()