import numpy as np
from scipy import optimize 
import matplotlib.pyplot as plt


class eEuler:
    def __init__(self, fun, t, Y0, steps):
        self.fun = fun
        self.t = t
        self.Y0 = Y0
        self.steps = steps
        self.tau = (t[1] - t[0]) / steps
        self.t_list = np.linspace(t[0], t[1], steps + 1)

    def call(self):
        Y = self.Y0
        Y_list = [Y]
        for i in range(self.steps):
            Y = Y + self.tau * self.fun(self.t_list[i], Y)
            Y_list.append(Y)
        return np.array(Y_list)



# ==========================================================

'''
def eEuler(fun, t, Y0, steps):
    tau = (t[1] - t[0]) / steps
    t_list = np.linspace(t[0], t[1], steps + 1)
    Y = Y0
    Y_list = [Y]
    for i in range(steps):
        Y = Y + tau * fun(t_list[i], Y)
        Y_list.append(Y)

    # print("Y_list", len(Y_list))
    return np.array(Y_list)
'''