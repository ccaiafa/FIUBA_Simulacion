import random

from Arrival import Arrival


class Parking(object):

    def __init__(self, env):
        self.env = env

    def run(self, aseed):
        random.seed(aseed)
        s = Arrival(self.env)
        yield self.env.process(s.generate())
