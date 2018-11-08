import matplotlib.pyplot as plt
import simpy

from Car import Car
from Constants import Constants
from Arrival import Arrival


env = simpy.Environment()

arrivals = Arrival(env)
env.process(arrivals.generate())
env.run(until=Constants.max_time)


plt.figure(figsize=(5.5, 4))
plt.plot(*zip(*Car.data))
plt.xlabel('Time')
plt.ylabel('Number of cars')
plt.xlim(0, 24)
plt.show()
