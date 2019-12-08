"""This is a program to interpolate given data using various interpolation techniques

Author:- Souparna Nath

Date:- 09/12/2019
"""

from scipy.interpolate import *
from numpy import *
from matplotlib.pyplot import *

f = open('/home/alnath/Desktop/COMPUTATION_TIFR/Interpolation_Data.txt','r')
data = loadtxt('/home/alnath/Desktop/COMPUTATION_TIFR/Interpolation_Data.txt',delimiter = '\t')

x = data[:,0]
y = data[:,1]

f.close()
spl_1 = InterpolatedUnivariateSpline(x,y,k = 1)
spl_2 = InterpolatedUnivariateSpline(x,y,k = 2)
spl_3 = InterpolatedUnivariateSpline(x,y,k = 3)
LagPol = lagrange(x,y)

plot(x,y,marker = 'o', mfc = 'r',mec = 'k', ms = 6)

xp = arange(0,x[len(x)-1],0.01)

xlabel("x", size = 15)
ylabel("y",size = 15)
title("INTERPOLATED CURVES", color = 'b',size = 20)

plot(xp, spl_1(xp),label = "Linear Spline")
plot(xp,spl_2(xp),label = "Quadratic Spline")
plot(xp,spl_3(xp),label = "Cubic Spline")
plot(xp,LagPol(xp),'k-',label = "Lagrange Polynomial")
legend(shadow = True, framealpha = 1.0)
grid(True)
show()
