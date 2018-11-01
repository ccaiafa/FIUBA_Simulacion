import random
import simpy
import numpy


client_count = 50
arrival_rate = 30


class Client(object):

    pay_duration = {
        '1': 300,
        '2': 200,
        '3': 100
    }

    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2', '3'], p=[0.6, 0.3, 0.1])

    def pay(self, cashier):
	# Automatic release
        with cashier.request() as req:
            yield req
            yield self.env.timeout(self.get_pay_duration())

	# Manual release
        # request = cashier.request()
        # yield request
        # yield self.env.timeout(self.get_pay_duration())
        # cashier.release(request)

        print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        return self.pay_duration[self.type]


def generate_clients(environment, count, interval):
    cashier = simpy.Resource(env, capacity = 1)
    for i in range(count):
        client = Client(env)
        environment.process(client.pay(cashier))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)


env = simpy.Environment()
env.process(generate_clients(env, client_count, arrival_rate))
env.run()
