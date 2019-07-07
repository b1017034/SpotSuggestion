import numpy as np




def insert(data):
    n = root



def post_difference(pre_latitude, pre_logitude, next_latitude, next_logitude):
    pre_spot = np.array([pre_latitude, pre_logitude])
    next_spot = np.array([next_latitude, next_logitude])

    return np.linalg.norm(next_spot - pre_spot)