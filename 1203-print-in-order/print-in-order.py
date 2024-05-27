from threading import Semaphore
class Foo:
    def __init__(self):
        self.secondSem = Semaphore(0)
        self.thirdSem = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.secondSem.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.secondSem.acquire()
        printSecond()
        self.thirdSem.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.thirdSem.acquire()
        printThird()
  