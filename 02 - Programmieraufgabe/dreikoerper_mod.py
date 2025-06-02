import numpy as np

import matplotlib
import matplotlib.pyplot as plt 

from scipy import optimize  

import sys
import os

# Construct the relative path to the other folder
path_to_algorithms = os.path.abspath("../01 - Programmieraufgabe")
if path_to_algorithms not in sys.path:
    sys.path.insert(0, path_to_algorithms)

# from algorithms import eEuler


#Einschrittverfahren

tau = 0.01
STEPS = 10**4
t0 = 0.0
a = 4.3162774
b = 1.4916623
m1 = 200
m2 = 100
m3 = 100

r1 = np.array([0,0,0])
r2 = np.array([-10,0,0])
r3 = np.array([10,0,0])

v1 = np.array([0,0,b])
v2 = np.array([0,-a,-b])
v3 = np.array([0,a,-b])

u = np.hstack([r1,r2,r3,v1,v2,v3])

def drei_körper_problem(t0, u0):
    r1 = u0[0:3]
    r2 = u0[3:6]
    r3 = u0[6:9]
    v1 = u0[9:12]
    v2 = u0[12:15]
    v3 = u0[15:18]

    ode1 = -m2 * ((r1-r2) / np.linalg.norm(r1-r2)**3) - m3 * ((r1-r3) / np.linalg.norm(r1-r3)**3)
    ode2 = -m3 * ((r2-r3) / np.linalg.norm(r2-r3)**3) - m1 * ((r2-r1) / np.linalg.norm(r2-r1)**3)
    ode3 = -m1 * ((r3-r1) / np.linalg.norm(r3-r1)**3) - m2 * ((r3-r2) / np.linalg.norm(r3-r2)**3)

    new = np.zeros(18)
    new[0:3] = v1
    new[3:6] = v2
    new[6:9] = v3
    new[9:12] = ode1
    new[12:15] = ode2
    new[15:18] = ode3
    
    return new


class eEuler:
    def __init__(self, fun, u0=u, t=[0,1], tau=0.01, steps=10**4):
        self.fun = fun # Dreikörper_funktion
        self.t = t # Zeitintervall 0, 10000
        self.u0 = u0
        self.steps = steps
        self.tau = tau
        self.t_list = np.linspace(t[0], t[1], steps + 1)


    def call(self):
        Y = self.u0
        Y_list = [Y]
        for i in range(self.steps):
            Y = Y + self.tau * self.fun(self.t_list[i], Y)
            Y_list.append(Y)
        return self.t_list, np.array(Y_list)


'''
def vorwärts_euler(F, t0, u0, tau):
    return u0 + tau * F(t0, u0)

print(eEuler(drei_körper_problem, t0, u, tau))
'''

t_array, Y_array = eEuler(drei_körper_problem, Y0=u, t=[0,1], steps=10**4).call()































# Mehrschrittverfahren

steps = 10**4

def adams_bashforth(F, t0, u0, tau, steps):
    u = [u0]
    t = [t0]

    t1 = t0 + tau
    u1 = vorwärts_euler(F, t0, u0, tau)
    u.append(u1)
    t.append(t1)
    
    for k in range(1, steps):
        u_next = u[k] + tau * (3/2 * F(t[k], u[k]) - 1/2 * F(t[k-1], u[k-1]))
        t_next = t[k] + tau
        u.append(u_next)
        t.append(t_next)

    return u,t

u, t = adams_bashforth(drei_körper_problem, t0, u, tau, steps)

for k in [1,2,10,100]:
    print("u[{}] = {}".format(k, u[k]))
    print("t[{}] = {:.2f}".format(k, t[k]))


# Symplektisches Euler-Verfahren

def symplektisch_drei_körper_problem(tau, u0):
    r1 = u0[0:3]
    r2 = u0[3:6]
    r3 = u0[6:9]
    v1 = u0[9:12]
    v2 = u0[12:15]
    v3 = u0[15:18]

    ode1 = -m2 * ((r1-r2) / np.linalg.norm(r1-r2)**3) - m3 * ((r1-r3) / np.linalg.norm(r1-r3)**3)
    ode2 = -m3 * ((r2-r3) / np.linalg.norm(r2-r3)**3) - m1 * ((r2-r1) / np.linalg.norm(r2-r1)**3)
    ode3 = -m1 * ((r3-r1) / np.linalg.norm(r3-r1)**3) - m2 * ((r3-r2) / np.linalg.norm(r3-r2)**3)

    v1_new = v1 + tau * ode1
    v2_new = v2 + tau * ode2
    v3_new = v3 + tau * ode3

    r1_new = r1 + tau * v1_new
    r2_new = r2 + tau * v2_new
    r3_new = r3 + tau * v3_new

    u_new = np.concatenate([r1_new, r2_new, r3_new, v1_new, v2_new, v3_new])
    return u_new

def symplektischer_euler(u0, tau, steps):
    u = np.zeros((steps+1, len(u0)))
    u[0] = u0
    for i in range(steps):
        u[i+1] = symplektisch_drei_körper_problem(tau, u[i])
    return u
