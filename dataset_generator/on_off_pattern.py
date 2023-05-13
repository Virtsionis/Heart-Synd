import numpy as np
import use_patterns as use_pat
import on_patterns as on_pat
import off_patterns as off_pat
import standby_patterns as standby_pat


def TV(t):
    global use
    global on
    global off
    global standby

    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        use, t_use = use_pat.TV_use()
        on, n_rows_on = on_pat.TV_on()
        standby, t_standby = standby_pat.TV_standby()
        off, n_rows_off = off_pat.TV_off()

        # #original
        # a = np.random.randint(550000, 650000)

        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        # #change
        a = np.random.randint(hours_24[11], hours_24[17])

        a = a + i*day
        data = np.zeros((t), dtype=None)


        for i in range(n_rows_on-1):
            data[a+i] = on[i]

        for i in range(t_use-1):
            data[a+(n_rows_on-1)+i] = use[i]

        for i in range(t_standby-1):
            data[a+(n_rows_on-1)+(t_use-1)+i] = standby[i]

        for i in range(n_rows_off-1):
            data[a+(n_rows_on-1)+(t_use-1) +
                 (t_standby-1)+i] = off[i]
        scale_factor = exist_power_factor_noise()
        data_final += data * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def printer(t):
    global use
    global on
    global off

    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        r = np.random.randint(0, 1)
        use, t_use = use_pat.printer_use(r)
        on, n_rows_on = on_pat.printer_on()
        off, n_rows_off = off_pat.printer_off()
        a = np.random.randint(350000, 700000)
        a = a + i*day
        data = np.zeros((t), dtype=None)

        for i in range(n_rows_on-1):
            data[a+i] = on[i]

        for i in range(t_use-1):
            data[a+(n_rows_on-1)+i] = use[i]

        for i in range(n_rows_off-1):
            data[a+(n_rows_on-1)+(t_use-1)+i] = off[i]
        scale_factor = exist_power_factor_noise()
        data_final += data * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def coffeemachine(t):

    global use
    global on
    global off
    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        on, n_rows_on = on_pat.coffeemachine_on()
        off, n_rows_off = off_pat.coffeemachine_off()
        standby, t_standby = standby_pat.coffeemachine_standby()


        s = np.random.randint(0, 2)
        if s == 0:
            a = np.random.randint(300000, 350000)
            a = a + i*day
            data_day = np.zeros((t), dtype=None)

            for i in range(n_rows_on-1):
                data_day[a+i] = on[i]

            count = np.random.randint(1, 4)
            for i in range(count):
                r = np.random.randint(0, 3)
                use, t_use = use_pat.coffeemachine_use(r)
                for j in range(t_use-1):
                    data_day[a+(n_rows_on-1)+i*j] = use[j]

            for i in range(t_standby-1):
                data_day[a+(n_rows_on-1) +
                         (count*t_use-1)+i] = standby[i]

            for i in range(n_rows_off-1):
                data_day[a+(n_rows_on-1)+(count *
                                          t_use-1)+(t_standby-1)+i] = off[i]
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor

        else:
            b = np.random.randint(500000, 550000)
            b = b + i*day
            data_day = np.zeros((t), dtype=None)

            for i in range(n_rows_on-1):
                data_day[b+i] = on[i]

            count = np.random.randint(1, 4)
            for i in range(count):
                r = np.random.randint(0, 3)
                use, t_use = use_pat.coffeemachine_use(r)
                for j in range(t_use-1):
                    data_day[b+(n_rows_on-1)+i*j] = use[j]

            for i in range(t_standby-1):
                data_day[b+(n_rows_on-1) +
                         (count*t_use-1)+i] = standby[i]

            for i in range(n_rows_off-1):
                data_day[b+(n_rows_on-1)+(count *
                                          t_use-1)+(t_standby-1)+i] = off[i]
            scale_factor = exist_power_factor_noise()
            data_final += data_day * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def laptop(t):

    global use
    global on
    global off

    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        use, t_use = use_pat.laptop_use()
        on, n_rows_on = on_pat.laptop_on()
        off, n_rows_off = off_pat.laptop_off()
        a = np.random.randint(400000, 700000)
        a = a + i*day
        data = np.zeros((t), dtype=None)

        for i in range(n_rows_on-1):
            data[a+i] = on[i]

        for i in range(t_use-1):
            data[(a+n_rows_on-1)+i] = use[i]

        for i in range(n_rows_off-1):
            data[(a+n_rows_on-1)+(t_use-1)+i] = off[i]
        scale_factor = exist_power_factor_noise()
        data_final += data * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def lamp(t):

    global use
    global on
    global off

    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        use, t_use = use_pat.lamp_use()
        on, n_rows_on = on_pat.lamp_on()
        off, n_rows_off = off_pat.lamp_off()
        a = np.random.randint(600000, 700000)
        a = a + i*day
        data = np.zeros((t), dtype=None)

        for i in range(n_rows_on-1):
            data[a+i] = on[i]

        for i in range(t_use-1):
            data[(a+n_rows_on-1)+i] = use[i]

        for i in range(n_rows_off-1):
            data[(a+n_rows_on-1)+(t_use-1)+i] = off[i]
        scale_factor = exist_power_factor_noise()
        data_final += data * scale_factor

    data_final = np.transpose(data_final)

    return data_final


def gaming_PC(t):

    global use
    global on
    global off

    day = 864000
    n_days = t//day
    data_final = np.zeros((t), dtype=None)
    for i in range(n_days):

        r = np.random.randint(0, 2)
        use, t_use = use_pat.gaming_PC_use(r)
        on, n_rows_on = on_pat.gaming_PC_on()
        off, n_rows_off = off_pat.gaming_PC_off()

        # # original
        # a = np.random.randint(500000, 700000)

        hours_24 = [0, 37565, 75130, 112696, 150261, 187826,
                    225391, 262957, 300522, 338087, 375652, 413217, 450783,
                    488348, 525913, 563478, 601043, 638609, 676174, 713739,
                    751304, 788870, 826435, 864000]
        # #change
        a = np.random.randint(hours_24[16], hours_24[20])

        a = a + i*day
        data = np.zeros((t), dtype=None)

    
        for i in range(n_rows_on-1):
            data[a+i] = on[i]

        for i in range(t_use-1):
            data[a+(n_rows_on-1)+i] = use[i]

        for i in range(n_rows_off-1):
            data[a+(n_rows_on-1)+(t_use-1)+i] = off[i]
        scale_factor = exist_power_factor_noise()
        data_final += data * scale_factor



    data_final = np.transpose(data_final)

    return data_final


def exist_power_factor():
    existence_factor = np.random.normal(0.75, 0.4)
    if existence_factor > 0.5:
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

# uses are almost every day
# power level alternations are same as in the previous function
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