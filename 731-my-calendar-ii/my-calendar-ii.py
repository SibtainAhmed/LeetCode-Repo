class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, s2: int, e2: int) -> bool:
        for s1,e1 in self.overlap:
            if s2<e1 and s1<e2:
                return False
        for s1,e1 in self.calendar:
            if s2<e1 and s1<e2:
                self.overlap.append([max(s2,s1), min(e2,e1)])
        self.calendar.append([s2,e2])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)