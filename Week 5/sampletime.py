import random

def sample_time(x):
    '''
    Return a random sample time until an event. In the long run, the events will have a rate of events per unit time.

    Preconditions:
    :param x: The desired arrival rate, per unit time.

    Post-conditions:
    :param: none

    :return: A random sample time that obeys a rate x.
    '''
    return random.expovariate(x)