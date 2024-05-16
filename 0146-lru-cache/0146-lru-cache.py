class Node:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    def makeRecent(self, nod):
        prev, nxt = nod.prev, nod.next
        prev.next, nxt.prev = nxt, prev
        # nod.prev.next = nod.next
        # nod.next.prev = nod.prev
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = nod
        nod.next, nod.prev = nxt, prev

        # nod.next = self.right
        # nod.prev = self.right.prev
        # self.right.prev.next = nod
        # self.right.prev = nod
    def removeLastUsed(self):
        key = self.left.next.key
        print('next small: ', self.left.next.next.val)
        next, prev = self.left.next.next, self.left
        # self.left.next = self.left.next.next
        prev.next, next.prev = next, prev
        print('deleting: ',key)
        del self.cache[key]

    def addNode(self,key, val):
        nod = Node(val,key, self.right, self.right.prev)
        self.right.prev.next = nod
        self.right.prev = nod
        self.cache[key] = nod

    def get(self, key: int) -> int:
        if key in self.cache:
            self.makeRecent(self.cache[key])
            print(self.left.next.val)
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.makeRecent(self.cache[key])
        else:
            self.addNode(key,value)
            if len(self.cache) > self.cap:
                self.removeLastUsed()
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)