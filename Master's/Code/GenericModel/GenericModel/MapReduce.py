import simpy
import matplotlib
from matplotlib import pyplot as plt

class Monitor(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store
        self.message_count = []

    def start_monitoring(self):
        while True:
            self.message_count.append(len(self.store.items))
            yield env.timeout(1)

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

env = simpy.Environment()
store = simpy.Store(env)
monitor = Monitor(env, store)

publication = Publication(env, store)
receiver = Receiver(env)

env.process(monitor.start_monitoring())

env.process(publication.start_publishing())
for i in range(3):
    env.process(Component(env, store).start_processing_messages())
env.process(receiver.start_receiving())

env.run(until=100)

p1, = plt.plot(monitor.message_count)
plt.legend ([p1], ['Unprocessed messages'], loc='upper left')

plt.show()


#p1, = plt.plot(monitor.jobstats)
#p2, = plt.plot(monitor.rejectedstats)
#p3, = plt.plot(monitor.completedstats)
#plt.legend ([p1, p2, p3], ['Jobs in system', 'Rejected jobs', 'Completed jobs'], loc='upper left')
#plt.savefig('results.pdf')
#plt.show()
