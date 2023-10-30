# import libraries
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import json

############################################################################################################

hour = round(14400 / 24)
day = 14400

date_format = "%m-%d-%Y"
today = date.today()
d3 = today.strftime(date_format)

a = datetime.strptime('07-04-2021', date_format)
b = datetime.strptime(d3, date_format)
delta = b - a
# print(delta.days)

# that's it how to calculate number of days between two given dates


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
    "wm": 32,
    "dw": 33
}

# all devices for settings json
all_appliances = ["fridge", "wm", "dishwasher", "heater", "dryer", "washing machine", "toaster", "dw", "microwave",
                  "iron",
                  "hot air gun", "ac", "router", \
                  "coffee machine", "TV", "printer", "laptop", "lamp", "gaming PC", "radio", "monitor", "minioven", \
                  "hair dryer", "watercooker", "WM_Heart", "AC_Heart", "DR_Heart", "DW_Heart", "FR_Heart"]

# 6 devices
standart_noise = ["fridge", "wm", "minioven", "TV", "router", "lamp"]

# 13 devices
extra_noise = ["heater", "toaster", "microwave", "iron", "hot air gun", "coffee machine", "printer",
               "laptop", "gaming PC", "radio", "monitor", "hair dryer", "watercooker"]

# Heron devices with smartplugs
heron = ["ac", "dw", "wm", "dryer", "TV", "gaming PC"]

H1 = ["ac", "dw", "fridge", "wm", "minioven", "TV", "router", "lamp", "heater", "toaster", "microwave", "iron"]
H2 = ["wm", "TV", "fridge", "watercooker", "minioven", "toaster", "router", "lamp", "iron", "hot air gun",
      "coffee machine", "printer"]
H3 = ["wm", "ac", "fridge", "hair dryer", "minioven", "TV", "router", "lamp", "laptop", "gaming PC", "radio", "monitor"]
H4 = ["ac", "wm", "fridge", "dryer", "minioven", "TV", "router", "lamp", "gaming PC", "radio", "monitor", "hair dryer"]
H5 = ["dw", "wm", "fridge", "monitor", "minioven", "TV", "router", "lamp", "heater", "toaster", "watercooker", "iron"]
H6 = ["ac", "wm", "fridge", "dw", "minioven", "TV", "router", "lamp", "hot air gun", "coffee machine", "printer",
      "laptop"]
H7 = ["dw", "wm", "fridge", "gaming PC", "minioven", "TV", "router", "lamp", "laptop", "watercooker", "radio",
      "monitor"]
H8 = ["TV", "dw", "fridge", "wm", "minioven", "microwave", "router", "lamp", "radio", "monitor", "hair dryer",
      "watercooker"]
H9 = ["ac", "TV", "fridge", "wm", "minioven", "microwave", "router", "lamp", "radio", "monitor", "hair dryer",
      "watercooker"]
H10 = ["ac", "wm", "fridge", "dryer", "minioven", "TV", "router", "lamp", "microwave", "iron", "hot air gun",
       "coffee machine"]
H11 = ["ac", "wm", "fridge", "dryer", "minioven", "TV", "router", "lamp", "gaming PC", "radio", "monitor", "hair dryer"]
H12 = ["ac", "wm", "fridge", "radio", "minioven", "TV", "router", "lamp", "toaster", "microwave", "iron", "hot air gun"]
H13 = ["TV", "wm", "fridge", "microwave", "minioven", "toaster", "router", "lamp", "iron", "hot air gun",
       "coffee machine", "printer"]
H14 = ["ac", "dw", "fridge", "wm", "minioven", "TV", "router", "lamp", "heater", "toaster", "microwave", "iron"]
H15 = ["ac", "ac.1", "fridge", "wm", "minioven", "TV", "router", "lamp", "radio", "monitor", "iron", "hot air gun"]
H38 = ["ac", "dryer", "fridge", "wm", "minioven", "TV", "router", "lamp", "laptop", "gaming PC", "coffee machine",
       "printer"]
H29 = ["gaming PC", "dw", "fridge", "wm", "minioven", "TV", "router", "lamp", "heater", "toaster", "microwave", "iron"]
H27 = ["wm", "TV", "fridge", "radio", "minioven", "dryer", "router", "lamp", "microwave", "iron", "hot air gun",
       "coffee machine"]
H33 = ["wm", "dw", "fridge", "iron", "minioven", "TV", "router", "lamp", "monitor", "hair dryer", "watercooker",
       "heater"]
H31 = ["dryer", "TV", "fridge", "wm", "minioven", "monitor", "router", "lamp", "heater", "toaster", "microwave",
       "watercooker"]
H26 = ["dryer", "TV", "fridge", "wm", "minioven", "toaster", "router", "lamp", "radio", "monitor", "hair dryer",
       "watercooker"]
H30 = ["ac", "ac.1", "fridge", "wm", "minioven", "TV", "router", "lamp", "microwave", "iron", "hot air gun",
       "coffee machine"]
H39 = ["wm", "ac", "fridge", "iron", "minioven", "TV", "router", "lamp", "laptop", "gaming PC", "radio", "monitor"]
H37 = ["dw", "wm", "fridge", "iron", "minioven", "TV", "router", "lamp", "radio", "monitor", "hair dryer",
       "watercooker"]
H28 = ["wm", "ac", "fridge", "iron", "minioven", "TV", "router", "lamp", "gaming PC", "radio", "monitor", "hair dryer"]
H22 = ["ac", "wm", "fridge", "iron", "minioven", "TV", "router", "lamp", "hair dryer", "radio", "hot air gun",
       "hair dryer"]
H21 = ["ac", "wm", "fridge", "dryer", "minioven", "TV", "router", "lamp", "microwave", "iron", "hot air gun",
       "coffee machine"]
H19 = ["ac", "ac.1", "fridge", "wm", "minioven", "TV", "router", "lamp", "laptop", "gaming PC", "iron", "hot air gun"]
H18 = ["ac", "ac.1", "fridge", "wm", "minioven", "TV", "router", "lamp", "hot air gun", "coffee machine", "hair dryer",
       "watercooker"]
H16 = ["ac", "dw", "fridge", "iron", "minioven", "TV", "router", "lamp", "radio", "monitor", "hair dryer",
       "watercooker"]
H23 = ["ac", "wm", "fridge", "dryer", "minioven", "TV", "router", "lamp", "heater", "toaster", "microwave", "iron"]


# load settings json
def load_settings(settings_file='settings.json'):
    with open(settings_file) as s_f:
        return json.load(s_f)


settings = load_settings('settings.json')
appliances = settings['appliances']
ID = settings['ID']
days_settings_json = settings['nr_days']

if len(appliances) == 8:

    df1 = pd.read_csv(
        f'target/{ID}/{appID[appliances[0]]}.csv',
        sep='\t')
    df1.columns = ['Datetime', 'power']
    df2 = pd.read_csv(
        f'target/{ID}/{appID[appliances[1]]}.csv',
        sep='\t')
    df2.columns = ['Datetime', 'power']
    df3 = pd.read_csv(
        f'target/{ID}/{appID[appliances[2]]}.csv',
        sep='\t')
    df3.columns = ['Datetime', 'power']
    df4 = pd.read_csv(
        f'target/{ID}/{appID[appliances[3]]}.csv',
        sep='\t')
    df4.columns = ['Datetime', 'power']
    df5 = pd.read_csv(
        f'target/{ID}/{appID[appliances[4]]}.csv',
        sep='\t')
    df5.columns = ['Datetime', 'power']
    df6 = pd.read_csv(
        f'target/{ID}/{appID[appliances[5]]}.csv',
        sep='\t')
    df6.columns = ['Datetime', 'power']
    df7 = pd.read_csv(
        f'target/{ID}/{appID[appliances[6]]}.csv',
        sep='\t')
    df7.columns = ['Datetime', 'power']
    df8 = pd.read_csv(
        f'target/{ID}/{appID[appliances[7]]}.csv',
        sep='\t')
    df8.columns = ['Datetime', 'power']

    df1_time = df1['Datetime']
    df1_mains = df1['power'] + df2['power'] + df3['power'] + df4['power'] + df5['power'] + df6['power'] \
                + df7['power'] + df8['power']
    # temp = pd.concat([df1_time, df1_mains], axis=1)
    HERON1 = pd.concat(
        [df1_time, df1_mains, df1['power'], df2['power'], df3['power'], df4['power'], df5['power'], df6['power'],
         df7['power'], df8['power']], axis=1)
    HERON1.columns = ['Datetime', 'mains', f"{appliances[0]}", f"{appliances[1]}", f"{appliances[2]}",
                      f"{appliances[3]}",
                      f"{appliances[4]}", f"{appliances[5]}", f"{appliances[6]}", f"{appliances[7]}"]

    # timestamp convertion
    timestamps = HERON1['Datetime'].tolist()
    # str to datetime oneliner
    list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
                                   timestamps]
    HERON1['Datetime'] = list_of_converted_datetimes
    HERON1.to_csv(f'target/{ID}/HERON{ID}.csv', index=False)

elif len(appliances) == 1:
    df1 = pd.read_csv(
        f'target/{ID}/{appID[appliances[0]]}.csv',
        sep='\t')
    df1.columns = ['Datetime', 'power']
    df1_time = df1['Datetime']
    df1_mains = df1['power']

    HERON1 = pd.concat(
        [df1_time, df1_mains, df1['power']], axis=1)
    HERON1.columns = ['Datetime', 'mains', f"{appliances[0]}"]

    # timestamp convertion
    timestamps = HERON1['Datetime'].tolist()
    # str to datetime oneliner
    list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
                                   timestamps]
    HERON1['Datetime'] = list_of_converted_datetimes
    HERON1.to_csv(f'target/{ID}/HERON{ID}.csv', index=False)

elif len(appliances) == 10:

    df1 = pd.read_csv(
        f'target/{ID}/{appID[appliances[0]]}.csv',
        sep='\t')
    df1.columns = ['Datetime', 'power']
    df2 = pd.read_csv(
        f'target/{ID}/{appID[appliances[1]]}.csv',
        sep='\t')
    df2.columns = ['Datetime', 'power']
    df3 = pd.read_csv(
        f'target/{ID}/{appID[appliances[2]]}.csv',
        sep='\t')
    df3.columns = ['Datetime', 'power']
    df4 = pd.read_csv(
        f'target/{ID}/{appID[appliances[3]]}.csv',
        sep='\t')
    df4.columns = ['Datetime', 'power']
    df5 = pd.read_csv(
        f'target/{ID}/{appID[appliances[4]]}.csv',
        sep='\t')
    df5.columns = ['Datetime', 'power']
    df6 = pd.read_csv(
        f'target/{ID}/{appID[appliances[5]]}.csv',
        sep='\t')
    df6.columns = ['Datetime', 'power']
    df7 = pd.read_csv(
        f'target/{ID}/{appID[appliances[6]]}.csv',
        sep='\t')
    df7.columns = ['Datetime', 'power']
    df8 = pd.read_csv(
        f'target/{ID}/{appID[appliances[7]]}.csv',
        sep='\t')
    df8.columns = ['Datetime', 'power']
    df9 = pd.read_csv(
        f'target/{ID}/{appID[appliances[8]]}.csv',
        sep='\t')
    df9.columns = ['Datetime', 'power']
    df10 = pd.read_csv(
        f'target/{ID}/{appID[appliances[9]]}.csv',
        sep='\t')
    df10.columns = ['Datetime', 'power']

    df1_time = df1['Datetime']
    df1_mains = df1['power'] + df2['power'] + df3['power'] + df4['power'] + df5['power'] + df6['power'] \
                + df7['power'] + df8['power'] + df9['power'] + df10['power']
    # temp = pd.concat([df1_time, df1_mains], axis=1)
    HERON1 = pd.concat(
        [df1_time, df1_mains, df1['power'], df2['power'], df3['power'], df4['power'], df5['power'], df6['power'],
         df7['power'], df8['power'], df9['power'], df10['power']], axis=1)
    HERON1.columns = ['Datetime', 'mains', f"{appliances[0]}", f"{appliances[1]}", f"{appliances[2]}",
                      f"{appliances[3]}",
                      f"{appliances[4]}", f"{appliances[5]}", f"{appliances[6]}", f"{appliances[7]}",
                      f"{appliances[8]}", f"{appliances[9]}"]

    # timestamp convertion
    timestamps = HERON1['Datetime'].tolist()
    # str to datetime oneliner
    list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
                                   timestamps]
    HERON1['Datetime'] = list_of_converted_datetimes



elif len(appliances) == 12:

    df1 = pd.read_csv(
        f'target/{ID}/{appID[appliances[0]]}.csv',
        sep='\t')
    df1.columns = ['Datetime', 'power']
    df2 = pd.read_csv(
        f'target/{ID}/{appID[appliances[1]]}.csv',
        sep='\t')
    df2.columns = ['Datetime', 'power']
    df3 = pd.read_csv(
        f'target/{ID}/{appID[appliances[2]]}.csv',
        sep='\t')
    df3.columns = ['Datetime', 'power']
    df4 = pd.read_csv(
        f'target/{ID}/{appID[appliances[3]]}.csv',
        sep='\t')
    df4.columns = ['Datetime', 'power']
    df5 = pd.read_csv(
        f'target/{ID}/{appID[appliances[4]]}.csv',
        sep='\t')
    df5.columns = ['Datetime', 'power']
    df6 = pd.read_csv(
        f'target/{ID}/{appID[appliances[5]]}.csv',
        sep='\t')
    df6.columns = ['Datetime', 'power']
    df7 = pd.read_csv(
        f'target/{ID}/{appID[appliances[6]]}.csv',
        sep='\t')
    df7.columns = ['Datetime', 'power']
    df8 = pd.read_csv(
        f'target/{ID}/{appID[appliances[7]]}.csv',
        sep='\t')
    df8.columns = ['Datetime', 'power']
    df9 = pd.read_csv(
        f'target/{ID}/{appID[appliances[8]]}.csv',
        sep='\t')
    df9.columns = ['Datetime', 'power']
    df10 = pd.read_csv(
        f'target/{ID}/{appID[appliances[9]]}.csv',
        sep='\t')
    df10.columns = ['Datetime', 'power']
    df11 = pd.read_csv(
        f'target/{ID}/{appID[appliances[10]]}.csv',
        sep='\t')
    df11.columns = ['Datetime', 'power']
    df12 = pd.read_csv(
        f'target/{ID}/{appID[appliances[11]]}.csv',
        sep='\t')
    df12.columns = ['Datetime', 'power']

    df1_time = df1['Datetime']
    df1_mains = df1['power'] + df2['power'] + df3['power'] + df4['power'] + df5['power'] + df6['power'] + df7['power'] + \
                df8['power'] \
                + df9['power'] + df10['power'] + df11['power'] + df12['power']
    # temp = pd.concat([df1_time, df1_mains], axis=1)
    HERON1 = pd.concat(
        [df1_time, df1_mains, df1['power'], df2['power'], df3['power'], df4['power'], df5['power'], df6['power'],
         df7['power'], df8['power'], df9['power'], df10['power'], df11['power'], df12['power']], axis=1)
    HERON1.columns = ['Datetime', 'mains', f"{appliances[0]}", f"{appliances[1]}", f"{appliances[2]}",
                      f"{appliances[3]}", f"{appliances[4]}",
                      f"{appliances[5]}", f"{appliances[6]}", f"{appliances[7]}", f"{appliances[8]}",
                      f"{appliances[9]}", f"{appliances[10]}", f"{appliances[11]}"]

    # timestamp convertion
    timestamps = HERON1['Datetime'].tolist()
    # str to datetime oneliner
    list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
                                   timestamps]
    HERON1['Datetime'] = list_of_converted_datetimes
    HERON1.to_csv(f'target/{ID}/HERON{ID}.csv', index=False)

# all appliances
else:
    df1 = pd.read_csv(
        f'target/{ID}/{appID[appliances[0]]}.csv',
        sep='\t')
    df1.columns = ['Datetime', 'power']
    df2 = pd.read_csv(
        f'target/{ID}/{appID[appliances[1]]}.csv',
        sep='\t')
    df2.columns = ['Datetime', 'power']
    df3 = pd.read_csv(
        f'target/{ID}/{appID[appliances[2]]}.csv',
        sep='\t')
    df3.columns = ['Datetime', 'power']
    df4 = pd.read_csv(
        f'target/{ID}/{appID[appliances[3]]}.csv',
        sep='\t')
    df4.columns = ['Datetime', 'power']
    df5 = pd.read_csv(
        f'target/{ID}/{appID[appliances[4]]}.csv',
        sep='\t')
    df5.columns = ['Datetime', 'power']
    df6 = pd.read_csv(
        f'target/{ID}/{appID[appliances[5]]}.csv',
        sep='\t')
    df6.columns = ['Datetime', 'power']
    df7 = pd.read_csv(
        f'target/{ID}/{appID[appliances[6]]}.csv',
        sep='\t')
    df7.columns = ['Datetime', 'power']
    df8 = pd.read_csv(
        f'target/{ID}/{appID[appliances[7]]}.csv',
        sep='\t')
    df8.columns = ['Datetime', 'power']
    df9 = pd.read_csv(
        f'target/{ID}/{appID[appliances[8]]}.csv',
        sep='\t')
    df9.columns = ['Datetime', 'power']
    df10 = pd.read_csv(
        f'target/{ID}/{appID[appliances[9]]}.csv',
        sep='\t')
    df10.columns = ['Datetime', 'power']
    df11 = pd.read_csv(
        f'target/{ID}/{appID[appliances[10]]}.csv',
        sep='\t')
    df11.columns = ['Datetime', 'power']
    df12 = pd.read_csv(
        f'target/{ID}/{appID[appliances[11]]}.csv',
        sep='\t')
    df12.columns = ['Datetime', 'power']
    df13 = pd.read_csv(
        f'target/{ID}/{appID[appliances[12]]}.csv',
        sep='\t')
    df13.columns = ['Datetime', 'power']
    df14 = pd.read_csv(
        f'target/{ID}/{appID[appliances[13]]}.csv',
        sep='\t')
    df14.columns = ['Datetime', 'power']
    df15 = pd.read_csv(
        f'target/{ID}/{appID[appliances[14]]}.csv',
        sep='\t')
    df15.columns = ['Datetime', 'power']
    df16 = pd.read_csv(
        f'target/{ID}/{appID[appliances[15]]}.csv',
        sep='\t')
    df16.columns = ['Datetime', 'power']
    df17 = pd.read_csv(
        f'target/{ID}/{appID[appliances[16]]}.csv',
        sep='\t')
    df17.columns = ['Datetime', 'power']
    df18 = pd.read_csv(
        f'target/{ID}/{appID[appliances[17]]}.csv',
        sep='\t')
    df18.columns = ['Datetime', 'power']
    df19 = pd.read_csv(
        f'target/{ID}/{appID[appliances[18]]}.csv',
        sep='\t')
    df19.columns = ['Datetime', 'power']
    df20 = pd.read_csv(
        f'target/{ID}/{appID[appliances[19]]}.csv',
        sep='\t')
    df20.columns = ['Datetime', 'power']
    df21 = pd.read_csv(
        f'target/{ID}/{appID[appliances[20]]}.csv',
        sep='\t')
    df21.columns = ['Datetime', 'power']
    df22 = pd.read_csv(
        f'target/{ID}/{appID[appliances[21]]}.csv',
        sep='\t')
    df22.columns = ['Datetime', 'power']
    df23 = pd.read_csv(
        f'target/{ID}/{appID[appliances[22]]}.csv',
        sep='\t')
    df23.columns = ['Datetime', 'power']

    df1_time = df1['Datetime']
    df1_mains = df1['power'] + df2['power'] + df3['power'] + df4['power'] + \
                df5['power'] + df6['power'] + df7['power'] + df8['power'] \
                + df9['power'] + df10['power'] + df11['power'] + df12['power'] \
                + df13['power'] + df14['power'] + df15['power'] + df16['power'] \
                + df17['power'] + df18['power'] + df19['power'] + df20['power']  \
                + df21['power'] + df22['power'] + df23['power']
        # temp = pd.concat([df1_time, df1_mains], axis=1)
    HERON1 = pd.concat(
        [df1_time, df1_mains, df1['power'], df2['power'], df3['power'], df4['power'], df5['power'], df6['power'],
         df7['power'], df8['power'], df9['power'], df10['power'], df11['power'], df12['power'],
         df13['power'], df14['power'], df15['power'], df16['power'], df17['power'], df18['power'],
         df19['power'], df20['power'], df21['power'], df22['power'], df23['power']], axis=1)
    HERON1.columns = ['Datetime', 'mains', f"{appliances[0]}", f"{appliances[1]}", f"{appliances[2]}",
                      f"{appliances[3]}", f"{appliances[4]}",
                      f"{appliances[5]}", f"{appliances[6]}", f"{appliances[7]}", f"{appliances[8]}",
                      f"{appliances[9]}", f"{appliances[10]}", f"{appliances[11]}",
                      f"{appliances[12]}", f"{appliances[13]}", f"{appliances[14]}",
                      f"{appliances[15]}", f"{appliances[16]}",
                      f"{appliances[17]}", f"{appliances[18]}", f"{appliances[19]}", f"{appliances[20]}",
                      f"{appliances[21]}", f"{appliances[22]}"]

    # # timestamp convertion
    # timestamps = HERON1['Datetime'].tolist()
    # # str to datetime oneliner
    # list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
    #                                timestamps]
    # HERON1['Datetime'] = list_of_converted_datetimes
    # # upsamping
    HERON1['Datetime'] = pd.to_datetime(HERON1['Datetime'])
    HERON1.iloc[:, 1:] = HERON1.iloc[:, 1:].div(1000 * 3600)
    HERON1.set_index('Datetime', inplace=True)
    hourly_df = HERON1.resample('1H').sum()

    # timestamp conversion
    hourly_df.reset_index(inplace=True)
    timestamps = hourly_df['Datetime'].tolist()
    # Convert Timestamp to string with the desired format
    timestamps_as_strings = [t.strftime('%Y-%m-%d %H:%M:%S') for t in timestamps]
    # Use the converted strings with strptime
    list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=delta.days) for t in
                                   timestamps_as_strings]
    hourly_df['Datetime'] = list_of_converted_datetimes

    # csv export
    hourly_df.to_csv(f'target/{ID}/HERON{ID}.csv', index=False)


