import numpy as np
from scipy import optimize   

class iEuler:
    def __init__(self, fun, t, Y0, steps):
        self.fun = fun
        self.t = t
        self.Y0 = Y0
        self.steps = steps
        self.tau = (t[1] - t[0]) / steps
        self.t_list = np.linspace(t[0], t[1], steps + 1)

    def crank_nicolson_verfahren(self, x, Y, tk, t_k1):
        return Y + (self.tau / 2) * (self.fun(tk, Y) + self.fun(t_k1, x)) - x

    def call(self):
        Y = self.Y0
        Y_list = [Y]
        tk = self.t[0]
        

        for i in range(self.steps):
            tk1 = tk + self.tau
            Y = optimize.fsolve(self.crank_nicolson_verfahren, Y, args=(Y, tk, tk1))
            Y_list.append(Y.item())
            tk = tk1
        return self.t_list, Y_list





