import json
import numpy as np
import pandas as pd
import os, shutil, time, h5py
import matplotlib.pyplot as plt
import plot as plot
import interpolate as interpol
import time_handler as time_handle
import use_patterns as use_pat

def router(t):

        data01, n_rows = use_pat.router_use()

        data = interpol.interpolate(t, n_rows, data01, 2)
        data = np.transpose(data)
        scale_factor = exist_power_factor_noise()
        data = data * scale_factor
        
        return data


def exist_power_factor_noise():
    existence_factor = np.random.normal(0.75, 0.4)
    if existence_factor < 1.2:
        existence_factor = 1
    else:
        existence_factor = 0
    power_level_noise = np.random.normal(1, 0.1)

    if power_level_noise > 1.10:
        power_level_noise = 1.10
    if power_level_noise < 0.9:
        power_level_noise = 0.9
    final_factor = existence_factor * power_level_noise
    return final_factor
