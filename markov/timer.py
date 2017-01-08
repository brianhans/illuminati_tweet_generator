import time

class Timer():

    def __init__(self):
        self.start()

    def start(self):
        """Starts the timer when called"""
        self.start = time.time()

    def current_time(self):
        """Returns the time that has passed since the timer started

        Returns:
        time: double
        """
        if not self.start:
            return 0

        return time.time() - self.start

    def stop(self):
        """Returns the time that has passed since the timer started and stops
        the timer.

        Returns:
        time: double
        """
        current_time = self.current_time()
        self.start = None
        return current_time
