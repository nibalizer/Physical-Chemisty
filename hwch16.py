#!/usr/bin/python2.7

from math import *
from matplotlib import *
from pylab import *

import numpy as np

print "Hello and welcome to Spencer Krum\'s Physical Chemistry homework"


def twenty(x):
    y = 33.258*x + -7.5884*(x**2) + 1.0306*(x**3) + -0.058757*(x**4) + -0.0033566*(x**5) + 0.00060696*(x**6)
    return y

def VdW(V, R, T, a, b):
    p = (((R*T) / (V - b)) - (a /(V*V)))
    return p


def RK(V, R, T, A, B):
    p = ((R*T)/(V - B)) - (A / ( sqrt(T) * V * (V + B)))
    return p


def sixteen_fortyseven



#for i in range(10):
#    print twenty(i)

def sixteen_thirtyone(name):
    #const
    R_LBarMolK = 0.083145
    R_LatmmolK = 0.082058

    #ethane
    ethane_p_bar = [.5,2, 10, 20, 40, 60, 80, 100, 120, 160, 200, 240, 300, 350, 400, 450, 500, 600]
    ethane_T = 500
    ethane_Vbar_literpermol = [83.076, 20.723, 4.105, 2.028, 0.9907, 0.6461, 0.4750, 0.3734, 0.3068, 0.2265, 0.1819, 0.1548, 0.1303, 0.1175, 0.1085, 0.1085, 0.1019, 0.09676, 0.08937, 0.08421]
    ethane_Vc = 0.1480
    #calc Z
    ethane_z = []
    ethane_Vr = []
    for i in range(len(ethane_p_bar)):
        ethane_z.append(((ethane_p_bar[i] * ethane_Vbar_literpermol[i] )/(R_LBarMolK * ethane_T ))) 
        ethane_Vr.append(ethane_Vbar_literpermol[i] / ethane_Vc ) 

    #argon
    argon_p_atm = [.5,2, 10, 20, 40, 60, 80, 100, 120, 160, 200, 240, 300, 350, 400, 450, 500, 600]
    argon_T = 247
    argon_Vbar_literpermol = [40.506, 10.106, 1.999, 0.9857, 0.4795, 0.3114, 0.2279, 0.1785, 0.1462, 0.1076, 0.08630, 0.07348, 0.06208, 0.05626, 0.05219, 0.04919, 0.05687, 0.04348, 0.04108]
    argon_Vc = 0.07530

    #calc Z
    argon_z = []
    argon_Vr = []
    for i in range(len(argon_p_atm)):
        argon_z.append(((argon_p_atm[i] * argon_Vbar_literpermol[i] )/(R_LatmmolK * argon_T ))) 
        argon_Vr.append(argon_Vbar_literpermol[i] / argon_Vc ) 
    
    
    ion()
    plot(argon_Vr, argon_z , 'g-', label="Argon")
    plot(ethane_Vr , ethane_z, 'r-', label="Ethane")
    ylabel('Compressibility')
    xlabel('Reduced Molar Volume')
    title("Problem 16.31")
    legend(numpoints=1)
    grid(True)
    draw()
    hold(True)
    savefig(name)
    ioff()
    raw_input("Press return to quit")

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
    plot(rho, P_book , 'g.', label="Experimental")
    plot(rho , P_rk, 'r.', label="Redlich-Kwong")
    plot(rho1, P_vdw , 'b.', label="van der Waals" )
    ylabel('Pressure')
    xlabel('Density')
    legend(numpoints=1)
    title("Problem 16.20")
    grid(True)
    draw()
    hold(True)
    savefig(name)
    ioff()
    raw_input("Press return to quit")


sixteen_thirtyone('Ch16_31.png')
sixteen_twenty('Ch16_20.png')

