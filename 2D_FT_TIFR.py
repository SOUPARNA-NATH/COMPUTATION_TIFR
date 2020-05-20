import numpy.fft as fft
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x_min = float(input("Enter the minimum domain of x: "))
x_max = float(input("Enter the maximum domain of x: "))

y_min = float(input("Enter the minimum domain of y: "))
y_max = float(input("Enter the maximum domain of y: "))

Nx = int(input("Enter the number of x points to be sampled: "))
Ny = int(input("Enter the number of y points to be sampled: "))

Dx = (x_max - x_min)/(Nx-1)
Dy = (y_max - y_min)/(Ny-1)

x = np.linspace(x_min,x_max,Nx,True)
y = np.linspace(y_min,y_max,Ny,True)

#xl = x.tolist()
#yl = y.tolist()


fx = np.exp(-x*x)
fy = np.exp(-y*y)


ar = []

for i in fx:
    arr =[]
    for j in fy:
        arr.append(i*j)
    ar.append(arr)

a = np.array(ar)

k1 = 2*np.pi*fft.fftshift(fft.fftfreq(Nx,Dx))
k2 =2*np.pi*fft.fftshift(fft.fftfreq(Ny,Dy))

f_k = Dx*Dy*np.sqrt(Nx*Ny)/(2*np.pi)*np.exp(-1j*k1*x_min-1j*k2*y_min)*fft.fftshift(fft.fft2(a,norm = "ortho"))

K1,K2 = np.meshgrid(k1,k2)

f_exact = 1/(2*np.pi)*np.exp(-(K1**2+K2**2)/4)

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(K1,K2,abs(f_k),cmap = 'viridis')
plt.title("Numerical")

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(K1,K2,f_exact,cmap = 'viridis')
plt.title("Exact")

plt.show()