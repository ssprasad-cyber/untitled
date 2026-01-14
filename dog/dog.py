import time
from dog.states import IDLE

class Dog:
    def __init__(self):
        self.state = IDLE
        self.state_time = time.time()

    def update(self):
        # later: random bark, music trigger, etc.
        pass

