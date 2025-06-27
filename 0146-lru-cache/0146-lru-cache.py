class LRUCache:

    def __init__(self, capacity: int):
        self.val = None
        self.next = None
        self.capacity = capacity
        self.cache = {}
        self.LL = []

    def get(self, key: int) -> int:
        if key not in self.LL:
            return -1
        if key in self.LL:
            idx = self.LL.index(key)
            if idx != len(self.LL)-1 :
                self.LL.remove(key)
                self.LL.append(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LL:
            self.LL.remove(key)
        
        elif len(self.LL) == self.capacity:
            rmvKey  = self.LL.pop(0)
            self.cache.pop(rmvKey)

        self.LL.append(key)
        self.cache[key] = value
        

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)