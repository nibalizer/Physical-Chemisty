#!/usr/bin/python2.7

from math import *
from matplotlib import *
from pylab import *

import numpy as np

#print "Hello and welcome to Spencer Krum\'s Physical Chemistry homework"


def twenty(x):
    y = 33.258*x + -7.5884*(x**2) + 1.0306*(x**3) + -0.058757*(x**4) + -0.0033566*(x**5) + 0.00060696*(x**6)
    return y

def VdW(V, R, T, a, b):
    p = (((R*T) / (V - b)) - (a /(V*V)))
    return p


def RK(V, R, T, A, B):
    p = ((R*T)/(V - B)) - (A / ( sqrt(T) * V * (V + B)))
    return p


#for i in range(10):
#    print twenty(i)


def sixteen_twenty(name):
    a = 9.3919
    b = 0.090494
    A = 183.02
    B = 0.062723
    T = 400
    R = 0.083145
    
    rho = np.arange(0, 12.3, .01)
    P_book = []
    P_rk = []
    P_vdw = []
    for rhos in rho:
        P_book.append(twenty((rhos)))
        P_rk.append(RK((1/rhos), R, T, A, B))

    rho1 = np.arange(0, 10, .01)
    for rhos in rho1:
        P_vdw.append(VdW((rhos**-1), R, T, a, b))

    ion()
    plot(rho, P_book , 'g.')
    plot(rho , P_rk, 'r.')
    plot(rho1, P_vdw , 'b.')
    ylabel('Pressure')
    xlabel('Density')
    grid(True)
    draw()
    hold(False)
    savefig(name)
    raw_input("Press return to quit")


namezz = "lies.png"
sixteen_twenty(namezz)


