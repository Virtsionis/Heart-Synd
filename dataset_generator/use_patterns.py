import numpy as np
import pandas as pd
import os
import interpolate as interpol
import filenames as names
import read_csv_data as csv_r

def coffeemachine_use(var):

    if var == 0:
        filename = 'Coffee_Machine_2_COFFEES.CSV'
        root_dir = 'data/coffeemachine/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

    elif var == 1:
        filename = 'Coffee_Machine_ESSPRESSO.CSV'
        root_dir = 'data/coffeemachine/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

    elif var == 2:
        filename = 'Coffee_Machine_Verlaengerter.CSV'
        root_dir = 'data/coffeemachine/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def printer_use(var):
    x = np.random.randint(1, 3)
    if var == 0:
        filename = 'Printer_US1.CSV'
        root_dir = 'data/printer/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

        t = np.random.randint(1000, 10000)
        use = interpol.interpolate(t, n_rows, data, x)

    else:
        filename = 'Printer_US2.CSV'
        root_dir = 'data/printer/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

        t = np.random.randint(1000, 10000)
        use = interpol.interpolate(t, n_rows, data, x)

    return use, t


def TV_use():

    filename = 'TV_USE.CSV'
    root_dir = 'data/TV/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    t = np.random.randint(20000, 150000)
    use = interpol.interpolate(t, n_rows, data, 2)

    return use, t


def laptop_use():

    filename = 'Laptop_USE.CSV'
    root_dir = 'data/laptop/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    t = np.random.randint(10000, 50000)
    use = interpol.interpolate(t, n_rows, data, 2)

    return use, t


def lamp_use():

    x = np.random.randint(1, 3)
    filename = 'LAMP_USE.CSV'
    root_dir = 'data/lamp/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    t = np.random.randint(10000, 30000)
    use = interpol.interpolate(t, n_rows, data, x)

    return use, t


def gaming_PC_use(var):

    if var == 0:
        filename = 'Gaming_PC_PLAY.CSV'
        root_dir = 'data/gaming_PC/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

        t = np.random.randint(50000, 100000)
        use = interpol.interpolate(t, n_rows, data, 2)

    elif var == 1:
        filename = 'Gaming_PC_USE.CSV'
        root_dir = 'data/gaming_PC/'
        data, n_rows = csv_r.csv_read(filename, root_dir)

        t = np.random.randint(50000, 100000)
        use = interpol.interpolate(t, n_rows, data, 2)

    return use, t


def fridge_use(t):

    filename = 'Fridge_USE.CSV'
    root_dir = 'data/fridge/'
    filepath = os.path.join(root_dir, filename)
    n_cols = 1
    n_rows = sum(1 for line in open(root_dir+filename)) - \
        6934  # has to be skipt to concat patterns clean

    data = np.zeros((n_rows, n_cols), dtype=None)

    X = pd.read_csv(filepath.format(1), sep=',', header=None, index_col=None, usecols=[
                    2], skiprows=6932, nrows=n_rows, doublequote=True, dtype=None)
    X.fillna(value=None, method='ffill')
    X.clip(lower=0)
    data[:, :] = X.values

    interpolated = np.zeros((t), dtype=None)
    up_factor = t//n_rows
    for j in range(up_factor-1):
        for i in range(n_rows-1):
            interpolated[j*n_rows+i] = data[i]
    return interpolated, t


def router_use():

    filename = 'Router_USE.CSV'
    root_dir = 'data/router/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def radio_use():

    filename = 'Radio_USE.CSV'
    root_dir = 'data/radio/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def watercooker_use():

    filename = 'WaterCooker_USE.CSV'
    root_dir = 'data/watercooker/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def monitor_use():
    x = np.random.randint(1, 3)
    filename = 'Monitor_USE.CSV'
    root_dir = 'data/monitor/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    t1 = np.random.randint(12000, 60000)
    interpolated = interpol.interpolate(t1, n_rows, data, x)
    return interpolated, t1


def hairdryer_use():

    filename = 'hairdryer_USE.CSV'
    root_dir = 'data/hairdryer/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def minioven_use():

    filename = 'MINI_OVEN_USE.CSV'
    root_dir = 'data/mini_oven/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def toaster_use(x):

    r = np.random.randint(0, 3)
    filename = names.toaster_use(r)
    root_dir = 'data/toaster/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows


def washingmachine_use(x):
    r = np.random.randint(0, 2)
    filename = names.washingmachine_use(r)
    root_dir = 'data/washingmachine/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows


def dishwasher_use(x):

    r = np.random.randint(0, 3)
    filename = names.dishwasher_use(r)
    root_dir = 'data/dishwasher/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows


def fan_use():

    r = np.random.randint(0, 2)
    filename = names.fan_use(r)
    root_dir = 'data/fan/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def heater_use():

    r = np.random.randint(0, 2)
    filename = names.heater_use(r)
    root_dir = 'data/heater/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def iron_use():

    r = np.random.randint(0, 2)
    filename = names.iron_use(r)
    root_dir = 'data/iron/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def hot_air_gun_use():

    r = np.random.randint(0, 2)
    filename = names.hot_air_gun_use(r)
    root_dir = 'data/hot_air_gun/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def microwave_use():

    r = np.random.randint(0, 3)
    filename = names.microwave_use(r)
    root_dir = 'data/microwave/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows

def WM_Heart_use():

    # r = np.random.randint(0, 12)
    filename = names.WM_Heart_use()
    root_dir = 'data/WM_Heart/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows

def wm_use(x):

    r = np.random.randint(0, 2)
    filename = names.wm_use(r)
    root_dir = 'data/wm/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows

def AC_Heart_use():

    # r = np.random.randint(0, 12)
    filename = names.AC_Heart_use()
    root_dir = 'data/AC_Heart/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows

def ac_use(x):
    r = np.random.randint(0, 9)
    filename = names.ac_use(r)
    root_dir = 'data/ac/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)
    return data, n_rows

def DR_Heart_use():

    # r = np.random.randint(0, 12)
    filename = names.DR_Heart_use()
    root_dir = 'data/DR_Heart/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows

def dryer_use(x):

    r = np.random.randint(0, 3)
    filename = names.dryer_use(r)
    root_dir = 'data/dryer/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows


def DW_Heart_use():

    # r = np.random.randint(0, 12)
    filename = names.DW_Heart_use()
    root_dir = 'data/DW_Heart/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows

def dw_use(x):

    r = np.random.randint(0, 6)
    filename = names.dw_use(r)
    root_dir = 'data/dw/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    if x == 1:
        data = np.zeros((n_rows), dtype=None)

    return data, n_rows


def FR_Heart_use():

    # r = np.random.randint(0, 12)
    filename = names.FR_Heart_use()
    root_dir = 'data/FR_Heart/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows
