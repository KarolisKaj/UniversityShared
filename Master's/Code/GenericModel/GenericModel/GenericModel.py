#!/usr/bin/python3
import simpy
import matplotlib
from matplotlib import pyplot as plt

class Component(object):
    def __init__(self, env):
        self.env = env

    def start_processing_messages(env):
        while True:
            print('Proccesed @ %d' % env.now)
            process_duration = 5
            yield env.timeout(process_duration)

class Publication(object):
    def __init__(self, env, component_count):
        self.env = env
        self.component_count = component_count

    def publisher(self):
        while True:
            print('Message sent to components %d' % self.env.now)
            sent_duration = 1
            yield self.env.timeout(sent_duration)


class Receiver(object):
    def __init__(self, env):
        self.env = env

    def start_receiving(env):
        while True:
            print('Message received %d' % env.now)
            received_handle_duration = 3
            yield env.timeout(received_handle_duration)



            #for x in range(self.component_count):
            #    yield self.env.process(component(env))

env = simpy.Environment()
publication = Publication(env,3)
env.process(publication.publisher())
env.run(100)

#p1, = plt.plot(monitor.jobstats)
#p2, = plt.plot(monitor.rejectedstats)
#p3, = plt.plot(monitor.completedstats)
#plt.legend ([p1, p2, p3], ['Jobs in system', 'Rejected jobs', 'Completed jobs'], loc='upper left')
#plt.savefig('results.pdf')
#plt.show()
