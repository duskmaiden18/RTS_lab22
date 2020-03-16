import math
import matplotlib.pyplot as plt
import random

n = 12
w = 2400
N = 1024

def generate_sygnal():
    harmonics=[]
    for i in range(n):
        A = random.randint(0, 50)
        phi = random.randint(0,4)
        one_harm = []
        for j in range(N):
            x = A * math.sin(((w * (n - i)) / n) * j + phi)
            one_harm.append(x)
        harmonics.append(one_harm)

    harm_sum = []
    for i in range(N):
        sumH = 0
        for j in range(n):
            sumH += harmonics[j][i]
        harm_sum.append(sumH)
    return harm_sum

signal=generate_sygnal()

def fft(signal2):
    NN=int(N/2)-1
    FFT=[]
    for i in range(N):
        real_part1 = 0
        im_part1 = 0
        real_part2 = 0
        im_part2 = 0
        for j in range(NN):
            real_part1 += signal[2*j] * math.cos(4 * math.pi * i * j / N)
            im_part1 += signal[2*j] * math.sin(4 * math.pi * i * j / N)
            real_part2 += signal2[2 * j + 1] * math.cos(4 * math.pi * i * j / N)
            im_part2 += signal[2 * j + 1] * math.sin(4 * math.pi * i * j / N)

        re_p=math.cos(2 * math.pi * i / N)
        im_p=math.sin(2 * math.pi * i / N)
        wP=math.sqrt(math.pow(re_p, 2) + math.pow(im_p, 2))
        if i<NN:
            f_p_real = real_part1 + real_part2 * wP
            f_p_im = im_part1 + im_part2 * wP
            f_p = math.sqrt(math.pow(f_p_real, 2) + math.pow(f_p_im, 2))
        else:
            f_p_real = real_part1 - real_part2 * wP
            f_p_im = im_part1 - im_part2 * wP
            f_p = math.sqrt(math.pow(f_p_real, 2) + math.pow(f_p_im, 2))
        FFT.append(f_p)
    return FFT

fft_new=fft(signal)
plt.plot(list(range(0,N)), fft_new)
plt.title('FFT_new')
plt.grid(True)
plt.show()