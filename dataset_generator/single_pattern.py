import numpy as np
import interpolate as interpol
import time_handler as time_handle
import use_patterns as use_pat
import on_patterns as on_pat

day = 864000


def radio(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        data, n_rows = use_pat.radio_use()


        t1 = np.random.randint(10000, 20000)
        interpolated = interpol.interpolate(t1, n_rows, data, 2)
        my = np.random.randint(300000, 340000)
        sigma = 20000

        t1_we = np.random.randint(20000, 30000)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, 2)
        my_we = np.random.randint(330000, 360000)
        sigma_we = 10000

        data_day = time_handle.time_handling(
            t, i, n_days, t1, my, sigma, interpolated, t1_we, my_we, sigma_we, interpolated_we)
        scale_factor = exist_power_factor_noise()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def watercooker(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 8)

        data, n_rows = use_pat.watercooker_use()

        t1 = np.random.randint(2300, 4600)
        t1_we = t1
        interpolated = interpol.interpolate(t1, n_rows, data, x)
        interpolated_we = interpolated

        my1 = 420000
        my1_we = my1
        my2 = 620000
        my2_we = my2
        sigma = 20000
        sigma_we = sigma


        s = 0
        if s == 0:
            try:
                data_day = time_handle.time_handling(
                    t, i, n_days, n_rows, my1, sigma, data, t1_we, my1_we, sigma_we, data)
                scale_factor = exist_power_factor_noise()
                data_final = data_final + data_day * scale_factor
            except IndexError:
                try:
                    data_day = time_handle.time_handling(
                        t, i, n_days, n_rows, my1, sigma, data, t1_we, my1_we, sigma_we, data)
                    scale_factor = exist_power_factor_noise()
                    data_final = data_final + data_day * scale_factor
                except IndexError:
                    pass
        else:
            try:
                data_day = time_handle.time_handling(
                    t, i, n_days, t1, my2, sigma, data, t1_we, my2_we, sigma_we, data)
                scale_factor = exist_power_factor_noise()
                data_final = data_final + data_day * scale_factor
            except IndexError:
                try:
                    data_day = time_handle.time_handling(
                        t, i, n_days, t1, my2, sigma, data, t1_we, my2_we, sigma_we, data)
                    scale_factor = exist_power_factor_noise()
                    data_final = data_final + data_day * scale_factor
                except IndexError:
                    pass

    data_final = np.transpose(data_final)

    return data_final


def monitor(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        on, n_rows_on = on_pat.monitor_on()
        use, t_use = use_pat.monitor_use()
        a = np.random.randint(500000, 600000)
        a = a + i*day
        data_day = np.zeros((t), dtype=None)
        for i in range(n_rows_on-1):
            data_day[a+i] = on[i]

        for i in range(t_use-1):
            data_day[a+(n_rows_on-1)+i] = use[i]

        scale_factor = exist_power_factor_noise()
        data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def hairdryer(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        data, n_rows = use_pat.hairdryer_use()

        t1 = np.random.randint(2400, 4800)
        interpolated = interpol.interpolate(t1, n_rows, data, 2)

        t1_we = np.random.randint(2400, 6400)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, 2)


        my1 = 280000
        my2 = 600000
        sigma = 20000

        my1_we = 350000
        my2_we = 650000
        sigma_we = 40000


        s = np.random.randint(0, 2)
        if s == 0:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my1, sigma, interpolated, t1_we, my1_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final = data_final + data_day * scale_factor
        else:
            data_day = time_handle.time_handling(
                t, i, n_days, t1, my2, sigma, interpolated, t1_we, my2_we, sigma_we, interpolated_we)
            scale_factor = exist_power_factor_noise()
            data_final = data_final + data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def minioven(t):

    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):
        x = np.random.randint(1, 8)

        data, n_rows = use_pat.minioven_use()

        t1 = np.random.randint(1800, 6000)
        interpolated = interpol.interpolate(t1, n_rows, data, x)

        t1_we = np.random.randint(1800, 6400)
        interpolated_we = interpol.interpolate(t1_we, n_rows, data, x)


        my1 = 290000
        sigma1 = 20000
        my2 = 620000
        sigma2 = 40000

        my1_we = 350000
        sigma1_we = 30000
        my2_we = 650000
        sigma2_we = 50000


        s = np.random.randint(0, 2)
        if s == 0:
            try:
                data_day = time_handle.time_handling(
                    t, i, n_days, t1, my1, sigma1, data, t1_we, my1_we, sigma1_we, data)
                scale_factor = exist_power_factor_noise()
                data_final = data_final + data_day * scale_factor
            except IndexError:
                try:
                    data_day = time_handle.time_handling(
                        t, i, n_days, t1, my1, sigma1, data, t1_we, my1_we, sigma1_we, data)
                except IndexError:
                    pass
        else:
            try:
                data_day = time_handle.time_handling(
                    t, i, n_days, t1, my2, sigma2, data, t1_we, my2_we, sigma2_we, data)
                scale_factor = exist_power_factor_noise()
                data_final = data_final + data_day * scale_factor
            except IndexError:
                try:
                    data_day = time_handle.time_handling(
                        t, i, n_days, t1, my2, sigma2, data, t1_we, my2_we, sigma2_we, data)
                    scale_factor = exist_power_factor_noise()
                    data_final = data_final + data_day * scale_factor
                except IndexError:
                    pass

    data_final = np.transpose(data_final)

    return data_final


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
