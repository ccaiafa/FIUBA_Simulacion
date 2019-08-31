from scipy.stats import expon

from Patient import Patient
from Constants import Constants


class Arrival(object):

    """
        Source generates patient at random
        Arrivals are at a time-dependent rate
    """

    def __init__(self, env, receptionist):
        self.env = env
        self.receptionist = receptionist

    def generate(self):
        i = 0
        while self.env.now < Constants.max_time:
            t = expon.rvs(0, 1.0 / Constants.ARRint, size=1)
            yield self.env.timeout(t)

            patient = Patient(self.env)
            self.env.process(patient.attend(self.receptionist))
            i += 1
