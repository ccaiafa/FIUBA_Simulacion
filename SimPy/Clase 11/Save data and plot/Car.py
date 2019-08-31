

class Car(object):
    """
        Cars arrives, parks for a while, and leaves
        Maintain a count of the number of parked cars as cars arrive and leave
    """

    parked_cars = 0
    data = []

    def __init__(self, env):
        self.env = env

    def visit(self, time_parking):
        Car.parked_cars += 1
        Car.data.append((self.env.now, Car.parked_cars))

        yield self.env.timeout(time_parking)

        Car.parked_cars -= 1
        Car.data.append((self.env.now, Car.parked_cars))
