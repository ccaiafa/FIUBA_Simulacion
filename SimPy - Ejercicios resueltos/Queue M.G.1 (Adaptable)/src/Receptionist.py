# import numpy
import simpy

from MonitoredResource import MonitoredResource


class Receptionist(object):
    def __init__(self, env, count=1):
        self.env = env

        # Unique queue
        # self.receptionist = simpy.Resource(env, capacity=count)
        self.receptionist = MonitoredResource(env, capacity=count)

        # Separate queue
        # self.receptionist = [simpy.Resource(env) for x in range(count)]

    def attend(self, patient):
        receptionist = self.select_receptionist()
        with receptionist.request() as req:
            yield req
            yield self.env.timeout(patient.get_attention_duration())

    def select_receptionist(self):
        return self.receptionist

        # Smart selection
        # queues = []
        #
        # for x in self.receptionist:
        #     if (x.count == 0) and (len(x.queue) == 0):
        #         return x
        #     else:
        #         queues.append(len(x.queue))
        #
        # return self.receptionist[numpy.array(queues).argmin()]

    def print_stats(self):
        self.receptionist.update_stats()
        print("Average and variance of receptionist use: %5.3f, %5.3f" %
              (self.receptionist.act_time_average(), self.receptionist.act_time_variance()))
        print("Average and variance of receptionist in queue: %5.3f, %5.3f" %
              (self.receptionist.wait_time_average(), self.receptionist.wait_time_variance()))

        # for index, x in enumerate(self.receptionist, start=1):
        #     x.update_stats()
        #     print("Average and variance of receptionist", index, "use: %5.3f, %5.3f" %
        #           (x.act_time_average(), x.act_time_variance()))
        #     print("Average and variance of receptionist", index, "in queue: %5.3f, %5.3f" %
        #           (x.wait_time_average(), x.wait_time_variance()))
