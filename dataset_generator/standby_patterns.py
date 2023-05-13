import numpy as np
import interpolate as interpol
import read_csv_data as csv_r


def TV_standby():

    filename = 'TV_STANDBY.csv'
    root_dir = 'data/TV/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    t = np.random.randint(1000, 60000)
    standby = interpol.interpolate(t, n_rows, data, 2)

    return standby, t


def coffeemachine_standby():

    filename = 'Coffee_Machine_STANDBY.csv'
    root_dir = 'data/coffeemachine/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    t = np.random.randint(100, 300)
    standby = interpol.interpolate(t, n_rows, data, 2)

    return standby, t
