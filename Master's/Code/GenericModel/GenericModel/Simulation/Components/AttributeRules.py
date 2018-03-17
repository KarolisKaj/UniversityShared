import random

from Simulation.Constants.Constants import *

attribute_actions = dict([
    (death_rate, lambda rate: random.random() <= rate),
    (recovery_rate, lambda rate: random.random() <= rate)
    ])
