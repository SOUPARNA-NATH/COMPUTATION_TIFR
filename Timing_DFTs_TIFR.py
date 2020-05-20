import numpy.fft as fft
import numpy as np
import timeit as time
import matplotlib.pyplot as plt

mysetup1 = '''import numpy as np
N = int(input("Enter the number of points to be sampled: "))'''

mycode1 = '''
arr = []

for i in range(N):
    arr.append(i)

D = (arr[N-1] - arr[0])/(N-1)

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

k_dft = 2*np.pi*frequency/(N*D)

dft = []
fk_p = 0
for q in range(N):
    for p in range (N):
        fk_p += arr[p]*np.exp(-1j*2*np.pi*q*p/N)
    dft.append(1/np.sqrt(N)*fk_p)

DFT = np.array(dft)

f_kdft = D*np.sqrt(N/(2*np.pi))*np.exp(-k_dft*arr[0]*1j)*DFT'''

mysetup2 = '''import numpy as np
import numpy.fft as fft
N = int(input("Enter the number of points to be sampled: "))'''

mycode2 = '''
arr_fft = []

for i in range(N):
    arr_fft.append(i)

D = (arr_fft[N-1] - arr_fft[0])/(N-1)

k_fft = 2*np.pi*fft.fftfreq(N,D)

f_kfft = D*np.sqrt(N/(2*np.pi))*np.exp(-k_fft*arr_fft[0]*1j)*fft.fft(arr_fft,norm = "ortho")
'''

print(time.timeit(stmt = mycode1,setup = mysetup1,number = 100000))
print(time.timeit(stmt = mycode2,setup = mysetup2,number = 100000))

minn = int(input("Enter the minimum value of n to start from: "))
maxx = int(input("Enter the maximum value of n: "))

mysetup3 = mysetup1
mycode3 = mycode1

mysetup4 = mysetup2
mycode4 = mycode2

nt = []
t = []

ntm = []
tm = []

plt.subplot(121)
for i in range(maxx-minn+1):
    nt.append(i)
    t.append(time.timeit(stmt = mycode3,setup = mysetup3,number = 100))

plt.plot(nt,t,'r-')
plt.xlabel("t")
plt.ylabel("n")
plt.title("Self Coded Time Plot")
plt.grid(True)

plt.subplot(122)
for j in range(maxx-minn+1):
    ntm.append(j)
    tm.append(time.timeit(stmt = mycode4,setup = mysetup4,number = 100))

plt.plot(ntm,tm,'r-')
plt.xlabel("n")
plt.ylabel("t")
plt.title("Module Time Plot")
plt.grid(True)

plt.show()