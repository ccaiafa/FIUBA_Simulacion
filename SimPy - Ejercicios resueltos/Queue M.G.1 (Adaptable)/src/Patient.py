# import numpy
from scipy.stats import erlang

from Constants import Constants


class Patient(object):

    # attention_duration = {
    #     '1': 0.8,
    #     '2': 0.6,
    #     '3': 1
    # }

    def __init__(self, env):
        self.env = env
        # self.type = numpy.random.choice(['1', '2', '3'], p=[0.6, 0.3, 0.1])

    def attend(self, receptionist):
        yield self.env.process(receptionist.attend(self))
        # print("%.2f Patient type %s attended" % (self.env.now, self.type))

    def get_attention_duration(self):
        return erlang.rvs(Constants.phases, scale=float(Constants.time_receptionist) / Constants.phases, size=1)
        # return self.attention_duration[self.type]
