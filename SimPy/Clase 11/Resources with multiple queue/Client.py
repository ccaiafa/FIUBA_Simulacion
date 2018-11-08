import numpy


class Client(object):

    pay_duration = {
        '1': 300,
        '2': 200,
        '3': 100
    }

    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2', '3'], p=[0.6, 0.3, 0.1])

    def pay(self, checkout):
        yield self.env.process(checkout.serve(self))
        print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        return self.pay_duration[self.type]
