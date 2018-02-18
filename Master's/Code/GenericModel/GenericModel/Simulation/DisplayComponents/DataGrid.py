import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button
from Simulation.DisplayComponents.DiscreteSlider import DiscreteSlider

class DataGrid(object):
    def __init__(self):
        print("Initializing DataGrid")

    def create_grid(self, maximumRange, run_sim_handle):
        matplotlib.rcParams['figure.figsize'] = (13, 8)

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.10, bottom=0.20)
        
        components_axes = plt.axes([0.25, 0.05, 0.65, 0.03])
        components_slider = DiscreteSlider(components_axes, 'Components count', 1, 10, valinit=4)
        
        p1, = ax.plot(range(maximumRange))
        p2, = ax.plot(range(maximumRange))

        p1.set_ydata(range(maximumRange))
        p2.set_ydata(range(maximumRange))
        fig.canvas.draw_idle()
        components_slider.on_changed(run_sim_handle)

        fig.legend([p1, p2], ['Unprocessed messages', 'Total messages'], loc='upper left')
        plt.show()

    def update_data(self, data):
        pass