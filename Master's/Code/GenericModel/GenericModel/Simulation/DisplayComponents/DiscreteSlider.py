import simpy
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

class DiscreteSlider(Slider):

    def __init__(self, * args, ** kwargs):
        self.inc = kwargs.pop('increment', 1)
        Slider.__init__(self, * args, ** kwargs)

    def set_val(self, val) :
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