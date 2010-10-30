#!/usr/bin/python2.7

from math import *
from matplotlib import *
from pylab import *

import numpy as np

print "Hello and welcome to Spencer Krum\'s PlotIt program"
print "Enter a function and we can plot it"

#xs = np.arange(0, 12.3, .00001)
#y = lambda x: x**2

def plotIt(name, xs, y, ylabell="Y values", xlabell="X values"): 
    ys = []
    for i in xs:
        ys.append(y(i))

    ion()
    plot(xs, ys , 'g.')
    ylabel(ylabell)
    xlabel(xlabell)
    grid(True)
    draw()
    hold(False)
    savefig(name)
    raw_input("Press return to quit")


#namezz = "Graph_Output.png"
#plotIt(namezz, xs, y)


