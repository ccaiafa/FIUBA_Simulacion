import simpy
import math
import scipy as sp
import pandas as pd


class MonitoredResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super(MonitoredResource, self).__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append((self._env.now, self.count, len(self.queue)))
        return super(MonitoredResource, self).request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.data.append((self._env.now, self.count, len(self.queue)))
        return super(MonitoredResource, self).release(*args, **kwargs)

    def update_stats(self):
        """ Update statistical counters before calculating summaries

             After completion of simulation, update_stats() prior to calculating
             statistics.
             Returns a panda data frame of delta time, number of active servers,
             and number in queue.
             If pandas is not installed. It will return a list of
             tuples of (elapsed time, active servers, number in queue)
         """
        elapsed_data = [(self.data[i][0] - self.data[i-1][0], self.data[i][1], self.data[i][2])
                        if i > 0 else (self.data[i][0], self.data[i][1], self.data[i][2])
                        for i in range(0, len(self.data))]

        try:
            self.resource_data = pd.DataFrame(self.data, columns=['time', 'servers', 'queue'])
            self.resource_data['system'] = (self.resource_data['servers'] + self.resource_data['queue'])
            self.elapsed_data = pd.DataFrame(elapsed_data, columns=['elapsed_time', 'servers', 'queue'])
            self.elapsed_data['system'] = (self.elapsed_data['servers'] + self.elapsed_data['queue'])
            return self.resource_data
        except:
            return elapsed_data

    def time_average(self, elapsed_time, values):
        return (sp.sum(elapsed_time * values)) / elapsed_time.sum()

    def time_variance(self, elapsed_time, values):
        """ Time weighted unbiased estimator of variance
        """
        weighted_mu = self.time_average(elapsed_time, values)
        V = elapsed_time.sum()
        weight_sum_squared = sum([elapsed_time[i] * math.pow(values[i] - weighted_mu, 2)
                                  for i in range(len(elapsed_time))])
        return weight_sum_squared / (V - 1)

    def act_time_average(self):
        """ Time weighted average of number of servers in use
        """
        return self.time_average(self.elapsed_data['elapsed_time'], self.elapsed_data['servers'])

    def wait_time_average(self):
        """ Time weighted average of number of elements in queue
        """
        return self.time_average(self.elapsed_data['elapsed_time'], self.elapsed_data['queue'])

    def act_time_variance(self):
        """ Time weighted unbiased variance of number of servers in operation
        """
        return self.time_variance(self.elapsed_data['elapsed_time'], self.elapsed_data['servers'])

    def wait_time_variance(self):
        """ Time weighted unbiased variance of number of elements in queue
        """
        return self.time_variance(self.elapsed_data['elapsed_time'], self.elapsed_data['queue'])
