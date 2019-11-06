"""
This is a program to plot the CMB Monopole spectrum using the COBE Data
and hence to compare its nature with the CMB BlackBody Spectrum, that will 
finally lead us to the 2020 Nobel Prize :P 

Author: Souparna Nath

Date: 05.11.2019
"""

import matplotlib.pyplot as plt
import numpy as np



h =  6.626*10**(-34) #Planck's Constant
c = 3*(10**8) #Speed of Light
KB = 1.38*(10**(-23)) #Boltzmann Constant

#Plotting the Theoretical BlackBody Curve
nu = np.arange(200,2500,0.1)

u = ((2*h*c*nu**3) * 1/(np.exp(h*c*nu/(KB*2.725))-1))
plt.plot(nu,u,'r-',label = "THEORETICAL CURVE")

#Now Plotting the data from COBE
f = open("/home/alnath/Desktop/PYTHON PROGRAM/CMBMonopole.txt","r")

freq = np.loadtxt("/home/alnath/Desktop/PYTHON PROGRAM/CMBMonopole.txt")
frequency = 100*freq[:,0]   #Converting cm^(-1) to m^(-1)
cmb_fl = np.loadtxt("/home/alnath/Desktop/PYTHON PROGRAM/CMBMonopole.txt")
cmb_flux = 10**-20*cmb_fl[:,1]  #Converting MJy/sr to J/m^2

f.close()

#Designing Plot Window
plt.plot(frequency,cmb_flux,'b+',markersize = 20,label = "EXPERIMENTAL DATA")
plt.title("COBE DATA COMPARISON WITH THEORETICAL BLACK BODY SPECTRUM",color = 'k')
plt.xlabel(r"$\bar{\nu}$")
plt.ylabel("CMB_Flux "+r"$(\frac{J}{m^2})$")
plt.legend(loc = 'best',framealpha = 1.0,shadow = True)
plt.grid(True)

plt.show()