import time

class Timer():

    def __init__(self):
        self.start()

    def start(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def stop(self):
        return self.current_time()
