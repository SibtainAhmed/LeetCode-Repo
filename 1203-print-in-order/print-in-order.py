from threading import Semaphore
class Foo:
    def __init__(self):
        self.secondSem = Semaphore(0)
        self.thirdSem = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.secondSem.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.secondSem.acquire()
        printSecond()
        self.thirdSem.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.thirdSem.acquire()
        printThird()
  