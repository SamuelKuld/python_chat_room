from cProfile import run
import time
import threading


class threader(threading.Thread):
    def __init__(self, name, function, *args):
        threading.Thread.__init__(self)
        self.name = name
        self.function = function
        self.args = args

    def run(self):
        if len(self.args) > 0:
            self.function(self.args)
        else:
            self.function()


def test_function(amount):
    amount = amount[0]
    while amount:
        print(f"Test Thread : {time.time()}")
        time.sleep(1)
        amount -= 1


def test_multithreading():
    test_initial = threader("Test", "test", run_funct=test_function)
    return test_initial
