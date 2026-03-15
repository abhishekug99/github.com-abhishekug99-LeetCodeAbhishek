class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        invMul = pow(self.mul, self.MOD - 2, self.MOD)
        normalized = (val - self.add) % self.MOD
        normalized = (normalized * invMul) % self.MOD
        self.arr.append(normalized)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD

# class Fancy:

#     def __init__(self):
#         self.stack = []
#         self.MOD = 10**9+7

#     def append(self, val: int) -> None:
#         self.stack.append(val)

#     def addAll(self, inc: int) -> None:
#         for i in range(len(self.stack)):
#             self.stack[i]+=inc

#     def multAll(self, m: int) -> None:
#         for i in range(len(self.stack)):
#             self.stack[i]*=m

#     def getIndex(self, idx: int) -> int:
#         return self.stack[idx]%self.MOD if idx < len(self.stack) else -1


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)