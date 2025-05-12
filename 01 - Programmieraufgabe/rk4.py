import numpy as np

class RK4:
    def __init__(self, fun, t, Y0, steps):
        self.fun = fun
        self.t = t
        self.Y = Y0
        self.steps = steps
        self.tau = (t[1] - t[0]) / steps
        self.t_list = np.linspace(t[0], t[1], steps + 1)

    def call(self):
        Y_list = [self.Y]

        for i in range(self.steps):
            k1 = self.tau * self.fun(self.t, self.Y)
            k2 = self.tau * self.fun(self.t, self.Y + 0.5 * k1)
            k3 = self.tau * self.fun(self.t, self.Y + 0.5 * k2)
            k4 = self.tau * self.fun(self.t, self.Y + k3)

            self.Y = self.Y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
            Y_list.append(self.Y)

        return self.t_list, np.array(Y_list)