import numpy.fft as fft
import numpy as np
import matplotlib.pyplot as plt

file = open("Noise.txt","r")
g = np.loadtxt("Noise.txt")
n = len(g)
file.close()

plt.subplot(221)
x = np.arange(0,n,1)
plt.plot(x,g)
plt.title('Noise Plot')
plt.grid(True)

k=fft.fftfreq(n,1)
g_k=fft.fft(g,norm='ortho')

plt.subplot(222)
plt.plot(k,abs(g_k))
plt.title('DFT of Noise')
plt.grid(True)

ps = ((abs(g_k))**2)/n

plt.subplot(223)
plt.plot(k,ps)
plt.title('Power Spectrum')
plt.grid(True)

binn = 10
N_bin = int(n/binn)
k_bin = fft.fftfreq(N_bin,1)

h_k = np.ones(N_bin*binn)
hk = h_k.reshape(binn,N_bin)

s = np.zeros(N_bin)
h = g[0:N_bin*binn].reshape(binn,N_bin)

for i in range(binn):
    hk[i] = abs(fft.fft(h[i],norm='ortho'))
    s += (hk[i])**2/N_bin
sp = s/binn

plt.subplot(224)
plt.plot(k_bin,sp)
plt.title('Binned Power Spectra')
plt.grid(True)

plt.show()
    