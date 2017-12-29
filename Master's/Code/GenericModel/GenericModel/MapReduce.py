import simpy
import matplotlib
from matplotlib import pyplot as plt
import random

def latency(env, latency_duration):
    return env.timeout(latency_duration)

def rand_latency(env, min, max):
    latency_duration = random.randint(min, max)
    return latency(env,latency_duration)

class Monitor(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store
        self.message_count = []

    def start_monitoring(self):
        while True:
            self.message_count.append(len(self.store.items))
            yield env.timeout(10)

class Component(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store

    def start_processing_messages(self):
        while True:
            process_duration = 40
            message = store.get()
            print('Proccesed %s @ %d ' % (message, env.now))
            yield env.timeout(process_duration)
            yield rand_latency(env, 20,40)

class Publication(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store

    def start_publishing(self):
        while True:
            print('Message sent to components %d' % env.now)
            store.put('msg')
            yield rand_latency(env, 20,40)

class Receiver(object):
    def __init__(self, env):
        self.env = env

    def start_receiving(self):
        while True:
            print('Message received %d' % env.now)
            yield env.timeout(30)

env = simpy.Environment()
store = simpy.Store(env)
monitor = Monitor(env, store)

publication = Publication(env, store)
receiver = Receiver(env)

env.process(monitor.start_monitoring())

env.process(publication.start_publishing())
for i in range(1):
    env.process(Component(env, store).start_processing_messages())
env.process(receiver.start_receiving())

env.run(until=10000)

p1, = plt.plot(monitor.message_count)
plt.legend([p1], ['Unprocessed messages'], loc='upper left')

plt.show()
