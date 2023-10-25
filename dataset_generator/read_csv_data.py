import json
from datetime import datetime
import numpy as np
import pandas as pd
import os


def unix_to_date(date, date_format='%Y-%m-%d %H:%M:%S'):
    '''
    converts unix timestamp to normal UTC date time
    date(str or int): the unix timestamp
    date_format(str): the desired format
        e.g:'%Y-%m-%d %H:%M:%S'
    '''
    if date:
        if type(date)!='int':
            date = int(date)
        return datetime.utcfromtimestamp(date).strftime(date_format)
    else:
        return ''


def load_settings(settings_file='settings.json'):
    with open(settings_file) as s_f:
        return json.load(s_f)


def csv_read(filename, root_dir):
    # load settings json

    settings = load_settings('settings.json')
    appliance = settings['appliances'][0]

    filepath = os.path.join(root_dir, filename)
    print(filepath)
    if root_dir == 'data/FRCombo_Heart/':
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp',nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)
    elif root_dir == "data/WM_Heart/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp',nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/FR_Heart/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp',nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/DW_Heart/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp',nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/DR_Heart/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp',nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/AC_Heart/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp', nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/ac/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp', nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/dw/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp', nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/wm/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp', nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    elif root_dir == "data/dryer/":
        n_rows = sum(1 for line in open(filepath)) - 10

        X = pd.read_csv(filepath.format(1), sep=',', index_col='Timestamp', nrows=n_rows,
                        doublequote=True, dtype=None)
        data = np.zeros((X.shape[0], X.shape[1]), dtype=None)

    else:
        if not os.path.isfile(filepath):
            filepath = filepath[:-3]+filepath[-3:].upper()

        n_cols = 1
        n_rows = sum(1 for line in open(filepath))-10
        data = np.zeros((n_rows, n_cols), dtype=None)
        X = pd.read_csv(filepath.format(1), sep=',', header=None, index_col=None, usecols=[2], skiprows=8, nrows=n_rows, doublequote=True, dtype=None)
    X.fillna(value=None, method='ffill')

    X.clip(lower=0)
    data[:,:] = X.values

    return data, n_rows
