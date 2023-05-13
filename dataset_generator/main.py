import glob, gc
import yaml
from datetime import datetime
from periodical import fridge
from always_on import router
from single_pattern import *
from on_off_pattern import *
from multi_pattern import *
from HDF5_converter import convert_SynD
import json
import os
import pandas as pd
import shutil

samples_per_day = 864000
log_file = 'synd_log.txt'

appID = {
    # SMART METER SIGNAL
    "aggregate": 1,

    # PERIODICAL APPLIANCES
    "fridge": 2,

    # MULTI PATTERN APPLIANCES
    "dishwasher": 3,
    "heater": 4,
    "washing machine": 5,
    "toaster": 6,
    "fan": 7,
    "microwave": 8,
    "iron": 9,
    "hot air gun": 10,

    # ALWAYS ON
    "router": 11,

    # ON-OFF APPLIANCES
    "coffee machine": 12,
    "TV": 13,

    "printer": 14,
    "laptop": 15,
    "lamp": 16,
    "gaming PC": 17,

    # SINGLE PATTERN
    "radio": 18,
    "monitor": 19,
    "minioven": 20,
    "hair dryer": 21,
    "watercooker": 22,

    # HEART SINGLE TRACE
    "ilias data": 23,
    "WM_Heart": 24,
    "AC_Heart": 25,
    "DR_Heart": 26,
    "DW_Heart": 27,
    "FR_Heart": 28,
    "FRCombo_Heart": 29,

    # HEART MULTI TRACES
    "ac": 30,
    "dryer": 31,
    "wm":32,
    "dw":33
}

# all devices for settings json
all_appliances = ["fridge", "wm", "dishwasher", "heater", "dryer",  "washing machine", "toaster", "dw", "microwave", "iron",
                  "hot air gun", "ac",  "router", \
                  "coffee machine", "TV", "printer", "laptop", "lamp", "gaming PC", "radio", "monitor", "minioven", \
                  "hair dryer", "watercooker", "WM_Heart", "AC_Heart", "DR_Heart", "DW_Heart", "FR_Heart"]

noise8_1 = ["heater", "toaster", "fridge", "minioven", "hair dryer", "watercooker"]
noise8_2 = ["fridge", "dishwasher", "heater", "washing machine", "toaster", "fan"]
noise8_3 = ["iron", "radio", "monitor", "watercooker", "lamp", "printer"]
noise8_4 = ["heater", "toaster",  "watercooker", "lamp", "fan", "router"]
noise8_5 = ["DR_Heart", "heater", "printer", "lamp", "gaming PC", "monitor"]
noise8_6 = ["hot air gun", "router", "coffee machine", "TV" ,"printer", "gaming PC"]
noise8_7 = ["AC_Heart", "monitor", "minioven", "TV", "printer", "laptop"]
noise8_8 = ["hair dryer", "watercooker", "toaster", "fan", "microwave", "iron"]
noise8_9 = ["lamp", "gaming PC", "radio", "hair dryer", "watercooker", "toaster"]
noise8_10 = ["iron", "hot air gun", "router", "lamp", "gaming PC", "radio"]

noise10_1 = ["heater", "toaster", "fridge", "minioven", "hair dryer", "watercooker", "lamp", "printer"]
noise10_2 = ["fridge", "dishwasher", "heater", "washing machine", "toaster", "fan", "minioven", "iron"]
noise10_3 = ["iron", "hot air gun", "router", "lamp", "gaming PC", "radio", "printer", "fan"]
noise10_4 = ["AC_Heart", "monitor", "minioven", "TV", "printer", "laptop", "gaming PC", "radio"]
noise10_5 = ["DR_Heart", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "gaming PC"]
noise10_6 = ["heater", "toaster",  "watercooker", "lamp", "fan", "router", "minioven", "hair dryer"]
noise10_7 = ["iron", "radio", "monitor", "watercooker", "lamp", "printer", "hot air gun", "FR_Heart"]
noise10_8 = ["fridge", "dishwasher", "heater", "washing machine", "minioven", "hair dryer", "watercooker", "toaster"]
noise10_9 = ["toaster", "fan", "microwave", "iron", "hot air gun", "router", "coffee machine", "TV"]
noise10_10 = ["printer", "laptop", "iron", "hot air gun", "router", "lamp", "gaming PC", "radio"]

noise12_1 = ["toaster", "fan", "microwave", "iron", "hot air gun", "gaming PC", "coffee machine", "TV", "printer", "laptop"]
noise12_2 = ["FR_Heart", "fan", "microwave", "iron", "hot air gun", "radio", "coffee machine", "TV", "printer", "laptop"]
noise12_3 = ["FR_Heart", "fan", "microwave", "iron", "hot air gun", "lamp", "coffee machine", "TV", "printer", "laptop"]
noise12_4 = ["DR_Heart", "fan", "microwave", "iron", "hot air gun", "fridge", "coffee machine", "TV", "printer", "laptop"]
noise12_5 = ["WM_Heart", "fan", "microwave", "iron", "hot air gun", "fridge", "coffee machine", "TV", "printer", "laptop"]
noise12_6 = ["AC_Heart", "fan", "microwave", "iron", "hot air gun", "FR_Heart", "coffee machine", "TV", "printer", "laptop"]
noise12_7 = ["fridge", "fan", "microwave", "iron", "hot air gun", "router", "coffee machine", "TV", "printer", "laptop"]

# filename = [filename_din, filename_device1, filename_device2]

#8
filename1 = ['9574384526955649793', '9574384527220941023', '9574384527220936278']
HERON1 = ["ac", "dw", "heater", "toaster", "fridge", "minioven", "hair dryer", "watercooker"]

#8
filename2 = ['9574384526955649798', '9574384527220936308', '9574384527220936121']
HERON2 = ['wm', 'TV', "fridge", "dishwasher", "heater", "washing machine", "toaster", "fan"]

#8
filename3 = ['9574384526955649774', '9574384527220941059', '9574384527220936275']
HERON3 = ['wm', 'ac', "iron", "radio", "monitor", "watercooker", "lamp", "printer"]

#8
filename4 = ['9574384526955649776', '9574384527220941042', '9574384527220936272']
HERON4 = ["ac", "wm", "heater", "toaster",  "watercooker", "lamp", "fan", "router"]

#8
filename5 = ['9574384526955649783', '9574384527220936130', '9574384527220936233']
HERON5 = ["dw", "wm", "DR_Heart", "heater", "printer", "lamp", "gaming PC", "monitor"]

#8
filename6 = ['9574384526955649786', '9574384527220934215', '9574384527220936279']
HERON6 = ['ac', 'wm', "hot air gun", "router", "coffee machine", "TV" ,"printer", "gaming PC"]

#8
filename7 = ['9574384526955649778', '9574384527220934118', '9574384527220936147']
HERON7 = ['dw', 'wm', "AC_Heart", "monitor", "minioven", "TV", "printer", "laptop"]

#8
filename8 = ['9574384526955649771', '9574384527220941028', '9574384527220936014']
HERON8 = ['TV', 'dw', "hair dryer", "watercooker", "toaster", "fan", "microwave", "iron"]

#8
filename9 = ['9574384526955649726', '9574384527220941058', '9574384527220936273']
HERON9 = ['ac', 'TV', "lamp", "gaming PC", "radio", "hair dryer", "watercooker", "toaster"]

#8
filename10 = ['9574384526955649730', '9574384527220941039', '9574384527220936274']
HERON10 = ['ac', 'wm', "iron", "hot air gun", "router", "lamp", "gaming PC", "radio"]

#10
filename11 = ['9574384526955649733', '9574384527220936267', '9574384527220935031']
HERON11 = ['ac', 'wm', "heater", "toaster", "fridge", "minioven", "hair dryer", "watercooker", "lamp", "printer"]

#10
filename12 = ['9574384526955649799', '9574384527220936265', '9574384527220934214']
HERON12 = ['ac', 'wm', "fridge", "dishwasher", "heater", "washing machine", "toaster", "fan", "minioven", "iron"]

#10
filename13 = ['9574384526955649789', '9574384527220941139', '9574384527220936133']
HERON13 = ['TV', 'wm', "iron", "hot air gun", "router", "lamp", "gaming PC", "radio", "printer", "fan"]

#10
filename14 = ['9574384526955649766', '9574384527220934984', '9574384527220936037']
HERON14 = ['ac', 'dw', "fridge", "toaster", "router", "lamp", "gaming PC", "radio", "printer", "fan"]

#10
filename15 = ['9574384526955649729', '9574384527220934034', '9574384527220936119']
HERON15 = ['ac', 'ac', "DR_Heart", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan"]

#10
filename38 = ['9574384526955649737', '9574384527220934791', '9574384527220934070']
HERON38 = ['ac', 'dryer', "wm", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan"]

#10
filename29 = ['9574384526955649764', '9574384527220934489', '9574384527220936010']
HERON29 = ["gaming PC", 'dw', "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan", "hair dryer"]

#10
filename27 = ['9574384526955649777', '9574384527220934164', '9574384527220936022']
HERON27 = ["dw", 'TV', "fridge", "lamp", "heater", "washing machine", "minioven", "hair dryer", "watercooker", "toaster"]

#10
filename33 = ['9574384526955649757', '9574384527220934603', '9574384527220934513']
HERON33 = ["wm", 'dw', "toaster", "fan", "microwave", "iron", "hot air gun", "router", "coffee machine", "TV"]

#10
filename31 = ['9574384526955649773', '9574384527220936009', '9574384527220933998']
HERON31 = ["dryer", 'TV', "printer", "laptop", "iron", "hot air gun", "router", "lamp", "gaming PC", "radio"]

#12
filename26 = ['9574384526955649732', '9574384527220933565', '9574384527220934884']
HERON26 = ['dryer', 'TV', 'wm', "fan", "microwave", "iron", "hot air gun", "gaming PC", "coffee machine", "TV", "printer", "laptop"]

#12
filename30 = ['9574384526955649735', '9574384527220934002', '9574384527220934363']
HERON30 = ['ac', 'ac', "gaming PC", "fan", "microwave", "iron", "hot air gun", "radio", "coffee machine", "TV", "printer", "laptop"]

#12
filename39 = ['9574384526955649780', '9574384527220934049', '9574384527220934044']
HERON39 = ['wm', 'ac', "DR_Heart", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan", "coffee machine", "TV"]

#12
filename37 = ['9574384526955649782', '9574384527220936128', '9574384527220934871']
HERON37 = ['dw', 'wm', "gaming PC", "fan", "microwave", "iron", "hot air gun", "radio", "coffee machine", "TV", "printer", "laptop"]

#12
filename28 = ['9574384526955649796', '9574384527220936573', '9574384527220934159']
HERON28 = ["wm", 'ac', "dryer", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan", "coffee machine", "TV"]

#12
filename22 = ['9574384526955649758', '9574384527220936571', '9574384527220934178']
HERON22 = ["ac", 'wm', "fridge", "lamp", "heater", "washing machine", "minioven", "hair dryer", "watercooker", "toaster", "coffee machine", "TV"]

#12
filename21 = ['9574384526955649734', '9574384527220934832', '9574384527220933391']
HERON21 = ["ac", 'wm', "gaming PC", "heater", "microwave", "iron", "hot air gun", "radio", "coffee machine", "toaster", "printer", "laptop"]

#12
filename19 = ['9574384526955649781', '9574384527220934640', '9574384527220934534']
HERON19 = ["ac", 'ac', "gaming PC", "fan", "microwave", "iron", "hot air gun", "radio", "coffee machine", "TV", "printer", "laptop"]

#12
filename18 = ['9574384526955649755', '9574384527220941163', '9574384527220934373']
HERON18 = ["ac", 'ac', "wm", "dryer", "fridge", "hot air gun", "router", "lamp", "gaming PC", "radio"]

#12
filename16 = ['9574384526955649785', '9574384527220936269', '9574384527220936045']
HERON16 = ["ac", 'dw', "router", "heater", "printer", "lamp", "gaming PC", "monitor", "toaster", "fan", "coffee machine", "TV"]

#12
filename23 = ['9574384526955649767', '9574384527220936042', '9574384527220934786']
HERON23 = ["ac", 'wm', "router", "fridge", "printer", "lamp", "gaming PC", "monitor", "radio", "fan", "laptop", "TV"]


appMapper = {
    # PERIODICAL APPLIANCES
    "fridge": (lambda x: fridge(x)),
    "FR_Heart": (lambda x: FR_Heart(x)),
    "FRCombo_Heart": (lambda x: FRCombo_Heart(x)),


    # MULTI PATTERN APPLIANCES
    "dishwasher": (lambda x: dishwasher(x)),
    "DW_Heart": (lambda x: DW_Heart(x)),
    "heater": (lambda x: heater(x)),
    "washing machine": (lambda x: washingmachine(x)),
    "toaster": (lambda x: toaster(x)),
    "fan": (lambda x: fan(x)),
    "microwave": (lambda x: microwave(x)),
    "iron": (lambda x: iron(x)),
    "hot air gun": (lambda x: hot_air_gun(x)),
    "WM_Heart": (lambda x: WM_Heart(x)),
    "ac": (lambda x: ac(x)),
    "dryer": (lambda x: dryer(x)),
    "wm": (lambda x: wm(x)),
    "dw": (lambda x: dw(x)),

    # ALWAYS ON
    "router": (lambda x: router(x)),

    # ON-OFF APPLIANCES
    "TV": (lambda x: TV(x)),
    "coffee machine": (lambda x: coffeemachine(x)),
    "printer": (lambda x: printer(x)),
    "laptop": (lambda x: laptop(x)),
    "lamp": (lambda x: lamp(x)),
    "gaming PC": (lambda x: gaming_PC(x)),

    # SINGLE PATTERN
    "radio": (lambda x: radio(x)),
    "monitor": (lambda x: monitor(x)),
    "minioven": (lambda x: minioven(x)),
    "hair dryer": (lambda x: hairdryer(x)),
    "watercooker": (lambda x: watercooker(x)),

    #ILIAS DATA
    "ilias data": (lambda x: ilias_data(x)),
    "AC_Heart": (lambda x: AC_Heart(x)),
    "DR_Heart": (lambda x: DR_Heart(x)),
}


def load_settings(settings_file='settings.json'):
    with open(settings_file) as s_f:
        return json.load(s_f)


def clean_dir(dir):
    files = glob.glob(dir)
    for f in files:
        os.remove(f)


def remove_csv(dir):
    path = os.listdir(dir)
    for item in path:
        if item.endswith('.csv'):
            os.remove(os.path.join(dir, item))


def update_metadata(settings_dict):

    with open('metadata/dataset.yaml', 'r') as outfile:
        meta_dict = yaml.load(outfile)

    meta_dict['dataset_ID'] = settings_dict['ID']
    meta_dict['duration'] = settings_dict['nr_days']
    meta_dict['sampling_interval'] = settings_dict['sampling_interval']
    meta_dict['date_created'] = datetime.now().date().strftime('%Y-%m-%d')

    with open('metadata/dataset.yaml', 'w') as outfile:
        yaml.dump(meta_dict, outfile, default_flow_style=False)


    with open('metadata/meter_devices.yaml', 'r') as outfile:
        meta_dict = yaml.load(outfile)

    meta_dict['HMC8015']['sample_period'] = settings_dict['sampling_interval']
    meta_dict['HMC8015']['max_sample_period'] = settings_dict['sampling_interval']

    with open('metadata/meter_devices.yaml', 'w') as outfile:
        yaml.dump(meta_dict, outfile, default_flow_style=False)

    return 0


def load_clean_resample_series(app_name, settings_dict):
    x = np.array([])

    for i in range(settings_dict['nr_days']):
        x = np.concatenate([x, appMapper[app_name](samples_per_day)])

    df = pd.Series(x)
    tz_naive = pd.date_range(datetime.today().strftime('%Y-%m-%d'), periods=settings_dict['nr_days'] * samples_per_day,
                             freq='0.1S')

    tz_aware = tz_naive.tz_localize(tz=None)
    df.index = tz_aware

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(method='ffill')
    return df.resample('{}S'.format(settings_dict['sampling_interval'])).first()#median()


def _generate(settings_dict, basedir='target'):

    for app_name in settings_dict['appliances']:

        # Convert to Pandas Series and remove INFs and NaNs
        submeter_df = load_clean_resample_series(app_name, settings_dict)
        # power_level_noise = np.random.normal(1, 0.1)
        # print('power_level_noise = ', power_level_noise)
        # submeter_df *= power_level_noise

        # Store to CSVs
        submeter_df.to_csv(
            'target/{}/{}.csv'.format(settings_dict['ID'], appID[app_name]), sep='\t', encoding='utf-8')

        try:

            aggregate_df = pd.read_csv(
                'target/{}/{}.csv'.format(settings_dict['ID'], appID["aggregate"]), sep='\t', encoding='utf-8',
            header=None)

            aggregate_df = aggregate_df.set_index(aggregate_df.columns[0], drop=True)
            aggregate_df = aggregate_df.squeeze()
            aggregate_df.add(submeter_df, fill_value=0)
            # aggregate_df += submeter_df

            aggregate_df.to_csv(
                'target/{}/{}.csv'.format(settings_dict['ID'], appID["aggregate"]), sep='\t', encoding='utf-8')

        except FileNotFoundError:
            submeter_df.to_csv(
                'target/{}/{}.csv'.format(settings_dict['ID'], appID["aggregate"]), sep='\t', encoding='utf-8')

        gc.collect()



if __name__ == '__main__':

    # #ignore warning
    # import warnings
    # warnings.simplefilter(action='ignore', category=FutureWarning)

    # LOAD SETTINGS
    settings = load_settings('settings.json')

    np.random.seed(settings['SEED'])

    try:
        os.mkdir('target/{}'.format(settings['ID']))

    except FileExistsError:
        pass

    # GENERATE DATA
    _generate(settings)

    if settings['output_format'] == 'CSV':

        shutil.copy('metadata.zip', 'target/{}'.format(settings['ID']))
        shutil.copy('appliance_labels.yml', 'target/{}'.format(settings['ID']))

        shutil.make_archive(
            'datasets/SynD_dataset_{}'.format(settings['ID']),
            'zip', 'target/{}'.format(settings['ID'])
        )

    elif settings['output_format'] == 'HDF5':

        # Convert to HDF5
        update_metadata(settings)

        convert_SynD('target/{}/'.format(settings['ID']), 'target/{}/SynD_{}.h5'.format(
            settings['ID'], settings['ID']), format='HDF')

        shutil.copy('metadata.zip', 'target/{}'.format(settings['ID']))
        shutil.copy('appliance_labels.yml', 'target/{}'.format(settings['ID']))

    else:
        pass


    # with open("merging_Households.py") as f:
    #     exec(f.read())

    exit()

'''
Copyright notice

CC0 - No Rights Reserved

Christoph Klemenjak (klemenjak@ieee.org), Christoph Kovatsch, Manuel Herold, and Wilfried Elmenreich

Find further material and the latest version of this tool at https://github.com/klemenjak/SynD/

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or
her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

Unless expressly stated otherwise, the person who associated a work with this deed makes no warranties about the work,
and disclaims liability for all uses of the work, to the fullest extent permitted by applicable law.
'''
