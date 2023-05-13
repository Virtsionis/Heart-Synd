import numpy as np
import math


def time_handling(t, nd, n_days, t1, my, sigma, interpolated, t1_we, my_we, sigma_we, interpolated_we):

    # 86400 seconds in a day
    # so here we have seconds in a day * 10
    day = 864000
    sa = 6
    so = 7
    data = np.zeros((t), dtype=None)
    a = np.zeros((n_days), dtype=None)


# where the device start the use to start on day one of the week
    if nd == 0:

        # random normal (normal distribution) defines the starting point of each appliance
        a[nd] = np.random.normal((my+(nd*day)), sigma)
        h = a[nd]
        # h is the starting point
        h = int(h)

        #updated
        for j in range(t1 - 1):
            if h + j > len(data) - 1:
                break
            data[h + j] = interpolated[j]

            # where the device start the use to start on saturday
    elif math.fmod(nd, sa) == 0:
        a[nd] = np.random.normal((my_we+(nd*day)), sigma)
        h = a[nd]
        h = int(h)
        for j in range(t1_we-1):
            data[h+j] = interpolated_we[j]

            # where the device start the use to start on sunday
    elif math.fmod(nd, so) == 0:
        a[nd] = np.random.normal((my_we+(nd*day)), sigma)
        h = a[nd]
        h = int(h)
        for j in range(t1_we-1):
            data[h+j] = interpolated_we[j]

# where the device starts on all the other week days
    else:

        a[nd] = np.random.normal((my+(nd*day)), sigma)
        h = a[nd]
        h = int(h)
        for j in range(t1-1):

            data[h+j] = interpolated[j]

    return data
