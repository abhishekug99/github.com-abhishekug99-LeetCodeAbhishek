class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.iMap = {}
    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        self.iMap[val] = len(self.lst)
        self.lst.append(val)
        return True
        
#pop works inO(1) whely when we do not pass index, else it take O(n)
    def remove(self, val: int) -> bool:
        if val not in self.iMap:
            return False
        i = self.iMap[val]
        endVal = self.lst[-1]
        self.lst[i] = endVal
        self.iMap[endVal] = i
        self.lst.pop()
        del self.iMap[val]
        return True
        
    def getRandom(self) -> int:
        # if self.lst:
        return random.choice(self.lst)
        #     return True
        # elif not self.lst:
        #     return False

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()