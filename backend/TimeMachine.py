from time import time


class TimeMachine:
    def __init__(self):
        self.times = []
        self.names = []

    def start(self):
        self.st = time()

    def measure(self, name):
        self.times.append(time() - self.st - sum(self.times))
        self.names.append(name)

    def duration(self):
        return self.times[-1] - self.st

    def __str__(self):
        return ", ".join(name + ": " + ("%.02f" % time) for (name, time) in zip(self.names, self.times)) \
            + ", TOTAL: " + ("%.02f" % sum(self.times))
