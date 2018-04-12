import time
from builtins import ZeroDivisionError

import schedule

class AverageCPS:

    def __init__(self):
        self.click_per_second = 0

        schedule.every(1).second.do(self._tick)

    def add_click(self):
        self.click_per_second += 1

    def _tick(self):
        print(f"CPS: {self.click_per_second}")
        self.click_per_second = 0
