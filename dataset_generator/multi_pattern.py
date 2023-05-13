import numpy as np
import interpolate as interpol
import time_handler as time_handle
import use_patterns as use_pat

day = 864000


def toaster(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.toaster_use(x)

        my = np.random.randint(290000, 340000)
        sigma = 10000
        my_we = np.random.randint(310000, 360000)
        sigma_we = 5000
        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor_noise()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def washingmachine(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.washingmachine_use(x)

        my = np.random.randint(500000, 600000)
        sigma = 40000
        my_we = np.random.randint(360000, 620000)
        sigma_we = 20000
        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def dishwasher(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 20)

        data, n_rows = use_pat.dishwasher_use(x)

        #original
        my = np.random.randint(450000, 600000)
        sigma = 50000
        my_we = np.random.randint(350000, 640000)
        sigma_we = 20000

        # #changes
        # my = np.random.randint(000000, 600000)
        # sigma = 50000
        # my_we = np.random.randint(00000, 860000)
        # sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)

        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def exist_power_factor():
    existence_factor = np.random.normal(0.75, 0.4)

    #Without changes
    # existence_factor > 0.5
    if existence_factor < 1.3:
        existence_factor = 1
    else:
        existence_factor = 0
    power_level_noise = np.random.normal(1, 0.1)

    # test always equal to 1
    # existence_factor = 1

    if power_level_noise > 1.10:
        power_level_noise = 1.10
    if power_level_noise < 0.9:
        power_level_noise = 0.9
    final_factor = existence_factor * power_level_noise
    return final_factor

# uses are almost every day
# power level alternations are same as in the previous function
def exist_power_factor_noise():
    existence_factor = np.random.normal(0.75, 0.4)
    # almost all the generated values from the current Gaussian distribution are under
    # with that if statement we make sure a huge percent of the uses get inserted every day and a very small percent of the uses is skipped every day
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


def fan(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 5)

        data, n_rows = use_pat.fan_use()

        t1 = np.random.randint(10000, 50000)
        interpolated = interpol.interpolate(t1, n_rows, data, x)
        my = 450000
        sigma = 80000

        t1_we = np.random.randint(10000, 50000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, x)
        my1_we = 400000
        my2_we = 650000
        sigma_we = 20000

        s = np.random.randint(0, 2)
        if s == 0:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my, sigma, interpolated, t1_we, my1_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor
        else:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my, sigma, interpolated, t1_we, my2_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def heater(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 5)

        data, n_rows = use_pat.heater_use()

        t1 = np.random.randint(30000, 100000)
        interpolated = interpol.interpolate(t1, n_rows, data, x)
        my = np.random.randint(650000, 680000)
        sigma = 20000

        t1_we = np.random.randint(40000, 100000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, x)
        my_we = np.random.randint(680000, 720000)
        sigma_we = 40000

        data_day = time_handle.time_handling(
            t, i, n_days, t1, my, sigma, interpolated, t1_we, my_we, sigma_we, interpolated_we)
        scale_factor = exist_power_factor_noise()
        data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def iron(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 5)

        data, n_rows = use_pat.iron_use()

        t1 = np.random.randint(24000, 60000)
        interpolated = interpol.interpolate(t1, n_rows, data, x)
        my = np.random.randint(480000, 550000)
        sigma = 20000

        t1_we = np.random.randint(28000, 64000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, x)
        my_we = np.random.randint(400000, 600000)
        sigma_we = 30000

        data_day = time_handle.time_handling(
            t, i, n_days, t1, my, sigma, interpolated, t1_we, my_we, sigma_we, interpolated_we)
        scale_factor = exist_power_factor_noise()
        data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def hot_air_gun(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 4)

        data, n_rows = use_pat.hot_air_gun_use()

        t1 = np.random.randint(1800, 4200)
        interpolated = interpol.interpolate(t1, n_rows, data, x)
        my = np.random.randint(400000, 450000)
        sigma = 10000

        t1_we = np.random.randint(2400, 6000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, x)
        my_we = np.random.randint(400000, 550000)
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, t1, my, sigma, interpolated, t1_we, my_we, sigma_we, interpolated_we)
        scale_factor = exist_power_factor_noise()
        data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def microwave(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        data, n_rows = use_pat.microwave_use()

        t1 = np.random.randint(1200, 3000)
        interpolated = interpol.interpolate(t1, n_rows, data, 2)
        my = np.random.randint(590000, 640000)
        sigma = 10000

        t1_we = np.random.randint(1200, 3000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, 2)
        my1_we = np.random.randint(590000, 640000)
        my2_we = np.random.randint(420000, 460000)
        sigma_we = 20000

        s = np.random.randint(0, 2)
        if s == 0:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my, sigma, interpolated, t1_we, my1_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor
        else:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my, sigma, interpolated, t1_we, my2_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def ilias_data(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.ilias_data_use()

        my = np.random.randint(500000, 600000)
        sigma = 40000
        my_we = np.random.randint(360000, 620000)
        sigma_we = 20000
        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final



def WM_Heart(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.WM_Heart_use()




        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        #changes
        my = np.random.randint(hours_24[12], hours_24[18])
        sigma = 3*hour
        my_we = np.random.randint(hours_24[12], hours_24[20])
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final

def wm(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(0, 10)

        data, n_rows = use_pat.wm_use(x)




        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        #changes
        my = np.random.randint(hours_24[13], hours_24[19])
        sigma = 4*hour
        my_we = np.random.randint(hours_24[16], hours_24[20])
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final



def dw(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(0, 6)

        data, n_rows = use_pat.dw_use(x)

        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        #changes
        my = np.random.randint(hours_24[11], hours_24[17])
        sigma = 4*hour
        my_we = np.random.randint(hours_24[11], hours_24[20])
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def DW_Heart(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.DW_Heart_use()

        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        #changes
        my = np.random.randint(hours_24[11], hours_24[17])
        sigma = 4*hour
        my_we = np.random.randint(hours_24[11], hours_24[20])
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def DR_Heart(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.DR_Heart_use()

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        # changes
        my = np.random.randint(hours_24[13], hours_24[18])
        sigma = 4 * hour
        my_we = np.random.randint(hours_24[11], hours_24[20])
        sigma_we = 20000

        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final

def dryer(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(0, 3)

        data, n_rows = use_pat.dryer_use(x)

        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        # changes
        my = np.random.randint(hours_24[13], hours_24[18])
        sigma = 4 * hour
        my_we = np.random.randint(hours_24[11], hours_24[20])
        sigma_we = 20000

        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def AC_Heart(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)
        data, n_rows = use_pat.AC_Heart_use()

        # changes
        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        # changes
        my = np.random.randint(hours_24[7], hours_24[9])
        sigma = 4 * hour
        my_we = np.random.randint(hours_24[8], hours_24[13])
        sigma_we = 20000

        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def ac(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(0, 8)
        data, n_rows = use_pat.ac_use(x)

        # changes
        range_24 = [000000, 864000]
        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        hour = 37565

        # changes
        my = np.random.randint(hours_24[7], hours_24[9])
        sigma = 4 * hour
        my_we = np.random.randint(hours_24[8], hours_24[13])
        sigma_we = 20000

        # #original
        # my = np.random.randint(500000, 600000)
        # sigma = 40000
        # my_we = np.random.randint(360000, 620000)
        # sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final



#periodical - to be changed as periodical and not multi after the data is done
def FR_Heart(t):

    n_days = t // day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.FR_Heart_use()

        # #changes
        # my = np.random.randint(000000, 860000)
        # sigma = 10000
        # my_we = np.random.randint(110000, 560000)
        # sigma_we = 5000

        # original
        my = np.random.randint(500000, 600000)
        sigma = 40000
        my_we = np.random.randint(360000, 620000)
        sigma_we = 20000


        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor_noise()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final

#periodical - to be changed as periodical and not multi after the data is done
def FRCombo_Heart(t):
    n_days = t // day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 10)

        data, n_rows = use_pat.FRCombo_Heart_use()

        # #changes
        # my = np.random.randint(000000, 860000)
        # sigma = 10000
        # my_we = np.random.randint(110000, 560000)
        # sigma_we = 5000

        #original
        my = np.random.randint(500000, 600000)
        sigma = 40000
        my_we = np.random.randint(360000, 620000)
        sigma_we = 20000

        data_day = time_handle.time_handling(
            t, i, n_days, n_rows, my, sigma, data, n_rows, my_we, sigma_we, data)
        scale_factor = exist_power_factor_noise()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final

