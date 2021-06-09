#!/usr/bin/python3
import math
import matplotlib.pyplot as plt
import numpy as np
import wave
from numpy.core.fromnumeric import size
from scipy.io import wavfile as wv
import sys
from fft_lib import recursivedft
import timeit


def main(file):
    rate, data = wv.read(file)
    length = data.shape[0]/rate
    
    # test the input wav 
    timestamp = np.linspace(0., length, data.shape[0])
    
    plt.plot(timestamp, data[:,0], label="left channel")
    #plt.plot(timestamp, data[:,1], label="right channel")
    """plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('sample')
    plt.show()"""
    # timeit while run FFT
    start = timeit.default_timer()
    X = recursivedft(data[:2**15,0], 2**15)
    stop = timeit.default_timer()

    freq = np.arange(0,2**15)
    plt.plot(freq,np.abs(X),color='blue',label="recursiveDFT")
    plt.ylabel('Magnitude')
    plt.title("Costume FFT")
    plt.legend()
    plt.show()

    print("time = ",stop-start)

if __name__ == '__main__':
    #file = sys.argv[1]
    main("news1.wav")