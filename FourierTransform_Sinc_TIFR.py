import numpy.fft as fft
import numpy as np
import matplotlib.pyplot as plt

x_min = float(input("Enter the minimum desired domain of f(x): "))
x_max = float(input("Enter the maximum desired domain of f(x): "))
N = int(input("Enter the number of points to be sampled: "))

D = (x_max - x_min)/(N-1)


x1 = np.linspace(x_min,x_max,N,True)
f_x1 = np.sin(x1)/x1

x2 = x1.tolist()
f_x2 = f_x1.tolist()

if (0.0 in x2):
    f_x3 = f_x2[0:x2.index(0.0)]+ [1.0]+ f_x2[x2.index(0.0)+1:len(x2)]
    f_x = np.array(f_x3)
else:
    f_x = np.array(f_x2)

x = np.array(x2)

k = 2*np.pi*fft.fftfreq(N,D)
f_k = D*np.sqrt(N/(2*np.pi))*np.exp(-k*x_min*1j)*fft.fft(f_x,norm = "ortho")

plt.subplot(121)
plt.plot(x,f_x,'r-')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Original Function")
plt.grid(True)

plt.subplot(122)
plt.plot(k,abs(f_k),'b-')
#plt.plot(k,f_k.imag,'k--')
plt.xlabel("k")
plt.ylabel("F(k)")
plt.title("Fourier Transform")
plt.grid(True)

plt.show()