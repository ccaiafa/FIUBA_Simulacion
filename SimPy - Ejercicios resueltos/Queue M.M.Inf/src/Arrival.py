import math
import random

from Car import Car
from Constants import Constants


class Arrival(object):

    """
        Source generates cars at random
        Arrivals are at a time-dependent rate
    """

    def __init__(self, env):
        self.env = env

    def generate(self):
        i = 0
        while self.env.now < Constants.max_time:
            t_now = self.env.now
            arrival_rate = 100 + 10 * math.sin(math.pi * t_now/12.0)
            t = random.expovariate(arrival_rate)
            yield self.env.timeout(t)

            time_parking = random.expovariate(1.0/Constants.parking_time)
            car = Car(self.env)
            self.env.process(car.visit(time_parking))
            i += 1
