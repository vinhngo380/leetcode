class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #list values of val and uses
        #use a stack and pop the lfr for tie breakers?
        self.stack = []
        self.lru = None

    def get(self, key: int) -> int:
        if self.cache[key]:
            self.cache[key][1] += 1
            return self.cache[key][0]
        return -1

        

    def put(self, key: int, value: int) -> None:
        if self.capacity == len(cache):

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#this code is not finished
