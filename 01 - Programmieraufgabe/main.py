import numpy as np
import matplotlib.pyplot as plt

from eEuler import eEuler
# import iEuler
# import rk4


if __name__ == "__main__":

    u0 = 5 
    N = 1
    T_INTERVAL = [0, N]
    STEPS = 100

    def function_a(u, t):
        return -20 * u

    def an_method(t):
        return 5 * np.exp(-20 * t)


    eEuler_solver = eEuler(function_a, T_INTERVAL, u0, STEPS)
    # iEuler_solver = eEuler(fun, T_INTERVAL, u0, steps)
    # rk4_solver = eEuler(fun, T_INTERVAL, u0, steps)

    eEuler_solution, t_list = eEuler_solver.call()
    exact_solution = np.array([an_method(t) for t in t_list])



    # Visualisierung
    plt.figure(figsize=(10, 6))
    plt.plot(t_list, exact_solution, label="Analytische Lösung", linestyle="--", color="blue")
    plt.plot(t_list, eEuler_solution, label="Numerische Lösung (eEuler)", linestyle="-", color="red")



    plt.xlabel("t")
    plt.ylabel("u(t)")
    plt.title("Vergleich der analytischen und numerischen Lösung")
    plt.legend()
    plt.grid()
    # plt.show()
    plt.savefig("euler.png", dpi=300)

































'''
    u0 = 5  # Anfangswert
    steps = 100  # Anzahl der Schritte

    solver = eEuler(fun, T_INTERVAL, u0, steps)
    numerical_solution = solver.call()
    T_LIST = np.linspace(T_INTERVAL[0], T_INTERVAL[1], steps + 1)
    analytical_values = analytical_solution(T_LIST)

    # Visualisierung
    plt.figure(figsize=(10, 6))
    plt.plot(T_LIST, analytical_values, label="Analytische Lösung", linestyle="--", color="blue")
    plt.plot(T_LIST, numerical_solution, label="Numerische Lösung (eEuler)", linestyle="-", color="red")
    plt.xlabel("t")
    plt.ylabel("u(t)")
    plt.title("Vergleich der analytischen und numerischen Lösung")
    plt.legend()
    plt.grid()
    plt.show()

    '''
