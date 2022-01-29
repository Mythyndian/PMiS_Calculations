import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import math

sns.set()

t = np.linspace(0, 100, 1000)
x = [0, 0]
delta = 0.62
k = 30.5
m = 59
omega = math.sqrt(k / m)
A = 0.1


def sho(t, x):
    result = [
        x[1],
        (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(2 * omega * t)),
    ]
    return result


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
plt.plot(t, solution.y[0], "b")
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title("Oscylator z tłumieniem i z wymuszeniem dla 2 $\omega$", fontsize=18)
plt.grid(True)
plt.show()
