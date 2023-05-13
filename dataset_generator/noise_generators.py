import numpy as np
import random


def AWGN(data_frame):
    return data_frame + np.random.normal(loc=0, scale=np.sqrt(1),size=len(data_frame))


def UncorrelatedUniformNoise(vector):
    return  vector + np.random.uniform(-max(vector),max(vector),len(vector))


def random_samples():
    return 0.0008*np.asarray(random.sample(range(0,1000),100))


def calc_AWGN(vector, SNR_dB):

    target_SNR_db = SNR_dB
    #target_SNR_db = 20

    vector_avg_watts = np.mean(vector)
    vector_agg_db = 10 * np.log10(vector_avg_watts)
    noise_avg_db = vector_agg_db - target_SNR_db
    noise_avg_watts = 10**(noise_avg_db/10)

    noise = np.random.normal(loc=0, scale=np.sqrt(noise_avg_watts),size=len(vector))

    return vector + noise, noise


def Gnoise_func(t, data):
    noise01 = np.zeros((t), dtype=None)
    noise02 = np.zeros((t), dtype=None)
    my = np.mean(data)
    sigma = 0.1
    for i in range(t - 1):


        if data[i] == 0:
            noise02[i] = 0
        else:
            my = data[i]
            noise02[i] = np.random.normal(loc=my, scale=sigma)
        noise01[i] = noise02[i] - data[i]

    x = np.random.randn(2 * t)
    X = np.fft.rfft(x) / t
    X = np.transpose(X)

    for k in range(t - 1):
        noise01[k] += X[k]
        noise02[k] += X[k]

    for j in range(t - 1):
        data[j] = noise02[j]

    return data, noise01
