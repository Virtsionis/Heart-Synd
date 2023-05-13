from __future__ import print_function, division
import numpy as np
import pandas as pd
from os.path import *
from os import listdir
from nilmtk.datastore import Key
from nilmtk.measurement import LEVEL_NAMES
from nilmtk.utils import check_directory_exists, get_datastore
from nilm_metadata import convert_yaml_to_hdf5

from datetime import datetime

seconds_per_day = 86400

columnNameMapping = {
    "P": ('power', 'active')
}


def convert_SynD(input_path, output_filename, format='HDF'):

    check_directory_exists(input_path)
    files = [f for f in listdir(input_path) if isfile(join(input_path, f)) and
             '.csv' in f and '.swp' not in f]

    files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    assert isdir(input_path)

    store = get_datastore(output_filename, format, mode='w')
    for i, csv_file in enumerate(files):
        key = Key(building=1, meter=(i + 1))
        print('Loading file #', (i + 1), ' : ', csv_file, '. Please wait...')
        df = pd.read_csv('{}{}'.format(input_path, str(csv_file)), sep='\t', encoding='utf-8', header=None)
        df = df.set_index(df.columns[0], drop=True)
        # df = df.squeeze() to convert DataFrame to Series
        df.columns = ['P']
        df.columns = pd.MultiIndex.from_tuples(
            [columnNameMapping[x] for x in df.columns],
            names=LEVEL_NAMES
        )

        # The CSV Version of SynD has naive timestamps, where we need tz-aware timestamps for NILMTK

        tz_naive = pd.to_datetime(df.index)
        tz_aware = tz_naive.tz_localize(tz='Europe/Vienna', ambiguous=True)
        df.index = tz_aware

        df = df.tz_convert('Europe/Vienna')

        store.put(str(key), df)
        print("Done with file #", (i + 1))

    store.close()

    print('Processing metadata...')
    convert_yaml_to_hdf5('metadata/', output_filename)
