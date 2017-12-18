#!/usr/bin/python3
import simpy
import matplotlib
from matplotlib import pyplot as plt

class Component(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store

    def start_processing_messages(self):
        while True:
            process_duration = 5
            message = store.get()
            print('Proccesed %s @ %d ' % (message, env.now))
            yield env.timeout(process_duration)

class Publication(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store

    def start_publishing(self):
        while True:
            print('Message sent to components %d' % self.env.now)
            sent_duration = 1
            yield self.env.timeout(sent_duration)
            yield store.put('msg')

class Receiver(object):
    def __init__(self, env):
        self.env = env

    def start_receiving(self):
        while True:
            print('Message received %d' % self.env.now)
            received_handle_duration = 3
            yield env.timeout(received_handle_duration)

env = simpy.Environment(100)
store = simpy.Store(env)

publication = Publication(env, store)
component1 = Component(env, store)
component2 = Component(env, store)
component3 = Component(env, store)
component4 = Component(env, store)
component5 = Component(env, store)
component6 = Component(env, store)
receiver = Receiver(env)

env.process(publication.start_publishing())
env.process(component1.start_processing_messages())
env.process(component2.start_processing_messages())
env.process(component3.start_processing_messages())
env.process(component4.start_processing_messages())
env.process(component5.start_processing_messages())
env.process(component6.start_processing_messages())
env.process(receiver.start_receiving())

env.run(until=500)


print('%s' % store.items)

#p1, = plt.plot(monitor.jobstats)
#p2, = plt.plot(monitor.rejectedstats)
#p3, = plt.plot(monitor.completedstats)
#plt.legend ([p1, p2, p3], ['Jobs in system', 'Rejected jobs', 'Completed jobs'], loc='upper left')
#plt.savefig('results.pdf')
#plt.show()
