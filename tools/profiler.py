import time


class SimpleProfiler:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            return 0.0
        return round(time.time() - self.start_time, 3)
