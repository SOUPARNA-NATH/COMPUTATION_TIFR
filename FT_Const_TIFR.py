
import numpy as np
import matplotlib.pyplot as plt

x_min = float(input("Enter the minimum desired domain of f(x): "))
x_max = float(input("Enter the maximum desired domain of f(x): "))
N = int(input("Enter the number of points to be sampled: "))

D = (x_max - x_min)/(N-1)

x = np.linspace(x_min,x_max,N,True)
f_x = np.ones(N)


freq = []

if(N%2 == 0):
    for i in range(N//2+1):
        freq.append(i)
       
    for j in range(N//2,1,-1):
        freq.append(-j)
else:
    for i in range((N-1)//2+1):
        freq.append(i)
        
    for j in range((N-1)//2+1,1,-1):
        freq.append(-j)

frequency = np.array(freq)

k = 2*np.pi*frequency/(N*D)

dft = []
for q in range(N):
    fk_p = 0
    for p in range (N):
        fk_p += f_x[p]*np.exp(-1j*k[q]*p*D)
    dft.append(1/np.sqrt(N)*fk_p)

DFT = np.array(dft)

f_k = D*np.sqrt(N/(2*np.pi))*np.exp(-k*x_min*1j)*DFT

plt.subplot(121)
plt.plot(x,f_x,'r-')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Original Function")
plt.grid(True)

plt.subplot(122)
plt.plot(k,f_k.real,'b-')
#plt.plot(k,f_k.imag,'k--')
plt.xlabel("k")
plt.ylabel("F(k)")
plt.title("Fourier Transform")
plt.grid(True)

plt.show()