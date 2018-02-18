import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button
from Simulation.DisplayComponents.DiscreteSlider import DiscreteSlider

class DataGrid(object):
    def __init__(self, run_sim_handle):
        print("Initializing DataGrid")
        self.parameters = []
        self.run_sim_handle = run_sim_handle;

    def create_grid(self, maximumRange, parameter_names):
        matplotlib.rcParams['figure.figsize'] = (13, 8)

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.05)

        for _ in parameter_names:
            p1, = ax.plot(range(maximumRange))
            self.parameters.append(p1) 

        fig.canvas.draw_idle()

        fig.legend(self.parameters, parameter_names, loc='upper left')
        plt.show()

    def update_data(self, data):
        for i in range(data.Count()):
            self.parameters[i].set_ydata(data[i])

    def add_changeable_sliders():
        components_axes = plt.axes([0.25, 0.05, 0.65, 0.03])
        
        components_slider = DiscreteSlider(components_axes, 'Components count', 1, 10, valinit=4)
        components_slider.on_changed(self.run_sim_handle)

        plt.subplots_adjust(left=0.1, bottom=0.20)


