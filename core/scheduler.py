import time
import random


class Scheduler:
    def __init__(self):
        self.min_idle_sleep = 5
        self.tasks = [
            {"type": "planning"},
            {"type": "research"},
            {"type": "experiment"},
            {"type": "evaluation"},
            {"type": "reflection"},
        ]

    def next_task(self):
        time.sleep(random.randint(1, 3))
        return random.choice(self.tasks)
