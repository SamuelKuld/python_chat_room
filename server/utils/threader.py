from cProfile import run
import time
import threading


class threader(threading.Thread):
    def __init__(self, name, function, arguments=None):
        threading.Thread.__init__(self)
        self.name = name
        self.function = function
        self.arguments = arguments

    def run(self):
        self.function(self.arguments)


def test_function(amount):
    amount = amount[0]
    while amount:
        print(f"Test Thread : {time.time()}")
        time.sleep(1)
        amount -= 1


def test_multithreading():
    test_initial = threader("Test", "test", run_funct=test_function)
    return test_initial
