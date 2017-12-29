import simpy
import matplotlib
from matplotlib import pyplot as plt
import random
from matplotlib.widgets import Slider, Button

from matplotlib.widgets import Slider

class  DiscreteSlider(Slider):
	"""A matplotlib slider widget with discrete steps.
	"""
	def __init__(self, *args, **kwargs):
		"""Identical to Slider.__init__, except for the "increment" kwarg.
		"increment" specifies the step size that the slider will be discretized to."""
		self.inc = kwargs.pop('increment', 1)
		Slider.__init__(self, *args, **kwargs)

	def set_val(self, val):
		xy = self.poly.xy
		xy[2] = val, 1
		xy[3] = val, 0
		self.poly.xy = xy

		self.valtext.set_text('%u' % val)

		if self.drawon:
			self.ax.figure.canvas.draw()
		self.val = int(val)
		if not self.eventson:
			return
		for cid, func in self.observers.items():
			func(val)

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

matplotlib.rcParams['figure.figsize'] = (16, 10)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.10, bottom=0.20)

handlers_axes = plt.axes([0.25, 0.05, 0.65, 0.03])
handlers_slider = DiscreteSlider(handlers_axes, 'Handlers count', 1, 10, valinit=4)

p1, = ax.plot(range(100))
p2, = ax.plot(range(100))

def run_sim(val):
    env = simpy.Environment()
    store = simpy.Store(env)
    
    publication = Publication(env, store)
    receiver = Receiver(env)

    monitor = Monitor(env, store, publication)
    
    env.process(monitor.start_monitoring())
    
    env.process(publication.start_publishing())
    
    for i in range(int(handlers_slider.val)):
        env.process(Component(env, store).start_processing_messages())
    env.process(receiver.start_receiving())
    env.run(until=1000)

    p1.set_ydata(monitor.unprocessed_message_count)
    p2.set_ydata(monitor.message_count)
    fig.canvas.draw_idle()

handlers_slider.on_changed(run_sim)

fig.legend([p1, p2], ['Unprocessed messages', 'Total messages'], loc='upper left')
plt.show()



