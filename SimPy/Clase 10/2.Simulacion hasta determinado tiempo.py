import simpy

simulation_time = 100


def car(env):
    index = 1
    while True:
        print('Car %d' % index)

        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

        index = index + 1


environment = simpy.Environment()
environment.process(car(environment))
environment.run(until=simulation_time)
