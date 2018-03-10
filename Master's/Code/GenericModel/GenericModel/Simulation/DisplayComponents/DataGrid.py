import matplotlib

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

from Simulation.DisplayComponents.DiscreteSlider import DiscreteSlider

class DataGrid(object):
    def __init__(self):
        print("Initializing DataGrid")
        self.parameters = []
        self.sliders = dict()
        self.next_slider_position = None

    def create_grid(self, data):
        matplotlib.rcParams['figure.figsize'] = (13, 8)

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.05)

        for metric in data:
            p1, = ax.plot(data[metric])
            self.parameters.append(p1) 

        fig.canvas.draw_idle()

        fig.legend(self.parameters, [metric for metric in data], loc='upper left')
        plt.show()

    def update_data(self, data):
        for param, metric in zip(self.parameters, data):
            param.set_ydata(data[metric])

    def add_changeable_slider(name, handle):
        components_axes = plt.axes([0.25, 0.05, 0.65, 0.03])
        
        components_slider = DiscreteSlider(components_axes, name, 1, 10, valinit=4)
        components_slider.on_changed(handle)

        plt.subplots_adjust(left=0.1, bottom=0.20)

        self.sliders[name] = components_slider


