class MyCalendar:

    def __init__(self):
      self.startArr = []
      self.endArr = []  

    def book(self, start: int, end: int) -> bool:
        for s,e in zip(self.startArr, self.endArr):
            if start < e and s < end:
                return False 
        self.startArr.append(start)
        self.endArr.append(end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)