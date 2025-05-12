import numpy as np

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
        return self.t_list, np.array(Y_list)




































'''
class ExplicitEuler:
    def __init__(self, f, u0, T, h):
        """
        f  : function f(u, t) defining the ODE du/dt = f(u, t)
        u0 : initial condition
        T  : total time
        h  : time step
        """
        self.f = f
        self.u0 = u0
        self.T = T
        self.h = h
        self.N = int(T / h)
        self.t = np.linspace(0, T, self.N + 1)
        self.u = np.zeros(self.N + 1)
        self.u[0] = u0
 
    def solve(self):
        """Perform the explicit Euler method."""
        for n in range(self.N):
            self.u[n + 1] = self.u[n] + self.h * self.f(self.u[n], self.t[n])
        return self.t, self.u

'''