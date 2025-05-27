class MinStack:
    def __init__(self):
        self.stack = []
        self.refStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.refStack:
            self.refStack.append(min(val, self.refStack[-1]))
        else:
            self.refStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.refStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.refStack[-1]

    # O(n)
    # def __init__(self):
    #     self.stack = []
        
    # def push(self, val: int) -> None:
    #     # self.stack.append(val)
    #     lq = deque(self.stack)
    #     lq.appendleft(val)
    #     self.stack = list(lq)        

    # def pop(self) -> None:
    #     del self.stack[0]
    #     print('poped',self.stack)

    # def top(self) -> int:
    #     return self.stack[0]

    # def getMin(self) -> int:
    #     return min(self.stack)
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()