import read_csv_data as csv_r



def coffeemachine_on():

    filename = 'Coffee_Machine_OFF.csv'
    root_dir = 'data/coffeemachine/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def printer_on():

    filename = 'Printer_ON.csv'
    root_dir = 'data/printer/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def TV_on():

    filename = 'TV_ON.csv'
    root_dir = 'data/TV/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def laptop_on():

    filename = 'Laptop_ON.csv'
    root_dir = 'data/laptop/'
    data, n_rows = csv_r.csv_read(filename, root_dir)
    return data, n_rows


def lamp_on():

    filename = 'LAMP_ON.csv'
    root_dir = 'data/lamp/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def gaming_PC_on():

    filename = 'Gaming_PC_ON.csv'
    root_dir = 'data/gaming_PC/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def monitor_on():

    filename = 'Monitor_ON.csv'
    root_dir = 'data/monitor/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows


def fridge_on():

    filename = 'Fridge_ON.csv'
    root_dir = 'data/fridge/'
    data, n_rows = csv_r.csv_read(filename, root_dir)

    return data, n_rows
