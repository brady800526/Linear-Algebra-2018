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
    n = len(N)
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j is 0:
                B[i, j] = 1 / np.sqrt(n)
            else:
                B[i, j] = (np.sqrt(2) / np.sqrt(n)) * \
                np.cos(((i + 0.5) * j * np.pi / n))
    return B

if __name__ == '__main__':
    # Do not modify these 2 lines
    signal_path = sys.argv[1]
    out_directory_path = sys.argv[2]
    
    # Get basis
    x = np.loadtxt(signal_path)
    plot_wave(x)
    B = gen_basis(x)

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
    f3[idxs[2]] = 1
    f3 = InvCosineTrans(f3, B)

    # Do not modify these 3 lines
    plot_ak(a, path=os.path.join(out_directory_path, 'freq.png'))
    plot_wave(f1, path=os.path.join(out_directory_path, 'f1.png'))
    plot_wave(f3, path=os.path.join(out_directory_path, 'f3.png'))

