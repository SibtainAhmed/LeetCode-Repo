class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque.append(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque = [value] + self.deque
            return True
        return False

    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque = self.deque[1:]
            return True
        return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[-1]
        return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[0]
        return -1

    def isEmpty(self) -> bool:
        if self.deque:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.deque) == self.size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

[7, 0, 3]