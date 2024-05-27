class Foo:
    def __init__(self):
        self.firstPass = False
        self.secondPass = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstPass = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not(self.firstPass):
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondPass = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not(self.secondPass):
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()