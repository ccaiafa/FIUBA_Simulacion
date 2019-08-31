import random

from Arrival import Arrival
from Receptionist import Receptionist


class Hospital(object):

    def __init__(self, env):
        self.env = env
        self.receptionist = Receptionist(env)

    def run(self, aseed):
        random.seed(aseed)
        s = Arrival(self.env, self.receptionist)
        yield self.env.process(s.generate())

    def print_stats(self):
        self.receptionist.print_stats()
