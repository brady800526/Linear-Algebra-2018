import sys
import numpy as np
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # implement cosine transform
    return np.matmul(np.linalg.inv(B), x)

def InvCosineTrans(a, B):
    # implement inverse cosine transform
    return np.matmul(B, a)

def gen_basis(N):
    B = np.zeros((N, N))
    for n in range(N):
        for k in range(N):
            if k is 0:
                B[n, k] = 1 / np.sqrt(N)
            else:
                B[n, k] = np.sqrt(2/N) * \
                np.cos((n + 0.5) * k * np.pi / N)
    return B

if __name__ == '__main__':
    # Do not modify these 2 lines
    signal_path = sys.argv[1]
    out_directory_path = sys.argv[2]
    
    # Get basis
    x = np.loadtxt(signal_path)
    plot_wave(x)
    B = gen_basis(len(x))

    # Get cosine transformation coefficient
    a = CosineTrans(x, B)

    # Get 5 Max coefficient value
    idxs = np.argsort(a)[-5:][::-1]

    # Get f1 spectrum
    f1 = np.zeros(len(x))
    f1[idxs[0]] = a[idxs[0]]
    f1 = InvCosineTrans(f1, B)

    # Get f3 spectrum
    f3 = np.zeros(len(x))
    f3[idxs[2]] = a[idxs[2]]
    f3 = InvCosineTrans(f3, B)

    # Do not modify these 3 lines
    plot_ak(a, path=os.path.join(out_directory_path, 'freq.png'))
    plot_wave(f1, path=os.path.join(out_directory_path, 'f1.png'))
    plot_wave(f3, path=os.path.join(out_directory_path, 'f3.png'))

