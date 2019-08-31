import numpy
import simpy


class Checkout(object):
    def __init__(self, env, count):
        self.env = env
        self.count = count
        self.cashiers = [simpy.Resource(env) for x in range(count)]

    def serve(self, client):
        cashier = self.select_cashier()
        with cashier.request() as req:
            yield req
            yield self.env.timeout(client.get_pay_duration())

    def select_cashier(self):
        queues = []

        for x in self.cashiers:
            if (x.count == 0) and (len(x.queue) == 0):
                return x
            else:
                queues.append(len(x.queue))

        return self.cashiers[numpy.array(queues).argmin()]
