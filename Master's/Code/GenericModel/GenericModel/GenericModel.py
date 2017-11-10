import random
from Car import Car
import sys
import os
import simpy


env = simpy.Environment()
car = Car(env)
env.run(50)