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
        self.fig = None
        self.main_plot_left = 0.1
        self.main_plot_bottom = 0.05
        self.main_plot_left_step = 0.1
        self.main_plot_bottom_step = 0.05

        self.slider_coordinates = [0.25, -0.03, 0.65, 0.03]
        self.slider_coordinates_step = [0, 0.05, 0, 0]


    def create_grid(self, data):
        matplotlib.rcParams['figure.figsize'] = (18, 9)

        fig, ax = plt.subplots()
        self.fig = fig
        plt.subplots_adjust(left=0.25, bottom=0.05)

        for metric in data:
            p1, = ax.plot(data[metric])
            self.parameters.append(p1) 

        fig.canvas.draw_idle()

        fig.legend(self.parameters, [metric for metric in data], loc='upper left')

    def update_data(self, data):
        for param, metric in zip(self.parameters, data):
            param.set_ydata(data[metric])

    def add_changeable_slider(self, name, handle, default_value):
        components_axes = plt.axes(self.calculate_slider_coordinates())
        
        components_slider = DiscreteSlider(components_axes, name, 1, 10, valinit=default_value)
        components_slider.on_changed(handle)
        
        self.main_plot_bottom = self.main_plot_bottom + self.main_plot_bottom_step

        plt.subplots_adjust(left=0.25, bottom=self.main_plot_bottom)

        self.sliders[name] = components_slider

    def calculate_slider_coordinates(self):
        slider_coordinates = []
        for current_coord, step in zip(self.slider_coordinates, self.slider_coordinates_step):
            slider_coordinates.append(current_coord + step)

        self.slider_coordinates = slider_coordinates
        return slider_coordinates
    
    def show_grid(self):
        plt.show()

        





