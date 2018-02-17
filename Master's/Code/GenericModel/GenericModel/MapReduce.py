import simpy
import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button
from Simulation.DisplayComponents.DiscreteSlider import DiscreteSlider

def latency(env, latency_duration):
    return env.timeout(latency_duration)

def rand_latency(env, min, max):
    latency_duration = random.randint(min, max)
    return latency(env,latency_duration)

class Monitor(object):
    def __init__(self, env, store, publisher):
        self.env = env
        self.store = store
        self.unprocessed_message_count = []
        self.message_count = []
        self.publisher = publisher

    def start_monitoring(self):
        while True:
            self.unprocessed_message_count.append(len(self.store.items))
            self.message_count.append(len(self.publisher.produced_messages))
            yield self.env.timeout(10)

class Component(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store

    def start_processing_messages(self):
        while True:
            process_duration = 40
            message = self.store.get()
            print('Proccesed %s @ %d ' % (message, self.env.now))
            yield self.env.timeout(process_duration)
            yield rand_latency(self.env, 20,40)

class Publication(object):
    def __init__(self, env, store):
        self.env = env
        self.store = store
        self.produced_messages = []

    def start_publishing(self):
        while True:
            print('Message sent to components %d' % self.env.now)
            self.store.put('msg')
            self.produced_messages.append(len(self.produced_messages) + 1)
            yield rand_latency(self.env, 20,40)

class Receiver(object):
    def __init__(self, env):
        self.env = env

    def start_receiving(self):
        while True:
            print('Message received %d' % self.env.now)
            yield self.env.timeout(30)

matplotlib.rcParams['figure.figsize'] = (13, 8)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.10, bottom=0.20)

components_axes = plt.axes([0.25, 0.05, 0.65, 0.03])
components_slider = DiscreteSlider(components_axes, 'Components count', 1, 10, valinit=4)

p1, = ax.plot(range(1000))
p2, = ax.plot(range(1000))

def run_sim(val):
    env = simpy.Environment()
    store = simpy.Store(env)
    
    publication = Publication(env, store)
    receiver = Receiver(env)

    monitor = Monitor(env, store, publication)
    
    env.process(monitor.start_monitoring())
    
    env.process(publication.start_publishing())
    
    for i in range(int(components_slider.val)):
        env.process(Component(env, store).start_processing_messages())
    env.process(receiver.start_receiving())
    env.run(until=10000)

    p1.set_ydata(monitor.unprocessed_message_count)
    p2.set_ydata(monitor.message_count)
    fig.canvas.draw_idle()

components_slider.on_changed(run_sim)

fig.legend([p1, p2], ['Unprocessed messages', 'Total messages'], loc='upper left')
plt.show()