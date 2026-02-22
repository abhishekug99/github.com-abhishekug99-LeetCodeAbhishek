class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.data = []
        self.idx=0
    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.store[val]=len(self.data)
            self.data.append(val)
        
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.store:
            i = self.store[val]
            end = self.data[-1]
            self.data[i] = end
            self.store[end] = i
            self.data.pop()
            del self.store[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()