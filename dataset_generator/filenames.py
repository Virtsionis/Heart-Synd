def toaster_use(var):
    if var == 0:
            filename = 'Toaster_1.csv'
    elif var == 1:
            filename = 'Toaster_US.csv'
    elif var == 2:
            filename = 'Toaster_7.csv'

    return filename

def washingmachine_use(var):
    if var == 0:
            filename = 'WM_USE40.csv'
    elif var == 1:
            filename = 'WM_USE60.csv'

    return filename


def dishwasher_use(var):
    if var == 0:
            filename = 'DW-LONG.csv'
    elif var == 1:
            filename = 'DW-ORDI.csv'
    elif var == 2:
            filename = 'DW-SP.csv'

    return filename


def fan_use(var):
    if var == 0:
            filename = 'FAN_1.csv'
    elif var == 1:
            filename = 'FAN_3.csv'

    return filename


def heater_use(var):
    if var == 0:
            filename = 'Heater_USE_1000W.csv'
    elif var == 1:
            filename = 'Heater_USE_2000W.csv'

    return filename



def iron_use(var):
     if var == 0:
            filename = 'IRON_US2.csv'
     elif var == 1:
            filename = 'IRON_US3.csv'

     return filename


def hot_air_gun_use(var):
    if var == 0:
            filename = 'Hot_Air_Gun.csv'
    elif var == 1:
            filename = 'Hot_Air_Gun_2.csv'
    return filename


def microwave_use(var):
    if var == 0:
            filename = 'Micro_Wave_90.csv'
    elif var == 1:
            filename = 'Micro_Wave_360.csv'
    elif var == 2:
            filename = 'Micro_Wave_800.csv'

    return filename

def WM_Heart_use():
    filename = "WM_ovenlike_double_9574384527220934871.csv"
    # filename = "WM_double_fat_9574384527220934178.csv"
    return filename

def wm_use(var):

    # not used traces
    # filename = 'WM_almost_nopulse_9574384527220936133.csv'
    # filename = "WM_high_thin_low_fat_double_9574384527220934178.csv"
    # filename = 'WM_ovenlike_double_9574384527220934871.csv'
    # filename = 'WM_ovenlike_double_9574384527220934049.csv'
    # filename = 'WM_nopulse_9574384527220934049.csv'
    # filename = 'WM_double_thin_9574384527220934178.csv'
    # filename = "WM_double_thin_9574384527220934786.csv"
    # used traces
    if var == 0:
        filename = 'WM_double_fat_9574384527220934178.csv'
    else:
        filename = 'WM_ovenlike_double_9574384527220934871.csv'
    return filename

def DR_Heart_use():
    filename = "DR_hp_low_9574384527220934070.csv"
    return filename


def dryer_use(var):
    if var == 0:
        filename = 'DR_hp_double_9574384527220936009.csv'
    elif var == 1:
        filename = 'DR_hp_double_high_9574384527220936009.csv'
    else:
        filename = 'DR_hp_low_9574384527220934070.csv'
    return filename


def DW_Heart_use():
    filename = "DW_two_pulse_9574384527220936014.csv"
    return filename


def dw_use(var):
    if var == 0:
        filename = 'DW_five_pulse_9574384527220936130.csv'
    elif var == 1:
        filename = 'DW_five_pulse_9574384527220934118.csv'
    elif var ==2 :
        filename = 'DW_four_pulse_9574384527220936128.csv'
    elif var == 3:
        filename = 'DW_three_pulse_9574384527220936014.csv'
    else:
        filename = 'DW_two_pulse_9574384527220936014.csv'
    return filename


def FR_Heart_use():
    filename = "FR_simple_1.csv"
    return filename


def FRCombo_Heart_use():
    filename = "IDD_AC_WM_final_stage.csv"
    return filename


def AC_Heart_use():
    filename = "AC_long_high_9574384527220941042.csv"
    return filename

def ac_use(var):
    if var == 0:
        filename = 'AC_high_9574384527220941042.csv'
    elif var == 1:
        filename = 'AC_hp_like_9574384527220936265.csv'
    elif var == 2:
        filename = 'AC_long_9574384527220936265.csv'
    elif var == 3:
        filename = 'AC_long_high_9574384527220934215.csv'
    elif var == 4:
        filename = 'AC_long_high_9574384527220941039.csv'
    elif var == 5:
        filename = 'AC_long_high_9574384527220941042.csv'
    elif var == 6:
        filename = 'AC_long_short_9574384527220934034.csv'
    else:
        filename = 'AC_short_9574384527220941042.csv'

    return filename


def ilias_data_use():
    filename = "IDD_AC_WM.csv"
    return filename

