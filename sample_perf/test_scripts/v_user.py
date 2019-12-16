
import random
import time


class Transaction(object):
    custom_timers = None
    def __init__(self):
        pass

    def run(self):
        r = random.uniform(1, 2)
        time.sleep(r)
        self.custom_timers = r


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print(trans.custom_timers)
