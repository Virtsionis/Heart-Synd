import numpy as np

def timestamp_func(t):
    timestamp = np.zeros((t), dtype=None)
    for i in range(t-1):
        timestamp[i] = 0 + 0.1*i
        timestamp[i] = timestamp[i].round(2)
    return timestamp
