import numpy as np

def F(t,u):
    return -20 * u

A = np.array([[0, 1], [-1, 0]])


def F2(t,u_vektor):
    return A @ u_vektor

t0 = 0
#u0 = 5
u0 = np.array([0,1])
tau = 0.1
steps = 100

def vorwärts_euler(F, t0, u0, tau):
    return u0 + tau * F(t0, u0)


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
    

    
#print(vorwärts_euler(F, t0, u0, tau))
#print(adams_bashforth(F, t0, u0, tau, steps))

u,t = adams_bashforth(F,t0, u0, tau, steps)

for k in [1, 2, 10, 100]:
    print(u[k],t[k])