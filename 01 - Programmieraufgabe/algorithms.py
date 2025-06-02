import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from scipy import optimize  


class eEuler:
    def __init__(self, fun, Y0=[0,1], t=[0,5], steps=10):
        self.fun = fun
        self.t = t
        self.Y0 = np.array(Y0, dtype=float)
        self.steps = steps
        self.tau = (t[1] - t[0]) / steps
        self.t_list = np.linspace(t[0], t[1], steps + 1)

    def testtt(self):
        print("testtt")
        return 0	

    def call(self):
        Y = self.Y0
        Y_list = [Y]
        for i in range(self.steps):
            Y = Y + self.tau * self.fun(self.t_list[i], Y)
            Y_list.append(Y)
        return self.t_list, np.array(Y_list)
    

class iEuler:
    def __init__(self, fun, Y0=[0,1], t=[0,5], steps=10):
        self.fun = fun
        self.t = t
        self.Y0 = np.array(Y0, dtype=float)
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
            Y_list.append(Y)
            tk = tk1
        return self.t_list, np.array(Y_list)
    

class RK4:
    def __init__(self, fun, Y0=[0,1], t=[0,5], steps=10):
        self.fun = fun
        self.t = t
        self.Y = np.array(Y0, dtype=float)
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



