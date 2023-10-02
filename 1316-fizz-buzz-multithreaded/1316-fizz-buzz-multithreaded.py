from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.sema5 = Semaphore(0)
        self.sema3 = Semaphore(0)
        self.sema15 = Semaphore(0)
        self.sema = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while True:
            self.sema3.acquire()
            if self.done:
                break
            printFizz()
            self.sema.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            self.sema5.acquire()
            if self.done:
                break
            printBuzz()
            self.sema.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.sema15.acquire()
            if self.done:
                break
            printFizzBuzz()
            self.sema.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for n in range(1, self.n + 1):
            self.sema.acquire()
            if n % 15 == 0:
                self.sema15.release()
            elif n % 3 == 0:
                self.sema3.release()
            elif n % 5 == 0:
                self.sema5.release()
            else:
                printNumber(n)
                self.sema.release()
        self.sema.acquire()
        self.done = True
        self.sema3.release()
        self.sema5.release()
        self.sema15.release()
        