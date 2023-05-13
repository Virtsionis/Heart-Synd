import read_csv_data as csv_r


def coffeemachine_off():

    filename = 'Coffee_Machine_ON.csv'
    root_dir = 'data/coffeemachine/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def printer_off():

    filename = 'Printer_OFF.csv'
    root_dir = 'data/printer/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def TV_off():

    filename = 'TV_OFF.csv'
    root_dir = 'data/TV/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def laptop_off():

    filename = 'Laptop_OFF.csv'
    root_dir = 'data/laptop/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def lamp_off():

    filename = 'LAMP_OFF.csv'
    root_dir = 'data/lamp/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def gaming_PC_off():

    filename = 'Gaming_PC_OFF.csv'
    root_dir = 'data/gaming_PC/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows
