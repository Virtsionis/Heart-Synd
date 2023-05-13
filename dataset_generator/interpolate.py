import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
def interpolate(t, rows, data, x):
    interpolated = np.zeros((t), dtype=None)
    if x==1:
        return interpolated

    else:
        up_factor = t//rows
        for i in range(rows-1):
            diff = ((data[i+1]-data[i])/up_factor)

            for j in range(up_factor-1):
                G = data[i]+j*diff
                interpolated[(((i-1)*up_factor)+j)] = G

    return interpolated
