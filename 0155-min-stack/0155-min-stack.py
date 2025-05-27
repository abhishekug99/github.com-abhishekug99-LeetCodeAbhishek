class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        # self.stack.append(val)
        lq = deque(self.stack)
        lq.appendleft(val)
        self.stack = list(lq)        

    def pop(self) -> None:
        del self.stack[0]
        print('poped',self.stack)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)
        

[-2,0,-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()