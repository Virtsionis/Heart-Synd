import use_patterns as use_pat



def fridge(t):

    day = 864000
    n_days = t//day
    data, t = use_pat.fridge_use(t)

    return data


def FR_Heart(t):

    day = 864000
    n_days = t//day
    data, t = use_pat.FR_Heart_use(t)

    return data


def FRCombo_Heart(t):

    day = 864000
    n_days = t//day
    data, t = use_pat.FRCombo_Heart_use(t)

    return data
