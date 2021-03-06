import random

from Car import Car
from Constants import Constants


class Arrival(object):

    """
        Source generates cars at a time-dependent rate
        Arrivals are at a time-dependent rate
    """

    def __init__(self, env):
        self.env = env

    def generate(self):
        i = 0
        while self.env.now < Constants.max_time:
            t = random.expovariate(Constants.arrival_rate)
            yield self.env.timeout(t)

            time_parking = random.expovariate(Constants.parking_time)
            car = Car(self.env)
            self.env.process(car.visit(time_parking))
            i += 1
