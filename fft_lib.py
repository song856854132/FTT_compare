import numpy as np
import math


def signal(N):
    return np.exp(-2j*np.pi/N)

def recursivedft(x,nf=int()):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    # Check the number of sample
    if nf == 0:
        nf = N
    elif N < nf:
        rs = np.zeros(nf-N)
        x = np.concatenate([x,rs])
        nf = len(x)
        N = nf
    else:
        nf = nf
        N = nf

    # Check the number of sample is power of two(2^N)
    power = math.log(nf,2)
    if power.is_integer() == False:
        rpower = round(power)
        nf = 2**rpower
        if N >= nf:
            print("Length of data is not power of two. Its was decreased to %d" % nf)
            x = x[0:nf]
            N = nf
        else:
            print("Length of data is not power of two. Its was increased to %d" % nf)
            res = np.zeros(nf-N)
            x = np.concatenate([x,res])
            N = x.shape[0]
    else:
        nf = int(2**power)
        x = x[0:nf]
        N = nf

    # Recursive of DFT (Cooley-Tukey Algorithm)
    if N <= 32:
        x = np.asarray(x, dtype=float)
        N = x.shape[0]
        n = np.arange(N)
        m = n.reshape((N, 1))
        Y_Cos = np.cos((2*np.pi*m*n/N))
        Y_Sin = np.sin((2*np.pi*m*n/N))
        Y = Y_Cos-(Y_Sin*1j)
        Y = np.dot(Y,x)
        return Y
    else:
        evendata = recursivedft(x[::2])
        odddata = recursivedft(x[1::2])
        fac = signal(N)**(np.arange(N))
        firsthalf = evendata+(fac[:int(N/2)]*odddata)
        secondhalf = evendata+(fac[int(N/2):]*odddata)
        return np.concatenate([firsthalf,secondhalf])

