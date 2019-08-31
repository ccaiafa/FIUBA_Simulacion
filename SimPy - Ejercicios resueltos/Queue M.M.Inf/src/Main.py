import matplotlib.pyplot as plt
import simpy

from Car import Car
from Constants import Constants
from Parking import Parking


env = simpy.Environment()

parking = Parking(env)
env.process(parking.run(Constants.a_seed))
env.run(until=Constants.max_time)


plt.figure(figsize=(5.5, 4))
plt.plot(*zip(*Car.data))
plt.xlabel('Time')
plt.ylabel('Number of cars')
plt.xlim(0, 24)
plt.show()
